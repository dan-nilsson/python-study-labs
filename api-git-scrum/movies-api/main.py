'''
Lab2 FastAPI Server - 261020
'''
#Part 1
#Ex1 - 1
from fastapi import FastAPI, HTTPException
from pydantic import *

from apitools import json_load, json_dump

app = FastAPI()

class Movie(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float

@app.get('/')
def home():
    return {'message': 'Welcome'}

@app.get('/movies')
def get_movies():
    return movies

#Ex2
@app.get('/movies/{movie_id}')
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.post('/movies', status_code=201)
def create_movie(movie: Movie):
    new_id = max(max([m['id'] for m in movies], default=0)) + 1
    new_movie = {   'id': new_id, 'title': movie.title,  'author': movie.author,
                    'year': movie.year, 'runtime': movie.runtime}
    movies.append(movie)
    return new_movie

@app.put('/movies/{movie_id}')
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing.update({   'title': movie.title, 'director': movie.author,
                        'year': movie.year, 'runtime': movie.runtime})
    return existing

@app.delete('/movies/{movie_id}')
def remove_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)

def find_movie(movie_id: int): 
    for movie in movies:
        if movie['id'] == movie_id: return movie
    raise HTTPException(status_code=404, detail={'msg': 'Movie not found'})

movies = [
    {'id': 1, 'title': 'Heat', 'director': 'Michael Mann', 'year': 1995, 'runtime': 170, 'genre': 'Heist', 'rating': 8.3},
    {'id': 2, 'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972, 'runtime': 175, 'genre': 'Drama', 'rating': 9.2},
    {'id': 3, 'title': 'Leon : The Professional', 'director': 'Luc Besson', 'year': 1994, 'runtime': 110, 'genre': 'Drama',  'rating': 8.5},
    {'id': 4, 'title': 'Das Boot', 'director': 'Wolfgang Pettersen', 'year': 1981, 'runtime': 210,  'genre': 'War',  'rating': 8.3},
    {'id': 5, 'title': 'Reservoir Dogs', 'director': 'Quintin Tarantino', 'year': 1992, 'runtime': 99,  'genre': 'Thriller',  'rating': 8.2},
    {'id': 6, 'title': 'Full Metal Jacket', 'director': 'Stanley Kubrick', 'year': 1987, 'runtime': 116,  'genre': 'War',  'rating': 8.2},
    {'id': 7, 'title': 'Snatch', 'director': 'Guy Ritchie', 'year': 2000, 'runtime': 104, 'genre': 'Comedy', 'rating': 8.2},
    {'id': 8, 'title': 'Die Hard with a Vengeance', 'director': 'John McTiernan', 'year': 1995, 'runtime': 131, 'genre': 'Action',  'rating': 7.6},
]