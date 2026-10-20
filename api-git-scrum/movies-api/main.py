'''
Lab2 FastAPI Server - 261020
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from apitools import json_load, json_dump

app = FastAPI()

class Movie(BaseModel):
    title: str
    director: str
    year: int
    runtime: int
    genre: str
    rating: float

class MovieUpdate(BaseModel):
    title: str      | None = None      
    director: str   | None = None
    year: int       | None = None
    runtime: int    | None = None
    genre: str      | None = None
    rating: float   | None = None

#changes.model_dump(exclude_unset=True)

@app.get('/')
def home():
    return {'message': 'Welcome'}

@app.get('/movies')
def get_movies(director: str | None = None, year: int | None = None) -> list:
    with_params = []
    if director != None or year != None:
        for movie in movies:
            if movie.get('director') == director.lower().title() if director else '' or movie.get('year') == year:
                with_params.append(movie)
        if with_params: return with_params
        else: raise HTTPException(status_code=404, detail='No result')
    return movies

@app.get('/movies/{movie_id}')
def get_movie(movie_id: int) -> Movie:
    return find_movie(movie_id)

@app.post('/movies', status_code=201)
def create_movie(movie: Movie) -> Movie:
    new_id = max([m.get('id') for m in movies],default=1) + 1
    print(new_id)
    new_movie = {   'id': new_id, 'title': movie.title,  'director': movie.director, 'year': movie.year,
                    'runtime': movie.runtime, 'genre': movie.genre, 'rating': movie.rating}
    movies.append(movie)
    return new_movie

@app.put('/movies/{movie_id}')
def replace_movie(movie_id: int, movie: Movie) -> Movie:
    existing = find_movie(movie_id)
    existing.update({   'title': movie.title, 'director': movie.director, 'year': movie.year,
                        'runtime': movie.runtime, 'genre': movie.genre, 'rating': movie.rating})
    return existing

@app.delete('/movies/{movie_id}')
def remove_movie(movie_id: int) -> None:
    existing = find_movie(movie_id)
    movies.remove(existing)

@app.patch('/movies/{movie_id}')
def update_movie(movie_id: int, movie: MovieUpdate) -> Movie:
    existing = find_movie(movie_id)
    #existing.update(changes.model_dump(exclude_unset=True))
    return existing

def find_movie(movie_id: int):
    for movie in movies:
        if movie.get('id') == movie_id: return movie
    raise HTTPException(status_code=404, detail='Movie not found')

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