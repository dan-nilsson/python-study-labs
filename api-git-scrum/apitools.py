'''
API helper functions
'''
import requests, os
from dotenv import load_dotenv

load_dotenv()
git_token = os.getenv("GITHUB_TOKEN")
git_headers = {"Authorization": f'Bearer: {token}'}

def get_req_json(endpoint,params=None,headers=None,timeout=1):
    try:
        respose = requests.get(endpoint, params=params, headers=headers, timeout=timeout)
        respose.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.JSONDecodeError:
        print('The returned data was not JSON format.')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None

def post_req_json(endpoint,data,params=None,headers=None,timeout=1) -> None:
    try:
        response = requests.post(endpoint, data, params=params, headers=headers, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None


def put_req_json(endpoint, index, data, params=None, headers=None, timeout=1) -> None:
    try:
        response = requests.put(f'{endpoint}/{index}', json=data, params=params, headers=headers, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.InvalidURL:
        print('The index is invalid.')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None

def patch_req_json(endpoint, index, data, params=None, headers=None, timeout=1) -> None:
    try:
        response = requests.patch(f'{endpoint}/{index}', json=data, params=params, headers=headers, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.InvalidURL:
        print('The index is invalid.')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None

def delete_req(endpoint, index, params=None, headers=None, timeout=1) -> None:
    try:
        response = requests.delete(f'{endpoint}/{index}', params=params, headers=headers, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.InvalidURL:
        print('The index is invalid.')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None

def options_req(endpoint, params=None, headers=None, timeout=1) -> None:
    try:
        response = requests.options(endpoint, params=params, headers=headers, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        print('The request timed out.',response.url)
    except requests.exceptions.ConnectionError:
        print('Could not connect to the server.')
    except requests.exceptions.HTTPError as error:
        print(f'The server gave an error: {error.response.status_code}')
    except requests.exceptions.InvalidURL:
        print('The index is invalid.')
    except requests.exceptions.RequestException as error:
        print(f'Something else went wrong: {type(error).__name__}')
    return None