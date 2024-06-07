import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# Функція для побудови частотного словника
def freq_table(text_string) -> dict:
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    freqTable = dict()
    for word in words:
        word = ps.stem(word.lower())  # Зведення до нижнього регістру
        if word in stop_words:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    return freqTable


# Зчитування тексту з файлу
with open("timemanagement.txt", "r") as my_file:
    test_text = my_file.read()


# Функція для оцінки речень на основі частотного словника
def score_sentences(sentences, freqTable) -> dict:
    sent_value = dict()
    for sent in sentences:
        word_count_in_sentence = len(word_tokenize(sent))
        sent_value[sent] = 0
        for word in word_tokenize(sent.lower()):
            word = PorterStemmer().stem(word)
            if word in freqTable:
                sent_value[sent] += freqTable[word]
        if word_count_in_sentence > 0:  # Додавання перевірки на випадок порожнього речення
            sent_value[sent] = sent_value[sent] / word_count_in_sentence
    return sent_value


# Виклик функцій для створення частотного словника та токенізації речень
ft = freq_table(test_text)
s = sent_tokenize(test_text)
sv = score_sentences(s, ft)


# Функція для обчислення середнього балу речень
def avg_score(sentValue) -> float:
    sumValues = sum(sentValue.values())
    average = sumValues / len(sentValue)
    return average


avg = avg_score(sv)
print("Поріг тексту: ", avg)


# Функція для створення реферату на основі балів речень та порогу
def summary(sentences, sentValue, threshold, max_sentences=None):
    summary = ''
    count = 0

    threshold *= 1.2

    for sent in sentences:
        if sent in sentValue and sentValue[sent] > threshold:
            summary += " " + sent
            count += 1
            if max_sentences and count >= max_sentences:
                break  # Припиняємо додавання речень, якщо досягнуто максимум
    return summary


max_sentences = 5
summ = summary(s, sv, avg, max_sentences)
print("Реферат: ", summ)
