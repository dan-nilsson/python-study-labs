'''
Lab2 FastAPI Client - 261020
'''

from apitools import get_req_json

endpoint = 'http://127.0.0.1:8000'

books = get_req_json(f'{endpoint}/books')

print(*[b for b in books],sep='\n')