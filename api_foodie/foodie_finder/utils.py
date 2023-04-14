import spacy
import re
import nltk
import csv

if not nltk.download('stopwords', quiet=True):
    nltk.download('stopwords')
if not nltk.download('punkt', quiet=True):
    nltk.download('punkt')

nlp = spacy.load("es_core_news_sm")
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

    return " ".join(stems)

def get_relevance_score():
    while True:
        try:
            score = int(input("Enter relevance score (1-5): "))
            if 1 <= score <= 5:
                return score
            else:
                print("Please enter a valid score between 1 and 5.")
        except ValueError:
            print("Please enter a valid score between 1 and 5.")

def save_result_to_csv(search_text, title, jaccard_score, relevance_score):
    with open("results.csv", "a", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["search_text", "title", "jaccard_score", "relevance_score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({
            "search_text": search_text,
            "title": title,
            "jaccard_score": jaccard_score,
            "relevance_score": relevance_score
        })

def get_relevance_score_from_csv(search_term, title):
    with open("results.csv", "r", newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        total_relevance_score = 0
        count = 0

        for row in csvreader:
            if row[0] == search_term and row[1] == title:
                total_relevance_score += float(row[3])
                count += 1

        if count > 0:
            return total_relevance_score / count  # Devuelve el promedio de los scores de relevancia
        else:
            return 0  # Si no se encuentra la combinación de término de búsqueda y título, devuelve 0