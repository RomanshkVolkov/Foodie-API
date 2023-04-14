import requests
from bs4 import BeautifulSoup

from .similarity import find_closest_title
from .utils import get_user_agent


def get_exact_ingredient(search_page_url, search_text, training_mode):
    response = requests.get(search_page_url, headers=get_user_agent())
    if (response.status_code != 200):
        return None
    page = BeautifulSoup(response.text, "html.parser")

    titles = [
        span.text
        for span in page.find_all("span", attrs={"data-automation-id": "product-title"})
    ]
    for title in titles:
        print(title)
    closest_title = find_closest_title(search_text, titles, training_mode)
    return closest_title


def get_ingredient_url(search_page_url):
    response = requests.get(search_page_url, headers=get_user_agent())
    if (response.status_code != 200):
        return None
    page = BeautifulSoup(response.text, "html.parser")

    a_tag = page.find(
        "a", class_="absolute w-100 h-100 z-1 hide-sibling-opacity")

    if not a_tag:
        return None
    url = a_tag["href"]
    return url
