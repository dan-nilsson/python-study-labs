'''
Lab06 MongoDB NoSQL 261013
'''

from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27018/")
db = client["webshop"]
