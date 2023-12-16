import json
import requests
import pymongo
from config import USER, PASSWORD

# Отримання даних з мережі
url = 'https://dummyjson.com/quotes?limit=100'
response = requests.get(url=url)
data_from_net = response.json()

# Підключення до бази даних MongoDB
url = 'mongodb+srv://{user}:{password}@cluster0.tbcrbjt.mongodb.net/?retryWrites=true&w=majority'.format(
    user=USER, password=PASSWORD)

client = pymongo.MongoClient(url)
db = client['citations']

collection = db['quotes']
collection.insert_one(data_from_net)

author = "Albert Einstein"
quotes_by_author = collection.find({"author": author})

for quote in quotes_by_author:
    print(quote)
