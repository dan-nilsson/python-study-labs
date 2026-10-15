'''
Lab-Extra Library impl MongoDB NoSQL
'''

import pymongo
from dbtools import mongodb_connect, mongodb_seed

def main():
    db = mongodb_connect(name='library')

if __name__ == '__main__':
    main()