import requests
from pprint import pprint

# 1. Informacije o svemirskoj stanici
# Napisati funkciju get_space_station() -> dict koja preko Open Notify API-ja (http://api.open-notify.org/iss-now.json) preuzima trenutnu poziciju Međunarodne svemirske stanice (ISS) i vraća rečnik koji sadrži:
# geografsku širinu (latitude),
# geografsku dužinu (longitude)

def get_space_station() -> dict:

    response = requests.get('http://api.open-notify.org/iss-now.json').json()

    return response['iss_position']

# 2. Pretraga univerziteta
# Napisati funkciju get_universities(country: str) -> list koja preko Hipolabs API-ja (http://universities.hipolabs.com/search) preuzima univerzitete iz zadate države i vraća listu njihovih naziva.
# Koristiti params={'country': country} za prosleđivanje naziva države API-ju.

def get_universities(country: str) -> list:

    params = {
        'country': country
    }

    response = requests.get('http://universities.hipolabs.com/search', params= params).json()

    result = []

    for i in response:
        result.append(i['name'])

    return result

# 3. Informacije o kursu valuta
# Napisati funkciju get_exchange_rate(base: str, target: str) -> float koja preko Frankfurter API-ja (https://api.frankfurter.dev/v1/latest ; ovde nema RSD a ovde ima https://api.frankfurter.dev/v2/rates) preuzima kurs između dve valute.
# Funkcija treba da vrati koliko jedinica ciljne valute (target) se dobija za jednu jedinicu početne valute (base).
# Input: get_exchange_rate("EUR", "RSD")
# Output: 117.2

# Ovo je uradjeno preko linka: https://api.frankfurter.dev/v2/rates Ali kod ovog linka ne moze preko parameters zato sto je drugaciji API V2. 
# U ovom API-ju ima RSD
def get_exchange_rate(base: str, target: str) -> float:

    url = f'https://api.frankfurter.dev/v2/rate/{base}/{target}'

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return float(data['rate'])

get_exchange_rate('RSD', 'EUR')

#--------------------------------------------------------------------
# Ovo je uradjen zadatak preko oginalnog link-a i API-ja V1. Ali ovaj API nema RSD i jos neke druge valute.
def get_exchange_rate(base: str, target: str):

    params = {
        'base': base,
        'quote': target
    }

    response = requests.get('https://api.frankfurter.dev/v1/latest', params= params)
    response.raise_for_status()

    data = response.json()['rates']
    exchange_rate = 0.0
    for key, value in data.items():
        if key == target:
            exchange_rate = float(value)
            break
    
    if exchange_rate == 0.0:
        print('Wanted currency is not available on exchange office')
    else:
        return exchange_rate
            

get_exchange_rate('EUR', 'GBP')
