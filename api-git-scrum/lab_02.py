'''
Lab2 FastAPI Server - 261020
'''

from fastapi import FastAPI, HTTPException
from pydantic import *

from apitools import json_load, json_dump

app = FastAPI()

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

class Book(BaseModel):
    title: str
    author: str
    year: int

@app.get('/')
def home():
    return {'message': 'Welcome'}

@app.get('/books')
def get_books():
    return books

@app.get('/books/{book_id}')
def get_books(book_id: int):
    return find_book(book_id)

@app.post('/books', status_code=201)
def create_book(book: Book):
    new_id = max(max([b['id'] for b in books], default=0)) + 1
    new_book = {'id': new_id, 'title': book.title,  'author': book.author, 'year': book.year}
    books.append(book)
    return new_book

@app.put('/books/{book_id}')
def replace_book(book_id: int, book: Book):
    existing = find_book(book_id)
    existing.update({'title': book.title, 'author': book.author, 'year': book.year})
    return existing

@app.delete('/books/{book_id}')
def remove_book(book_id: int):
    existing = find_book(book_id)
    books.remove(existing)

def find_book(book_id: int): 
    for book in books:
        if book in books:
            if book['id'] == book_id: return book
    raise HTTPException(status_code=404, detail={'msg': 'Book not found'})