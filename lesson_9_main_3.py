import lesson_9_library
import lesson_9_constants


def main():
    total_loan_amount = float(input(lesson_9_constants.MSG_USER_INPUT_LOAN_AMOUNT))
    monthly_income = float(input(lesson_9_constants.MSG_USER_INPUT_SALARY))

    result = lesson_9_library.can_get_loan(total_loan_amount, monthly_income)

    if result:
        print("Банк може видати позику.")
    else:
        print("Банк не може видати позику через великий щомісячний платіж.")


if __name__ == '__main__':
    main()