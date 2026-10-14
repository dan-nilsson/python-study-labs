'''
Database helpers and tools library
'''

from pymongo    import MongoClient
import os, json, sqlite3

from seed_webshop   import customers,products,orders

base_dir = os.path.dirname(os.path.abspath(__file__))
cfg_path = os.path.join(base_dir, 'config.json')

with open(cfg_path, 'r') as file:
    cfg = json.load(file)

def sqlite_connect(cfg=cfg,fk=True) -> Connection:
    db_path = os.path.join(base_dir, cfg['sqlite'].get('name'))
    conn = sqlite3.connect(db_path)
    if fk: conn.execute('PRAGMA foreign_keys = ON')
    return conn

def mongodb_connect(cfg=cfg,seed=False) -> MongoClient:
    cfg_mongodb = cfg['mongodb']
    client = MongoClient(f'mongodb://{cfg_mongodb.get('host')}:{cfg_mongodb.get('port')}')
    db = client[cfg_mongodb.get('name')]
    if seed: mongodb_seed(db)
    return db

def mongodb_seed(db):
    collections = ['customers','products','orders']
    for c in collections:
        db[c].drop()

    db.customers.insert_many(customers)
    db.products.insert_many(products)
    db.orders.insert_many(orders)

    print('webshop is ready:',
          db.customers.count_documents({}), 'customers,',
          db.products.count_documents({}), 'products,',
          db.orders.count_documents({}), 'orders')

def sanitize_input(*args) -> tuple:
    return (*args,)