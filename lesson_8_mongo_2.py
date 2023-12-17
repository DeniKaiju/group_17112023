import pymongo
from config import USER, PASSWORD

url = 'mongodb+srv://{user}:{password}@cluster0.tbcrbjt.mongodb.net/?retryWrites=true&w=majority'.format(
    user=USER, password=PASSWORD)
client = pymongo.MongoClient(url)
db = client['citations']
collection = db['quotes']

selected_author_einstein = 'Albert Einstein'
quotes = collection.find({'author': selected_author_einstein})

# Перевірка вибранного автора 'Albert Einstein'
# for quote in quotes:
#     if quote['author'] == selected_author_einstein:
#         print(quote.get('quote'))

search_text = {'quote': {'$regex': 'success'}}
result = collection.find(search_text)

# Перевірка вибранного слова 'success'
# for quote in result:
#     print(quote.get('quote'))

selected_author_twain = {'author': 'Mark Twain'}
new_data = {'$set': {'favorite': True}}
processed = collection.update_many(selected_author_twain, new_data)

quote_gogh = {'author': 'Vincent Van Gogh'}
deleted_gogh = collection.delete_many(quote_gogh)

query = {}
deleted_quotes = collection.delete_many(query)
