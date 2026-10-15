'''
Lab-Extra Library impl MongoDB NoSQL
'''

import pymongo
from dbtools import mongodb_connect, mongodb_seed

from seed_library import books

seed_data = [('books',books)]

def main():
    db = mongodb_connect(name='library')
    mongodb_seed(db,seed_data)

if __name__ == '__main__':
    main()