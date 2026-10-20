'''
Lab01 - API CRUM REST - 261019
'''
from datetime import datetime, timedelta

from apitools import(   get_req_json, post_req_json, dummy_product, git_headers, get_req_full,
                        json_load, json_dump)

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

def weather_from_coords(lat,long) -> dict:
    response = get_req_json(weather_open_meteo_endpoint,
                            params={'latitude': lat,'longitude': long, 'timezone': 'Europe/Stockholm',
                            'current': ['temperature_2m','wind_speed_10m']})
    return response.get('current')

# print(weather_from_coords(10,10))

#Ex2 - 3

def get_weather_city_name(name=None) -> None:
    if not name: name = input('Enter a city name: ').lower().title()
    try: city_data = find_city(name)
    except TypeError:
        print('City name not found.')
        return
    lat, long = city_data.get('latitude'),city_data.get('longitude')
    country, city_name = city_data.get('country'),city_data.get('name')
    current = weather_from_coords(lat,long)
    temp, wind = current.get('temperature_2m'),current.get('wind_speed_10m')
    city_data.update(current)
    json_dump(city_data)
    print(  f'Weather Report -\n{country}, {city_name}',
            f'temp: {temp}°C, wind: {wind} km/h')

# get_weather_city_name()

#Ex2 - 4
#done

#Ex3 - 1-2
#done

#Ex3 - 3-4

git_endpoint = 'https://api.github.com/users/'
suffix = '/repos'

def get_git_info() -> None:
    user = input('Enter a username: ').lower()
    response = get_req_json(git_endpoint+user+suffix,headers=git_headers)
    print(*[repo.get('name') for repo in response],sep='\n')
    full_response = get_req_full(git_endpoint+'dan-nilsson'+suffix, headers=git_headers)
    print(full_response.headers.get('X-RateLimit-Limit'),full_response.headers.get('X-RateLimit-Remaining'))

# get_git_info()

#Ex3 - 5
# It gives error 401.
# Error: 401. Unauthorized.     = User Unknown
# Error: 403. Forbidden.        = User Known and not Allowed access.

#Ex3 - 5-6
# done 

#Ex4 - 1-3

def check_cache_cityname(name) -> dict:
    file = json_load()
    if file.get('name') == name.lower().title(): return file
    return None

def check_time_delta_10(time) -> bool:
    file_time = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    return file_time + timedelta(minutes=10) > datetime.now()

def cached_weather(name) -> None:
    file_city, time = None, datetime(2000,1,1)
    try:
        file_city = check_cache_cityname(name)
        time = file_city.get('time')
    except TypeError: pass
    if file_city and check_time_delta_10(time):
        print('Local file data.')
        country, city_name = file_city.get('country'),file_city.get('name')
        temp, wind = file_city.get('temperature_2m'), file_city.get('wind_speed_10m')
        print(  f'Weather Report -\n{country}, {city_name}',
                f'temp: {temp}°C, wind: {wind} km/h')
        return
    print('API data.')
    get_weather_city_name(name)
    
cached_weather(input('Enter a city name: '))

'''
Caching API fetch data to local file and using it when resonably fresh cuts
down on API usage and is faster.
'''
