import decimal

print("~" * 40)

name = input("Enter your name>>> ").strip().capitalize()
age = input("Enter your age>>> ")
print(age.isdigit())

salary = input("Enter your salary>>>")

retirement = 65 - int(age)

total_money_earned = decimal.Decimal(int(retirement)*12*float(salary))
total_money_earned_usd = decimal.Decimal(float(total_money_earned) / 37.3)
round_total_usd = total_money_earned_usd.quantize(decimal.Decimal('0.00'))

cars_amount = decimal.Decimal(int(total_money_earned_usd)/35000)
cars_round = cars_amount.quantize(decimal.Decimal('0'))

print("I'm " + name," and I can earn only " f'{round_total_usd}'" USD, this money will be enough only for " f'{cars_round}'" Toyots, I don't like it, so I'm going to change my life and study programming with a vengeance!")
