from operator import itemgetter
from nltk.probability import FreqDist
import difflib
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nltk.download('punkt')

word1 = wn.synsets('hell', pos=wn.NOUN)
word2 = wn.synsets('bell', pos=wn.NOUN)

for synset in wn.synsets('hell', wn.NOUN):
    print(synset.name() + ":", synset.definition())

for synset in wn.synsets('bell', wn.NOUN):
    print(synset.name() + ":", synset.definition())

for i in word1:
    x = i.hyponyms()
    if len(x) == 0:
        print(f'{i}: no hyponyms')
    else:
        print(f'{i}: ', x)

for i in word2:
    x = i.hyponyms()
    if len(x) == 0:
        print(f'{i}: no hyponyms')
    else:
        print(f'{i}: ', x)

for i in word1:
    x = i.hypernyms()
    if len(x) == 0:
        print(f'{i}: no hypernyms')
    else:
        print(f'{i}: ', x)

for i in word2:
    x = i.hypernyms()
    if len(x) == 0:
        print(f'{i}: no hypernyms')
    else:
        print(f'{i}: ', x)

w1 = wn.synset('hell.n.01')
w2 = wn.synset('bell.n.01')
print('hell:', w1.min_depth())
print('bell:', w2.min_depth())
print(w1.lowest_common_hypernyms(w2))
print(w2.lowest_common_hypernyms(w1))

print(w1.path_similarity(w2))
print(w1.wup_similarity(w2))
print(w1.lch_similarity(w2))


def levenshtein(s1, s2):
    d = {}
    s1_length = len(s1)
    s2_length = len(s2)
    for i in range(-1, s1_length + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, s2_length + 1):
        d[(-1, j)] = j + 1

    for i in range(s1_length):
        for j in range(s2_length):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost,
            )
    return d[s1_length - 1, s2_length - 1]


word1 = 'hell'
word2 = 'bell'
dl = levenshtein(word1, word2)
print(f"Result for '{word1}' & '{word2}':", dl)


def damerau_levenshtein_distance(s1, s2):
    d = {}
    s1_length = len(s1)
    s2_length = len(s2)
    for i in range(-1, s1_length + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, s2_length + 1):
        d[(-1, j)] = j + 1

    for i in range(s1_length):
        for j in range(s2_length):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost,
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)

    return d[s1_length - 1, s2_length - 1]


word1 = 'hell'
word2 = 'bell'
dld = damerau_levenshtein_distance(word1, word2)
print(f"Result for '{word1}' & '{word2}':", dld)


def dict_distance(word, num_words):
    file = open(r'1-1000.txt', 'r')
    lines = file.readlines()
    file.close()

    distances = {}
    for line in lines:
        word_distance = levenshtein(word, line.strip())
        distances[line.strip()] = word_distance
    sorted_dict = sorted(distances.items(), key=
    itemgetter(1))
    closest_words = []
    for i in range(num_words):
        closest_words.append(sorted_dict[i])
    return closest_words


word = input('Введіть рандомне слово: ')
print(word, ": ", dict_distance(word, 6))


file = open('austen-persuasion.txt', 'r')
tokenized_austen = nltk.word_tokenize(file.read())
words = []
for word in tokenized_austen:
    if word.isalpha():
        words.append(word.lower())

nlp_words = FreqDist(words)
nlp_words.items()


def convert_tuple(tup):
    st = ''.join(map(str, tup[0]))
    return st


f = open('sorted.txt', "w")
for word in nlp_words.most_common():
    myStr = convert_tuple(word)
    f.write(myStr + '\n')


f.close()


user_word = input("Знову введіть рандомне слово: ")
f = open('sorted.txt', "r")
words = f.read()
words_list = words.split('\n')
closest = difflib.get_close_matches(user_word, words_list, n=6)
print(user_word, ': ', closest)
