import lesson_9_library
import lesson_9_constants


def main():
    input_numbers = lesson_9_library.convert_str_to_int_list(input(lesson_9_constants.MSG_USER_INPUT_NUMBERS_LIST))
    even_numbers = lesson_9_library.filter_even_numbers(input_numbers)
    print("Список парних чисел:", even_numbers)


if __name__ == '__main__':
    main()
