import lesson_9_library
import lesson_9_constants


def main():
    centimeters = float(input(lesson_9_constants.MSG_USER_INPUT_CM))

    inches_result = lesson_9_library.convert_cm_to_inch(centimeters)
    print(f"{centimeters} см дорівнюють {inches_result:.2f} дюймам")


if __name__ == '__main__':
    main()
