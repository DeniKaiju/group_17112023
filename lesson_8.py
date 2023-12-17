# from pprint import pprint

import json
import requests

url = 'https://dummyjson.com/quotes?limit=100'

response = requests.get(url=url)
data_from_net = response.json()

with open('data.json', mode='w') as file:
    json.dump(data_from_net, file, indent=4)
