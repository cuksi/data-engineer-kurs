import requests     # biblioteka za rad sa API-jem

# 1. define endpoint
url = 'https://bored-api.appbrewery.com/random'

# 2. make a request
response = requests.get(url)

print(response)

# 3. check status_code (check response)
if response.status_code == 200:
    data = response.json()
    print(data)
    print(type(data))
else:
    print(f'Error, status_code: {response.status_code}')

# print(data['activity'])   # ovo bolje da ide u if jer ako ima greska tj. ne dobijemo odgovor od api-ija puci ce program

# Status codes
# 2xx   - OK
#   201 - Created on server, when we send something
# 3xx   - Redirect
# 4xx   - BadRequest
#   400 - BadRequest
#   401 - Unauthorized
#   403 - Forbidden (ako si ulogovan a nemas pristup)
#   404 - Not found
# 5xx - Server errors

# pdf - base64 (string representation of pdf)

url = 'https://bored-api.appbrewery.com/filter'

payload = {     # parametri za api kako se upisuju u python-u
    'type': 'education'
}

response = requests.get(url, params = payload)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(type(data))
else:
    print(f'Error, status_code: {response.status_code}')

from pprint import pprint
import pandas as pd

# params = {
#     'latitude': 45.24,
#     'longitude': 19.84,
#     'forecast_days': 2,
#     'hourly': 'temperature_2m',
#     'timezone': 'Europe/Belgrade'
# }

# data = requests.get('https://api.open-meteo.com/v1/forecast', params= params).json()

data = {'latitude': 45.24554, 'longitude': 19.84993, 'generationtime_ms': 0.0457763671875, 'utc_offset_seconds': 3600, 'timezone': 'Europe/Belgrade', 'timezone_abbreviation': 'GMT+1', 'elevation': 81.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'}, 'hourly': {'time': ['2026-11-17T00:00', '2026-11-17T01:00', '2026-11-17T02:00', '2026-11-17T03:00', '2026-11-17T04:00', '2026-11-17T05:00', '2026-11-17T06:00', '2026-11-17T07:00', '2026-11-17T08:00', '2026-11-17T09:00', '2026-11-17T10:00', '2026-11-17T11:00', '2026-11-17T12:00', '2026-11-17T13:00', '2026-11-17T14:00', '2026-11-17T15:00', '2026-11-17T16:00', '2026-11-17T17:00', '2026-11-17T18:00', '2026-11-17T19:00', '2026-11-17T20:00', '2026-11-17T21:00', '2026-11-17T22:00', '2026-11-17T23:00', '2026-11-18T00:00', '2026-11-18T01:00', '2026-11-18T02:00', '2026-11-18T03:00', '2026-11-18T04:00', '2026-11-18T05:00', '2026-11-18T06:00', '2026-11-18T07:00', '2026-11-18T08:00', '2026-11-18T09:00', '2026-11-18T10:00', '2026-11-18T11:00', '2026-11-18T12:00', '2026-11-18T13:00', '2026-11-18T14:00', '2026-11-18T15:00', '2026-11-18T16:00', '2026-11-18T17:00', '2026-11-18T18:00', '2026-11-18T19:00', '2026-11-18T20:00', '2026-11-18T21:00', '2026-11-18T22:00', '2026-11-18T23:00'], 'temperature_2m': [7.0, 6.8, 6.5, 6.0, 5.3, 4.4, 4.8, 5.7, 7.2, 11.1, 14.4, 15.8, 16.2, 16.5, 16.8, 16.4, 16.2, 16.2, 16.4, 16.0, 15.8, 14.7, 14.0, 13.8, 14.3, 14.8, 13.9, 14.2, 14.1, 14.9, 15.4, 15.2, 14.6, 14.4, 15.9, 18.1, 19.0, 19.8, 19.1, 15.5, 15.5, 14.9, 14.0, 13.8, 13.9, 13.9, 13.9, 13.4]}}

# print(data)
# pprint(data['hourly_units'])

# print(data['hourly'])

hourly = pd.DataFrame(data['hourly'])
# pprint(hourly)

url = 'https://geocoding-api.open-meteo.com/v1/search'

data = requests.get(url, params= {'name': 'Novi Sad', 'countryCode': 'RS', 'count': 1}).json()      # count je opciono ako ima vise gradova sa istim imenom

print(data['results'][0])

base_url = 'https://jsonplaceholder.typicode.com'   # ovo je pocetni url na koji nadogradjujemo

users = requests.get(f'{base_url}/users').json()     # ovo je neka praksa kako se pise
# user = requests.get(f'{base_url}/posts').json()

print(users)

users_df =pd.DataFrame(users)
print(users_df[['name', 'address']])

print(users[0]['address'])

# for user in users:        # ovo je prost nacin, nije lepo napisana petlja samo primer
#     address_string = ''
#     for k,v in user['address'].items():
#         address_string += v + '_'
#     print(address_string)

# Flattens, ovo je bolji nacin nego for petlja
users_df = pd.json_normalize(users, sep='_')    # ako ima jos neki recnik unutar originalnog, on to stavlja sve u jedan, ovo sep= '_' odredjuje kako ce biti naziv tih novih kolona
display(users_df)

users_df.columns    # ovo je da dobijemo kljuceve

base_url = 'https://jsonplaceholder.typicode.com'

response = requests.post(f'{base_url}/posts', json={'title': 'Naslov', 'body': 'Neki test', 'userId': 5})   # redosled nije bitan unutar json-a

print(response.status_code)
print(response.json())

import json

json.dumps({'title': 'Naslov', 'id': 52})   # pretvara u json

x = json.loads('{"team": "MNJ"}')

type(x)
