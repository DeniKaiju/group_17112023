# from pprint import pprint

import requests

url = 'https://script.google.com/macros/s/AKfycbzjh0-mOMTcbN-tsA43wH62_yR-8ayNbpD-XBsI4LMMooksQIECKRONd3-2vQLx4eCI/exec'

response = requests.get(url=url)
data_from_net = response.json()

# pprint(data_from_net)
large_families_count = 0
credit_more_than_income = 0
women_with_house = 0

for client in data_from_net['clients']:
    if client['age'] > 35 and client['large_family'] is True:
        print(f"{client['name']}: {client['monthly_income']}")

    if client['large_family'] is True:
        large_families_count += 1
        large_families_amount = f"Кількість багатодітних сімей: {large_families_count}"
    if client['Loan_expense_per_month'] > client['monthly_income']:
        credit_more_than_income += 1
        loan_more_income = f"Кількість сімей, в яких витрати за кредитами більші за доходи: {credit_more_than_income}"
    if client['gender'] == 'Ж' and client['Owning_own_home'] is True:
        women_with_house += 1
        result_women_with_houses = f"Кількість жінок забезпечених власним житлом: {women_with_house}"

print(large_families_amount)
print(loan_more_income)
print(result_women_with_houses)
