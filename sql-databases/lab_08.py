'''
Lab8 NoSQL MongoDB Aggregation Pipelines, Validaton, Sanitizing
'''
from dbtools import mongodb_connect, mongodb_validation
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

#Ex5
def products_minmax_price_items() -> None:
    pipe = [{'$group': {'_id': '$category', 'min_price': {'$min': '$price'}, 'max_price': {'$max': '$price'}}}]
    result = db.products.aggregate(pipe)
    print(*[doc for doc in result])

products_minmax_price_items()
#just prices for now. will get names

#Ex6


#Ex7


#Ex8


#Ex9


#Ex10


#Ex11


#Ex12


#Ex13


#Ex14