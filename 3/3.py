import random
import pickle
import nltk
from nltk.corpus import movie_reviews

nltk.download('movie_reviews')

doc = [(list(movie_reviews.words(fileid)), category)
       for category in movie_reviews.categories()
       for fileid in movie_reviews.fileids(category)]
random.shuffle(doc)
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print("Найвживаніші слова: ", all_words.most_common(20))

print("Слово 'miracle' вживається ", all_words["miracle"], "разів.")

pos_words = []
neg_words = []
for f in doc:
    if f[1] == 'neg':
        for w in f[0]:
            neg_words.append(w.lower())
    else:
        for w in f[0]:
            pos_words.append(w.lower())
pos_words = nltk.FreqDist(pos_words)
neg_words = nltk.FreqDist(neg_words)
print("К-ть вживань серед позитивних відгуків: ", pos_words['digital'])
print("К-ть вживань серед негативних відгуків: ", neg_words['digital'])

word_features = list(all_words.keys())[:2200]


def find_features(d):
    words = set(d)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features


found_words = []
for k, v in find_features(movie_reviews.words('pos/cv002_15918.txt')).items():
    if v is True:
        found_words.append(k)
print('Найвживаніші слова з поданого файлу: ', found_words)

featuresets = [(find_features(rev), category)
               for (rev, category) in doc]
training_set = featuresets[:1800]
testing_set = featuresets[:1800]

classifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

print("Відсоток точності наївного баєсівського алгоритму складає ",
      (nltk.classify.accuracy(classifier, testing_set)) * 100, '%')
classifier.show_most_informative_features(20)

from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import NuSVC

NuSVC_classifier = SklearnClassifier(NuSVC(),
                                     sparse=False).train(training_set)
save_classifier = open("NuSVC.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
classifier_fs = open("NuSVC.pickle", "rb")
svc_classifier = pickle.load(classifier_fs)
classifier_fs.close()

print("Відсоток точності алгоритму NuSVC: ",
      (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)
