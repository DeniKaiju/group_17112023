# from pprint import pprint

import requests
url = 'https://script.google.com/macros/s/AKfycbyc7HcC4tzepOtMlZOIxQQazrcp94GylCFRdv47Xnch6l87H2t67o8XbLH8OQUT0IR6/exec'

response = requests.get(url=url)
data_from_net = response.json()

# pprint(data_from_net)

for client in data_from_net['clients']:
    if client['age'] > 35:
        pass
        if client['large_family'] == 'Так':
            print(f"{client['name']}: {client['monthly_income']}")

large_families_count = 0

for client in data_from_net['clients']:
    if client['large_family'] == 'Так':
        large_families_count += 1

print(f"Кількість багатодітних сімей: {large_families_count}")

credit_more_than_income = 0

for client in data_from_net['clients']:
    if client['Loan_expense_per_month'] > client['monthly_income']:
        credit_more_than_income += 1

print(f"Кількість сімей, в яких витрати за кредитами більші за доходи: {credit_more_than_income}")

women_with_house = 0

for client in data_from_net['clients']:
    if client['gender'] == 'Ж' and client['Owning_own_home'] == 'Так':
        women_with_house += 1

print(f"Кількість жінок забезпечених власним житлом: {women_with_house}")
