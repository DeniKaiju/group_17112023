import lesson_11_set_dict_library
import lesson_11_set_dict_constants


def main():
    visited_cities = lesson_11_set_dict_library.get_cities_from_user(lesson_11_set_dict_constants.MSG_USER_visited_cities)

    future_cities = lesson_11_set_dict_library.get_cities_from_user(lesson_11_set_dict_constants.MSG_USER_future_cities)

    common_cities = visited_cities.intersection(future_cities)
    if common_cities:
        print("Схоже, що вам дуже сподобалося в цих містах:")
        for city in common_cities:
            print(city.capitalize())
    else:
        print("Ви відкриті до чогось нового!")


if __name__ == '__main__':
    main()
