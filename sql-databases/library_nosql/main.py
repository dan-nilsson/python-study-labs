'''
Lab-Extra Library impl MongoDB NoSQL
'''

import pymongo
from dbtools import mongodb_connect, mongodb_seed

def main():
    db = mongodb_connect(name='library')

if __name__ == '__main__':
    main()

'''
Database Schema

members: name, email (unique), join_date
books: title, author, year, genre, num_copies
reviews: member_id, rating
borrowings: member, book, borrow_date, return_date

'''