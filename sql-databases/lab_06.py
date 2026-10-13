'''
Lab06 MongoDB NoSQL 261013
'''

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27018/")
db = client["webshop"]

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
# result = db.customers.insert_one(
    # {'first_name': 'Daniel', 'last_name': 'Nilsson', 'email': 'dan@nil.se', 'city': 'Göteborg'})
# print(result.inserted_id)

# pprint(db.customers.find_one({'email': 'dan@nil.se'}))

#Ex8

