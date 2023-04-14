from .scrapper import get_ingredient_id


def get_ingredient_url_from_name(ingredient_name, training_mode):
    BASE_PAGE_URL = "https://super.walmart.com.mx/"
    BASE_SEARCH_PAGE_URL = "https://super.walmart.com.mx/search?q="

    search_page_url = BASE_SEARCH_PAGE_URL + ingredient_name

    ingredient_id = get_ingredient_id(search_page_url, ingredient_name, training_mode)

    # Comprobar si exact_ingredient es None antes de concatenar
    if ingredient_id is None:
        raise ValueError(f"No se pudo encontrar un ingrediente exacto para '{ingredient_name}'")
    
    ingredient_url = BASE_PAGE_URL + ingredient_id
        
    return ingredient_url


def main(ingredient, training_mode):
    print(training_mode)
    ingredient_url = get_ingredient_url_from_name(ingredient, training_mode)
    return ingredient_url
