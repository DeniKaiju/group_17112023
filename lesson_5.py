import requests

url_carts = 'https://dummyjson.com/carts'

response = requests.get(url=url_carts)
data_from_net = response.json()
carts = data_from_net['carts']

for cart in carts:
    if cart['userId'] == 56:
        pass
        for product in cart['products']:
            if product['discountPercentage'] > 15:
                print(product['title'])
