import lesson_11_set_dict_constants


def get_cities_from_user(prompt):
    cities_input = input(prompt)
    cities = set(cities_input.lower().split())
    return cities
