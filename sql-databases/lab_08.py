'''
Lab8 NoSQL MongoDB Aggregation Pipelines, Validaton, Sanitizing
'''
import json
from pymongo import MongoClient, errors

from dbtools import mongodb_connect, mongodb_validation, sanitize_match
from seed_webshop import seed_data

db = mongodb_connect()
# db = mongodb_connect(seed=seed_data)

#Ex1
'''
I would make a reviews collection that references the book and member.
Embedding in either of those would be a ever growing list.
'''

#Ex2
'''
Adv: You have all the data needed for receipts, reports in one place.
DisAdv: You are writing more to the database on order creation.
So having to look up once on order creation vs. every time you need the receipt/report.
'''

#Ex3
vexpr_newsletter = { "$jsonSchema": {
    "bsonType": "object",
    "required": ["email", "source"],
    "properties": {
        "email": {
            "bsonType": "string",
            "description": "must be a string and is required"
        },
        "source": {
            "bsonType": "string",
            "enum": ["web", "store"],
            "description": "must be a string and in valid values"
        }
}}}

mongodb_validation(db,[('newsletter_signups',vexpr_newsletter)])

#Ex4
def city_members() -> None:
    pipe = [{'$group' : {'_id': '$city', 'count': {'$sum': 1} }},
            {'$sort': {'count': -1}}]
    result = db.customers.aggregate(pipe)
    print(  *[f'Rank{i}, {f'{doc.get('_id') if doc.get('_id') else 'unknown'}':<10} {doc.get('count')} members.' 
            for i,doc in enumerate(result,1)],sep='\n')

# city_members()

#Ex5 hey, it works
def products_minmax_price_items() -> None:
    pipe = [{'$group': {'_id': '$category', 'min_price': {'$min': '$price'}, 'max_price': {'$max': '$price'},}},
            {'$lookup': {'from': 'products', 'localField': 'min_price', 'foreignField': 'price', 'as': 'min_product'}},
            {'$lookup': {'from': 'products', 'localField': 'max_price', 'foreignField': 'price', 'as': 'max_product'}}]
    result = db.products.aggregate(pipe)
    print(*[f'Category: {doc.get('_id'):<12} Low Price: {doc.get('min_product')[0].get('name'):<15} {doc.get('min_price'):>5} kr '
            f'High Price: {doc.get('max_product')[0].get('name'):<15} {doc.get('max_price'):>5} kr' 
            for doc in result],sep='\n')

# products_minmax_price_items()

#Ex6
def customers_orders_over2() -> None:
    pipe = [{'$group': {'_id': '$customer_id', 'count': {'$sum': 1}}},
            {'$match': {'count': {'$gte': 2}}}]
    result = db.orders.aggregate(pipe)
    print(*[f'Customer: {doc.get('_id')} Orders: {doc.get('count')}' for doc in result],sep='\n')

# customers_orders_over2()

#Ex7
def order_id_numitems() -> None:
    pipe = [{'$project': {'items': {'$size': '$items'}}}]
    result = db.orders.aggregate(pipe)
    print(*[doc for doc in result],sep='\n')

# order_id_numitems()

#Ex8

def sold_by_category() -> None:
    pipe = [{'$match': {'status': {'$ne': 'cancelled'}}},
            {'$unwind': '$items'},
            {'$lookup': {'from': 'products', 'localField': 'items.product_id', 'foreignField': '_id', 'as': 'product'}},
            {'$unwind': '$product'},
            {'$group': {'_id': '$product.category', 'count': {'$sum': '$items.quantity'}}}]
    result = db.orders.aggregate(pipe)
    print(*[doc for doc in result],sep='\n')

# sold_by_category()

#Ex9
def revenue_per_status() -> None:
    pipe = [{'$unwind': '$items'},
            {'$project': {'status': '$status', 'total': {'$multiply': ['$items.quantity','$items.unit_price']}}},
            {'$group': {'_id': '$status', 'revenue': {'$sum': '$total'}}}]
    result = db.orders.aggregate(pipe)
    print(*[doc for doc in result],sep='\n')

# revenue_per_status()

#Ex10
def most_common_tags() -> None:
    pipe = [{"$unwind": "$tags"},
            {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}]
    result = db.products.aggregate(pipe)
    print(*[doc for doc in result],sep='\n')

# most_common_tags()

#Ex11
def find_orders(request_text) -> list:
    # data = json.loads(request_text)
    return list(db.orders.find({'status': {'$eq': sanitize_match(data['status'])}}))

# print(*find_orders(1),sep='\n')


#Ex12
def products_under(text) -> list:
    try: val = float(text)
    except ValueError: 
        print('Please enter a number.')
        return []
    pipe = [{'$match': {'price': {'$lt': val}}},
            {'$sort': {'price': 1}}]
    return db.products.aggregate(pipe)

# print(*products_under(input('Enter price upper threshold: ')),sep='\n')

#Ex13
bad_db = MongoClient("mongodb://localhost:27020/", serverSelectionTimeoutMS=2000)
def timeout_request() -> list:
    pipe = [{'$project': {'product': '$name'}},
            {'$sort': {'product': 1}}]
    try: result = bad_db.products.aggregate(pipe)
    except errors.ServerSelectionTimeoutError: 
        print('server timeout')
        result = []
    return result

print(*timeout_request(),sep='\n')

#Ex14
'''
Personal data fields in customers: All fields.
You still need to save all the order data for accounting, receipts.
So having a anonomized id lets you delete all the actual customer data while
the order records are 'intact'.
While faster reads it creates the beforementioned problem with having data
that might have to be deleted and or changed in many places.
'''