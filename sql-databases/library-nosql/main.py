'''
Lab-Extra Library impl MongoDB NoSQL
'''

import pymongo
from dbtools import mongodb_connect, mongodb_seed

from seed_library import books
from library import library_menu

seed_data = [('books',books)]

def main():
    db = mongodb_connect(name='library')
    mongodb_seed(db,seed_data)

    while True:
        library_menu(db)

if __name__ == '__main__':
    main()