'''
Lab01 - API CRUM REST - 261019
'''
from apitools import get_req_json, post_req_json, dummy_product, git_headers, get_req_full

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

#Ex2 - 1
geo_open_meteo_endpoint = 'https://geocoding-api.open-meteo.com/v1/search'
weather_open_meteo_endpoint = 'https://api.open-meteo.com/v1/forecast'

def find_city(name) -> dict:
    response = get_req_json(geo_open_meteo_endpoint,params={'name': name, 'count': 1})
    city_data = response.get('results')[0]
    return city_data

# print(city_coords('Stockholm'))

#Ex2 - 2

def weather_from_coords(lat,long) -> tuple:
    response = get_req_json(weather_open_meteo_endpoint,
                            params={'latitude': lat,'longitude': long,
                            'current': ['temperature_2m','wind_speed_10m']})
    weather = response.get('current')
    return (weather.get('temperature_2m'),weather.get('wind_speed_10m'))

# print(weather_from_coords('Stockholm'))

#Ex2 - 3

def get_weather_city_name() -> None:
    name = input('Enter a city name: ').lower().title()
    try: city_data = find_city(name)
    except TypeError:
        print('City name not found.')
        return
    lat, long = city_data.get('latitude'),city_data.get('longitude')
    country, city_name = city_data.get('country'),city_data.get('name')
    temp, wind = weather_from_coords(lat,long)
    print(  f'Weather Report -\n{country}, {city_name}',
            f'temp: {temp}°C, wind: {wind} km/h'  )

# get_weather_city_name()

#Ex2 - 4
#done

#Ex3 - 1-2
#done

#Ex3 - 3-4

git_endpoint = 'https://api.github.com/users/'
suffix = '/repos'

def get_git_info() -> None:
    user = input('Enter a username: ')
    response = get_req_json(git_endpoint+user+suffix,headers=git_headers)
    print(*[repo.get('name') for repo in response],sep='\n')
    full_response = get_req_full(git_endpoint+'dan-nilsson'+suffix, headers=git_headers)
    print(full_response.headers.get('X-RateLimit-Limit'),full_response.headers.get('X-RateLimit-Remaining'))

get_git_info()

#Ex3 - 5
# It gives error 401.
# Error: 401. Unauthorized.     = User Unknown
# Error: 403. Forbidden.        = User Known and not Allowed access.

#Ex3 - 5-6
# done 

#Ex4