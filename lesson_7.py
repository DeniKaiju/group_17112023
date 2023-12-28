import csv

file_path = 'C:\\Users\\Yarik\\Desktop\\airport-codes_csv.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=';')

    for row in csv_reader:
        if 'iso_country' in row and row['iso_country'] == 'UA':
            print(row['name'])