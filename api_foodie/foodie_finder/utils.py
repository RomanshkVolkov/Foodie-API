import es_core_news_sm
import spacy
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')

nlp = es_core_news_sm.load()

stopwords = nltk.corpus.stopwords.words("spanish")


def get_user_agent():
    return {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}


def format(text):
    return re.sub(r'[^a-z]+', '', text.lower())


def preprocess(text):
    formatted_text = format(text)

    # Tokenización y eliminación de palabras irrelevantes
    tokens = [token.lower() for token in nltk.word_tokenize(formatted_text)
              if token.lower() not in stopwords and re.match(r"[a-zA-Záéíóú]+", token)]

    # Stemming
    stems = [nlp(token)[0].lemma_ for token in tokens]
    print(stems)

    return " ".join(stems)
