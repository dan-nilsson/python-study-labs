'''
Lab06 MongoDB NoSQL 261013
'''

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27018/')
db = client['webshop']

#Ex1
# print(*[doc['name'] for doc in db.products.find({'category': 'Accessories'})],sep='\n')

#Ex2
# print(*[f'{doc['first_name']} {doc['last_name']}' for doc in db.customers.find({'city': 'Göteborg'})],sep='\n')

#Ex3
# print(*[f'Name: {doc['name']} Price: {doc['price']} kr' for doc in db.products.find({})],sep='\n')

#Ex4
# print(db.customers.count_documents({'city': 'Uppsala'}))

#Ex5
# print(db.products.find_one({'name': 'Sandals'})['stock'])

#Ex6
# print(*[f'{doc['first_name']}' for doc in db.customers.find({'newsletter': True})],sep='\n')

#Ex7
def insert_me():
    result = db.customers.insert_one(
        {'first_name': 'Daniel', 'last_name': 'Nilsson', 'email': 'dan@nil.se', 'city': 'Göteborg'})
    print(result.inserted_id)
    pprint(db.customers.find_one({'email': 'dan@nil.se'}))

# insert_me()

#Ex8
def insert_many_many():
    db.products.insert_many([
        {'_id': 13, 'name': 'Scarf', 'category': 'Accessories', 'price':299,
            'stock':15, 'tags':['winter'], 'details': {'color': 'red'}},
        {'_id': 14, 'name': 'Gloves', 'category': 'Accessories', 'price':199,
              'stock':20, 'tags':['winter'], 'details': {'color': 'black'}}])
    print(db.products.count_documents({}))

# insert_many_many()

#Ex9
def get_customers_info():
    result = db.customers.find({})
    print(*[f'{'{:<25}'.format(f'{doc['first_name']} {doc['last_name']}')}'
            f'{'{:<10}'.format(f'{doc.get('city','unknown')}')}' for doc in result],sep='\n')

# get_customers_info()

#Ex10
def order_sizes():
    print(*[f'Order {doc['_id']:<3}: {len(doc['items'])} items' for doc in db.orders.find({})],sep='\n')

# order_sizes()