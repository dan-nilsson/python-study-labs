'''
Database helpers and tools library
'''

from pymongo    import MongoClient
import os, json, sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
cfg_path = os.path.join(base_dir, 'config.json')

with open(cfg_path, 'r') as file:
    cfg = json.load(file)

def sqlite_connect(cfg=cfg,fk=True) -> Connection:
    db_path = os.path.join(base_dir, cfg['sqlite'].get('name'))
    conn = sqlite3.connect(db_path)
    if fk: conn.execute('PRAGMA foreign_keys = ON')
    return conn

def mongodb_connect(name=cfg['mongodb'].get('name'),seed=False) -> MongoClient:
    cfg_mongodb = cfg['mongodb']
    client = MongoClient(f'mongodb://{cfg_mongodb.get('host')}:{cfg_mongodb.get('port')}')
    db = client[name]
    if seed: mongodb_seed(db)
    return db

def mongodb_seed(db,data):
    for col_name,_ in data:
        db[col_name].drop()
    for col_name,col_data in data:
        db[col_name].insert_many(col_data)
    print(f'database is ready')
    for col_name,_ in data:
        print(db[col_name].count_documents({}), col_name)

def sanitize_input(*args) -> tuple:
    return (*args,)