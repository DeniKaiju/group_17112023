dirty_list = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$".strip('6..5874$:?$').title().split()

cities = list(dirty_list)

for city in cities:
    message = f'Я \U00002764 {city}'
    print(message)
