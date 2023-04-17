import requests
from bs4 import BeautifulSoup

from .similarity import find_closest_title
from .utils import get_user_agent


def get_ingredient_id(search_page_url, search_text, training_mode):
    response = requests.get(search_page_url, headers=get_user_agent())
    if (response.status_code != 200):
        return None
    page = BeautifulSoup(response.text, "html.parser")

    titles = [
        span.text
        for span in page.find_all("span", attrs={"data-automation-id": "product-title"})
    ]
    closest_title = find_closest_title(search_text, titles, training_mode)

    id = None
    for a_tag in page.find_all('a', href=True):
        if closest_title in a_tag.text:
            id = a_tag['href']
            break
    return id
