import requests
import pandas as pd
from pprint import pprint

# 1. Написати функцију get_user(user_id: int) -> dict која са JSONPlaceholder-а
# (https://jsonplaceholder.typicode.com/users/<user_id>) преузима корисника и враћа само
# име, email и град.
# Input: get_user(1)
# Output: {'name': 'Leanne Graham', 'email': 'Sincere@april.biz', 'city':
# 'Gwenborough'}
# Помоћ: град је унутар address

def get_user(user_id: int) -> dict:
    base_url = 'https://jsonplaceholder.typicode.com/users/'

    response = requests.get(base_url, params= {'id': user_id}).json()

    data = response[0]
    result = {'name': data['name'], 'email': data['email'], 'city': data['address']['city']}

    return result

get_user(1)

########################################################################################################
# Profino resenje
# 'https://jsonplaceholder.typicode.com/users/<user_id>'    # ovo i ovo ispod je sve jedan te isti zapis
# 'https://jsonplaceholder.typicode.com/users/:user_id'
# 'https://jsonplaceholder.typicode.com/users/{user_id}'

def get_user2(user_id: int) -> dict:
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    response.raise_for_status() # ovo se pise umesto if petlje za proveru statusa

    user = response.json()
    return {
        'name': user['name'],
        'email': user['email'],
        'city': user['address']['city']
    }

get_user2(1)

# 2. Написати функцију get_post_titles(user_id: int) -> list која враћа листу наслова свих постова једног корисника. Користити params={'userId': user_id}, а не филтрирање у Python-у.
# Input: get_post_titles(1)
# Output: листа од 10 наслова, први је 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'

# def get_post_titles(user_id: int) -> list:
#     base_url = 'https://jsonplaceholder.typicode.com/users/'
    
#     response = requests.get(base_url, params= {'userId': user_id}).json()

#     return response

# get_post_titles(1)

########################################################################################################
# Profino resenje

def get_post_titles(user_id: int) -> list:
    r = requests.get(f'https://jsonplaceholder.typicode.com/posts', params={'userId': user_id})
    r.raise_for_status()

    return [post['title'] for post in r. json()]

get_post_titles(1)

# 3. Написати функцију get_current_temperature(latitude: float, longitude: float) -> float која преко Open-Meteo API-ја (https://api.open-meteo.com/v1/forecast, параметар current='temperature_2m') враћа тренутну температуру.
# Input: get_current_temperature(45.25, 19.84)
# Output: број (зависи од тренутне температуре)
# Помоћ: прво испишите цео одговор и пронађите где је температура

# Profino resenje
def get_current_temperature(latitude: float, longitude: float) -> float:
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m'
    }

    r = requests.get('https://api.open-meteo.com/v1/forecast', params= params)
    r.raise_for_status()

    return r.json()['current']['temperature_2m']

get_current_temperature(45.25, 19.84)

# 4. Написати функцију city_coordinates(city: str) -> tuple која преко Open-Meteo geocoding API-ја (https://geocoding-api.open-meteo.com/v1/search) враћа (latitude, longitude) првог резултата у Србији (countryCode='RS'). Ако град не постоји, подићи ValueError.
# Input1: city_coordinates('Novi Sad')
# Output1: око (45.25, 19.84)
# Input2: city_coordinates('Xyzzyville')
# Output2: ValueError: City not found: Xyzzyville

# Profino resenje
def city_coordinates(city: str) -> tuple:
    params = {
        'name': city,
        'count': 1,
        'countryCode': 'RS'
    }

    r = requests.get('https://geocoding-api.open-meteo.com/v1/search', params= params)
    r.raise_for_status()

    data = r.json()

    if 'results' not in data:
        raise ValueError(f'City not found: {city}')

    return data['results'][0]['latitude'], data['results'][0]['longitude']

city_coordinates('Novi Sad')
# city_coordinates('Xyzzyville')

# 5. *Написати функцију warmest_city(cities: list, days: int) -> tuple која за сваки град из листе узима координате (задатак 4) и дневну прогнозу temperature_2m_max за наредних days дана. Враћа град са највишим просеком максималних температура и тај просек, заокружен на једну децималу.
# Град који не постоји се прескаче уз испис Skipping <град>
# Ако ниједан град не постоји, подићи ValueError
# Input: warmest_city(['Novi Sad', 'Niš', 'Subotica', 'Xyzzyville'], 3)
# Output: исписано Skipping Xyzzyville, затим нпр. ('Niš', 9.7) (зависи од прогнозе)

def warmest_city(cities: list, days: int) -> tuple:

    result = []
    for i in cities:
        try:
            coords = city_coordinates(i)
        except ValueError:
            print(f'Skipping {i}')
            continue

        params = {
            'latitude': coords[0],
            'longitude': coords[1],
            'daily': 'temperature_2m_max',
            'forecast_days': days
        }

        r = requests.get('https://api.open-meteo.com/v1/forecast', params= params)
        
        max_temp_list = r.json()['daily']['temperature_2m_max']
        sum = 0.0
        for b in max_temp_list:
            sum += float(b)
        prosek = round(float(sum / len(max_temp_list)), 1)
        
        result.append((i, prosek))
    
    if len(result) == 0:
        raise ValueError('Not valid cities')
    else:
        grad = max(result, key=lambda i: i[1])[0]
        temp = max(result, key=lambda i: i[1])[1]
        return grad, temp

spisak_gradova = ['Niš','Beograd', 'Novi Sad', 'Xyzzyville']
warmest_city(spisak_gradova, 2)
