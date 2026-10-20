'''
Lab2 FastAPI Client - 261020
'''

from apitools import get_req_json

endpoint = 'http://127.0.0.1:8000'

movies = get_req_json(f'{endpoint}/movies')
one_movie = get_req_json(f'{endpoint}/movies/2')

print(*[m for m in movies],sep='\n')
print(one_movie)