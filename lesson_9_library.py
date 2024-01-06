

def convert_cm_to_inch(cm):
    inches = cm / 2.54
    return inches


def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


def convert_str_to_int_list(input_str):
    return [int(num) for num in input_str.split()]


def can_get_loan(total_loan_amount, monthly_income):
    total_months = 25 * 12

    max_monthly_payment = 0.35 * monthly_income

    monthly_payment = total_loan_amount / total_months

    if monthly_payment <= max_monthly_payment:
        return True
    else:
        return False
