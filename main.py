from pydantic.v1.validators import anystr_lower
from spacy.lang.ru import Russian
from spacy.lang.ru.stop_words import STOP_WORDS
import ru_core_news_md
import asyncio
from textblob import TextBlob
#from translate import Translator
from googletrans import Translator
model = ru_core_news_md.load()

text = model("Фильм так себе,слабый сюжет и актерская игра просто ужасна")
print(text)
text_list = [word.lemma_ for word in text]
filter_text_list= [elem for elem in text_list if not elem in STOP_WORDS]
print(text_list)
print(filter_text_list)

ru_text = " ".join(filter_text_list)
#translator = Translator(from_lang="Russian", to_lang="English")
#eng_text = translator.translate(ru_text)
async def Translate_text(text):
    translator = Translator()
    translated = await translator.translate(text, src='ru',dest='en')

    return translated.text
eng_text = asyncio.run(Translate_text(ru_text))

analys = TextBlob(eng_text)
sentiment= analys.sentiment.polarity

if sentiment >0:
    print("pos")
elif sentiment <0:
    print("neg")
else:
    print("neytral")