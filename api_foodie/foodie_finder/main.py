from .scrapper import get_exact_ingredient, get_ingredient_url


def get_ingredient_url_from_name(ingredient_name):
    BASE_PAGE_URL = "https://super.walmart.com.mx/"
    BASE_SEARCH_PAGE_URL = "https://super.walmart.com.mx/search?q="

    search_page_url = BASE_SEARCH_PAGE_URL + ingredient_name

    exact_ingredient = get_exact_ingredient(search_page_url, ingredient_name)
    exact_search_page_url = BASE_SEARCH_PAGE_URL + exact_ingredient

    ingredient_url = BASE_PAGE_URL + get_ingredient_url(exact_search_page_url)
    return ingredient_url


def main(ingredient):
    ingredient_url = get_ingredient_url_from_name(ingredient)
    return ingredient_url
