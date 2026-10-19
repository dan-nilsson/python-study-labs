'''
Lab01 - API CRUM REST - 261019
'''
from apitools import get_req_json, post_req_json, dummy_product

endpoint = 'https://fakestoreapi.com/products'

def print_products(data) -> None:
    print(*[f'{i:<2}. {prod.get('title'):<80} ${prod.get('price'):>6}' 
            for i,prod in enumerate(data,1)],
            sep='\n')

#Ex1 - 1
def get_products_sorted() -> None:    
    data = get_req_json(endpoint)
    sort_data = sorted(data,key=lambda x: x.get('price'))
    print_products(sort_data)

# get_products_sorted()

#Ex1 - 2
def get_categories() -> None:
    categories = get_req_json(endpoint+'/categories')
    print(f'Categories: {', '.join([cat.title() for cat in categories])}')
    data = get_req_json(endpoint)
    sort_data = sorted(data,key=lambda x: x.get('price'))
    user_input = input('Enter a category: ').lower()
    print_products([prod for prod in sort_data if prod.get('category') == user_input])

# get_categories()

#Ex1 - 3
#Already done

#Ex1 - 4
def post_product(data) -> None:
    response = post_req_json(endpoint,data)
    print(response, response.status_code, response.json())

# post_product(dummy_product)

#Ex1 - 5
def bad_req() -> None:
    return get_req_json('https://not-a-domain-frfr-og.com/notproducts',timeout=0.001)

# bad_req()

#Ex2


#Ex3


#Ex4