'''
Lab-Extra Library impl MongoDB NoSQL
'''

import pymongo

from dbtools import mongodb_connect, mongodb_seed
from seed_library import books, members, borrowings, reviews
from library import library_menu

seed_data = [('books',books),('members',members),('borrowings',borrowings),('reviews',reviews)]
seed_on_run = True

def main():
    db = mongodb_connect(name='library',seed=seed_data if seed_on_run else None)

    while True:
        library_menu(db)

if __name__ == '__main__':
    main()