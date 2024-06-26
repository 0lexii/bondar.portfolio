print("Введіть, будь ласка, рядок тексту")
user_text = input()

voc = {'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'ґ', 'h': 'х', 'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'ку', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'ф', 'w': 'в', 'x': 'кс', 'y': 'ю', 'z': 'з', 'ß': 'с', 'ch': 'х', 'sch': 'ш', 'tsch': 'щ', 'ei': 'ай', 'ie': 'і', 'eu': 'ой', 'ö': 'ьо', 'ä': 'е', 'ü': 'у'}


def transcribe(text):
    result = str()
    for i in text:
        result += voc.get(i.lower(), i.lower()).capitalize() if i.isupper() else voc.get(i, i)
    return result


print(str(transcribe(user_text)))
