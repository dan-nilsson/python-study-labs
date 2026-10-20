'''
Lab2 FastAPI Client - 261020
'''

from apitools import get_req_json, post_req_json, get_req_full, API_KEY

endpoint = 'http://127.0.0.1:8000'

movies = get_req_json(f'{endpoint}/movies')
one_movie = get_req_json(f'{endpoint}/movies/3')
bad_movie = get_req_json(f'{endpoint}/movies/20')

print(*[m for m in movies],sep='\n')
print(one_movie)
print(bad_movie)

top_gun: dict = {
  "title": "Top Gun",
  "director": "Tony Scott",
  "year": 1986,
  "runtime": 109,
  "genre": "Action",
  "rating": 7.0
}
post_headers = {"X-API-Key": API_KEY}

add_movie = post_req_json(f'{endpoint}/movies',top_gun,headers=post_headers)
print(add_movie)

'''
You would use PUT when replacing and PATCH when updating less than all fields.
'''