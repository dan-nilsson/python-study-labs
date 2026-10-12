'''
Lab05 sql python gdpr 261012
'''

import sqlite3
import os.path #database read wouldn't work without path

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'webshop.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('SELECT first_name,last_name,city FROM customers')
data = cursor.fetchall()

# print(*[f'{first_name} {last_name} ({city})' for first_name,last_name,city in data],sep='\n')

def sanitize(arg):
    return (arg,)

def ask_max_price():
    cursor.execute( 'SELECT name, price FROM products WHERE price < ? ORDER BY price',
                    sanitize(input('max price: ')))
    print(*[f'{prod:<20} {price:.2f} kr' for prod,price in cursor.fetchall()],sep='\n')

# ask_max_price()

def ask_category():
    category = input('category: ').lower().capitalize()
    cursor.execute( 'SELECT COUNT(*) FROM products WHERE category IN (?)',
                    sanitize(category))
    print(f'{cursor.fetchone()[0]} items in the category : {category}.')

# ask_category()

'''
Using f-strings for queries may allow injection and unintended data access/modification.
Sanitizing user input with ? placeholder is a easy fix for this issue.
'''

conn.close()
