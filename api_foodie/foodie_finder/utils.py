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


def user_agent_rotator():
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        # Agrega más User-Agents si lo deseas
    ]
    while True:
        for user_agent in user_agents:
            yield user_agent


user_agent_generator = user_agent_rotator()


def get_user_agent():
    return {"User-Agent": next(user_agent_generator)}


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
        fieldnames = ["search_text", "title",
                      "jaccard_score", "relevance_score"]
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
            # Devuelve el promedio de los scores de relevancia
            return total_relevance_score / count
        else:
            return 0  # Si no se encuentra la combinación de término de búsqueda y título, devuelve 0
