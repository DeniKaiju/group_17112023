import json
import requests
import pymongo
from config import USER, PASSWORD

url = 'https://dummyjson.com/quotes?limit=100'
response = requests.get(url=url)
data_from_net = response.json()
quotes_list = data_from_net['quotes']

url = 'mongodb+srv://{user}:{password}@cluster0.tbcrbjt.mongodb.net/?retryWrites=true&w=majority'.format(
    user=USER, password=PASSWORD)

client = pymongo.MongoClient(url)
db = client['citations']

collection = db['quotes']
collection.insert_many(quotes_list)
