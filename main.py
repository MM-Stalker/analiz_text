from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS

model = Russian()

text = model("Фильм так себе,слабый сюжет и актерская игра просто ужасна")
print(text)
text_list = [word for word in text]
print(text_list)