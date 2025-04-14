from pydantic.v1.validators import anystr_lower
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
from textblob import TextBlob
model = ru_core_news_md.load()

text = model("Фильм так себе,слабый сюжет и актерская игра просто ужасна")
print(text)
text_list = [word.lemma_ for word in text]
filter_text_list= [elem for elem in text_list if not elem in STOP_WORDS]
print(text_list)
print(filter_text_list)

analys = TextBlob(str(filter_text_list))
sentiment= analys.sentiment.polarity

if sentiment >0:
    print("pos")
elif sentiment <0:
    print("neg")
else:
    print("neytral")