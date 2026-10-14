'''
Lab7 MongoDB NoSQL 261014
'''

from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

from dbtools import mongodb_connect,mongodb_seed

db = mongodb_connect()

#Ex1
def find_price_gt_1000():
    result = db.products.find({'price': {'$gt' : 1000}})
    print(*[f'Name: {doc.get('name'):<20} Price: {doc.get('price')} kr' 
        for doc in result],sep='\n')
# 
# find_price_gt_1000()

#Ex2
def orders_delivered():
    result = db.orders.find({'status': {'$ne' : 'delivered'}})
    print(*[f'ID::{doc.get('_id'):<3} Status: {doc.get('status')}' 
        for doc in result],sep='\n')
# 
# orders_delivered()


#Ex3
def customers_sthlm_mlm():
    result = db.customers.find({'city': {'$in': ['Stockholm','Malmlö']}})
    print(*[f'Name: {doc.get('first_name')} {doc.get('last_name')}' for doc in result],sep='\n')

# customers_sthlm_mlm()

#Ex4
def white_products():
    result = db.products.find({'details.color': 'white'})
    print(*[f'Product: {doc.get('name')}' for doc in result],sep='\n')

# white_products()

#Ex5
def sport_tag_products():
    result = db.products.find({'tags': 'sport'})
    print(*[f'Product: {doc.get('name')}' for doc in result],sep='\n')

# sport_tag_products()

#Ex6
def five_cheapest_products():
    result = db.products.find().sort('price',1).limit(5)
    print(*[f'Product: {doc.get('name'):<15} Price: {doc.get('price')}' for doc in result],sep='\n')

# five_cheapest_products()

#Ex7
def orders_containing_productid_two():
    result = db.orders.find({'items.product_id': 2})
    print(*[f'OrderID: {doc.get('_id')}' for doc in result],sep='\n')

# orders_containing_productid_two()

#Ex8
def accessories_inc_price_20():
    result = db.products.find({'category': {'$eq': 'Accessories'}})
    print(*[f'Product: {doc.get('name'):<15} Price: {doc.get('price')} kr' for doc in result],sep='\n')
    result = db.products.update_many({'category': {'$eq': 'Accessories'}},{'$inc': {'price': 20}})
    print(result.matched_count ,result.modified_count)

# accessories_inc_price_20()

#Ex9
def rain_jacket_updates():
    result = db.products.update_one({'name': 'Rain Jacket'},
        {'$push': {'tags': 'new'}, '$set': {'restock_date': datetime.now()}})
    print(result.matched_count, result.modified_count)

# rain_jacket_updates()

#Ex10
def delete_new_before_date(date):
    result = db.orders.find({'status': 'new', 'order_date': {'$lt': date}})
    print(*[f'{doc.get('_id'):<3} {doc.get('order_date')}' for doc in result])
    result = db.orders.delete_many({'status': 'new', 'order_date': {'$lt': date}})
    print(result.deleted_count)

# delete_new_before_date(datetime(2026,3,20))