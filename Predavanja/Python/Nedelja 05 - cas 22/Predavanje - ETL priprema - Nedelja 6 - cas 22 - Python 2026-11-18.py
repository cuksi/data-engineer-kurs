import json
import os
from urllib.parse import urljoin
import pandas as pd
import requests

BASE_URL = 'https://cvijan.github.io/nss-api/v1/'
RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'

# Make sure both data folders exist; exist_ok=True means no error if a folder is already there
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# 1. (5 поена) Позив API-ја. Написати функцију get_json(url: str) -> dict која шаље GET захтев.
# - Подиже грешку ако статус није успешан и враћа одговор као речник ако јесте.
# - get_json(BASE_URL + 'status.json')['service'] враћа 'Northern Star Shop API'
# - get_json(BASE_URL + 'orders/page-99.json') подиже requests.HTTPError

def get_json(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# get_json(BASE_URL + 'status.json')['service']
# get_json(BASE_URL + 'orders/page-99.json')


# Profino resenje
def get_json2(url: str):
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    return response.json()

# get_json2(BASE_URL + 'status.json')['service']
# get_json2(BASE_URL + 'orders/page-99.json')
# 2. (10 поена) Странице. Написати функцију fetch_all(first_url: str) -> list која прати next линкове и враћа записе са свих страна у једној листи
# Помоћ: next је релативна путања ('page-2.json')
# Пуну адресу добијамо са: urljoin(url, page['next']) (пазите када нема следеће стране)
# Input: BASE_URL + 'products/page-1.json' даје 48 производа
# Input: BASE_URL + 'orders/page-1.json' даје 125 поруџбина

def fetch_all(first_url: str) -> list:
    result_list = []

    # ne vazi u drugom slucaju mora drugaciji split
    # url_split = first_url.split('products/')
    # path = url_split[0] + 'products/'
    # page = url_split[1]

    url = first_url
    condition_while = True

    while condition_while:
        result_list.extend(get_json(url)['data'])

        new_page = get_json(url)['next']

        if get_json(url)['next'] is None:
            condition_while = False
        else:
            url = urljoin(url, new_page)

    return result_list

# print(len(fetch_all(BASE_URL + 'products/page-1.json')))
# print(len(fetch_all(BASE_URL + 'orders/page-1.json')))

# Profino resenje
def fetch_all2(first_url: str) -> list:
    records = []
    url = first_url
    while url:
        page = get_json2(url)
        records.extend(page['data'])
        url = urljoin(url, page['next']) if page ['next'] else None # urljoin gleda posle cega nema kosa crta i ono iza zadnje kose crte sklanja i menja ga sa drugim parametrom
    return records
    

# 3. (5 поена) Чување сирових података. Написати функцију save_raw(records: list, path: str) -> None која листу речника уписује у JSON фајл без икаквих измена.
# Ако нешто пође наопако у чишћењу података, сирови подаци остају сачувани онако какви су стигли
# os.path.join(RAW_DIR, 'test.json')
# Представља путању до новог фајла који желимо да буде направљен
# Input: save_raw([{'id': 1, 'city': 'Niš'}], os.path.join(RAW_DIR,'test.json'))
# Output: Нема повратне информације, али у data/raw/test.json пише: "city": "Niš"
# Обрисати све направљене JSON фајлове након пробе! Служили су само за проверу.

def save_raw(records: list, path: str) -> None:

    with open(path, 'w', encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii= False, indent= 2)

# save_raw([{'id': 1, 'city': 'Niš'}], os.path.join(RAW_DIR,'test.json'))


# Profino resenje
def save_raw2(records: list, path: str) -> None:
    with open(path, 'w') as f:
        json.dump(records, f, ensure_ascii= False, indent= 2)   # ensure_ascii je po default-u True i onda gubimo kvacice na nasim slovima


# 4. (5 поена) Extract. Написати функцију extract(raw_dir: str) -> tuple која преузима све потребне податке са API-ја (orders и products) и враћа их као два DataFrame-а
# Функцијом из задатка 2 преузети све поруџбине и све производе
# Функцијом из задатка 3 сачувати их као orders.json и products.json у RAW_DIR
# Угњеждена поља распаковати помоћу pd.json_nnormalize(..., sep='_')
# customer_name преименовати у customer
# customer_city преименовати у city
# Input: extract(RAW_DIR)
# Output: Два DataFrame-a (orders_df, products_df):
# Orders shape (125, 8)
# Products shape (48, 4)
# Поред њих, направљена су и два фајла у data/raw

def extract(raw_dir: str) -> tuple:

    products_df = pd.DataFrame(fetch_all(BASE_URL + 'products/page-1.json'))
    orders_df = pd.json_normalize(fetch_all(BASE_URL + 'orders/page-1.json'), sep='_').rename(columns = {'customer_name': 'customer', 'customer_city':'city'})

    product_path = raw_dir + '/products.json'
    product_list= products_df.values.tolist()   # Pretvara DataFrame u list ali sve redove
    save_raw(product_list, product_path)

    orders_path = raw_dir + '/orders.json'
    order_list= orders_df.values.tolist()   # Pretvara DataFrame u list ali sve redove
    save_raw(order_list, orders_path)

    # Moze i ovako ali se u tekstu trazi da se koristi funkcija iz 3 zadatka
    # product_path = RAW_DIR + '/products.json'
    # products_df.to_json(product_path, orient='records', indent= 2)
    # orders_path = RAW_DIR + '/orders.json'
    # orders_df.to_json(orders_path, orient='records', indent= 2)

    return (orders_df, products_df)

# display(extract(RAW_DIR)[0])
# display(extract(RAW_DIR)[1])		

# Profino resenje
def extract2(raw_dir: str) -> tuple:
    orders = fetch_all2(BASE_URL + 'orders/page-1.json')
    products = fetch_all2(BASE_URL + 'products/page-1.json')

    save_raw2(orders, os.path.join(raw_dir,'orders.json'))
    save_raw2(products, os.path.join(raw_dir,'products.json'))

    orders_df = pd.json_normalize(orders, sep= '_').rename(columns = {'customer_name': 'customer', 'customer_city':'city'})

    return orders_df, pd.DataFrame(products)

def extract_with_out_write(raw_dir: str) -> tuple:
    orders = fetch_all2(BASE_URL + 'orders/page-1.json')
    products = fetch_all2(BASE_URL + 'products/page-1.json')

    orders_df = pd.json_normalize(orders, sep= '_').rename(columns = {'customer_name': 'customer', 'customer_city':'city'})

    return orders_df, pd.DataFrame(products)


# 5. (10 поена) Clean. Написати функцију clean_orders(df: pd.DataFrame) -> pd.DataFrame
# Колонама order_id, customer, city и payment уклонити почетне и крајње размаке
# order_id претворити у велика слова, customer и city у облик title()
# Где град недостаје, уписати 'Unknown'
# Не мењати оригиналан DataFrame
# Помоћ: df[col].str.strip(), .str.upper(), .str.title(), .fillna(...)
# Input (1 ред): {'order_id': 'NSS-0003', 'customer': 'MILICA PETROVIĆ', 'city': ' NIŠ '}
# Output: {'order_id': 'NSS-0003', 'customer': 'Milica Petrović', 'city': 'Niš'}
# У сировим подацима град има 30 различитих записа, после чишћења 9 (8 градова + 'Unknown')

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()

    df_copy['order_id'] = df_copy['order_id'].str.strip()
    df_copy['order_id'] = df_copy['order_id'].str.upper()

    df_copy['customer'] = df_copy['customer'].str.strip()
    df_copy['customer'] = df_copy['customer'].str.title()

    df_copy['city'] = df_copy['city'].str.strip()
    df_copy['city'] = df_copy['city'].str.title()
    df_copy['city'] = df_copy['city'].fillna('Unknown')

    df_copy['payment'] = df_copy['payment'].str.strip()

    return df_copy

# test = pd.DataFrame([{'order_id': ' NsS-0003', 'customer': ' MILICA PETROVIĆ', 'city': None, 'payment': ' card '}])
# clean_orders(test)

# Profino resenje
    def clean_orders2(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in ['order_id', 'customer', 'city', 'payment']:
            df[col] = df[col].str.strip()

        df['order_id'] = df['order_id'].str.upper()
        df['customer'] = df['customer'].str.title()
        df['city'] = df['city'].str.title().fillna('Unknown')

        return df

# 6. (5 поена) Дупликати. Написати функцију remove_duplicates(df: pd.DataFrame) -> tuple
# Враћа торку (unique, duplicates) (Оба DataFrame)
# Поруџбина са истим order_id се задржава само први пут (све остало иде у duplicates)
# Помоћ: df.duplicated(...)
# Тестирањем над очишћеним поруџбинама: 122 јединствене и 3 дупликата

def remove_duplicates(df: pd.DataFrame) -> tuple:

    uslov = df.duplicated(subset= 'order_id', keep= 'first')

    return (df[~uslov], df[uslov])

# unique, duplicates = remove_duplicates(clean_orders(extract(RAW_DIR)[0]))
# print(len(unique))
# print(len(duplicates))

# Profino resenje
def remove_duplicates2(df: pd.DataFrame) -> tuple:
    is_dup = df.duplicated('order_id', keep= 'first')
    return df[~is_dup], df[is_dup]

# 7. (15 поена) Validation. Написати функцију validate_order(row: dict, product_ids: set)-> str која враћа 'OK' за исправан ред, у супротном разлог
# Провере радити редом и вратити први пронађени проблем
# order_id не почиње са NSS- -> 'invalid_order'
# quantity недостаје -> 'missing_quantity'
# quantity није цео број већи од нуле -> 'invalid_quantity'
# unit_price није број већи од нуле -> 'invalid_price'
# product_id не постоји међу производима -> 'unknown_product'
# Помоћ:
# pd.to_numeric(value, errors='coerce') претвара '2' у 2, а 'abc' у NaN
# pd.isna(value) препознаје и None и NaN

def is_positive(text: str) -> bool:
    return pd.to_numeric(text, errors='coerce') > 0

def validate_order(row: dict, product_ids: set)-> str:
    
    if not row['order_id'].startswith('NSS'):
        return 'invalid_order'
    if row['quantity'] == '':
        return 'missing_quantity'
    if not is_positive(row['quantity']):
        return 'invalid_quantity'
    if not is_positive(row['unit_price']):
        return 'invalid_price'
    if row['product_id'] not in product_ids:
        return 'unknown_product'
    
    return 'OK'

# order = {'order_id':' NSS-0001', 'order_date': '2026-11-09', 'product_id': 113, 'quantity': 2, 'unit_price': 6090.0, 'payment': 'paypal', 'customer': 'milan petrović', 'city': 'Beograd'}	
# product = {'product_id' : 101, 'name': 'NPM Home Jersey', 'category': 'jerseys', 'price': 8490}
# mix = {'order_id':'NSS-0001', 'order_date': '2026-11-09', 'product_id': 113, 'name': 'NPM Home Jersey','category': 'jerseys', 'quantity': '2', 'unit_price': 6900.0, 'payment': 'paypal', 'customer': 'milan petrović', 'city': 'Beograd'}
# set_p_id = {101, 113}
# validate_order(mix, set_p_id)

# 8. (10 поена) Transformation. Написати функцију transform_orders(orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame која прима исправне редове.
# Типови:
# quantity -> int
# unit_price -> float
# order_date -> датум (pd.to_datetime)
# Нова колона total (quantity * unit_price)
# Из products додати product_name (колона name) и category (merge по product_id)
# Output: Нпр за NSS-0001: quantity 2, unit_price 6090.0, total 12180.0, product_name 'NPM Kids Jersey', category 'jerseys'

def transform_orders(orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    products = products.rename(columns = {'name': 'product_name'})
    final_df = pd.merge(
        orders,
        products[['product_id', 'product_name', 'category']],
        on= 'product_id',
        how ='left'
        )
    final_df['quantity'] = pd.to_numeric(final_df['quantity'], downcast= 'integer')
    final_df['unit_price'] = pd.to_numeric(final_df['unit_price']).astype(float)
    final_df['order_date'] = pd.to_datetime(final_df['order_date'])
    final_df['total'] = final_df['quantity'] * final_df['unit_price']

    return final_df

# orders_df, products_df  = extract_with_out_write(RAW_DIR)

# # display(products_df)

# orders_clean_df = remove_duplicates(clean_orders(orders_df))[0]

# # display(products_clean_df)

# result = transform_orders(orders_clean_df, products_df)
# display(result)
# result.dtypes


# 9. (10 поена) Раздвајање. Написати функцију split_orders(df: pd.DataFrame, products: pd.DataFrame) -> tuple која сирове поруџбине чисти, избацује дупликате, проверава и враћа торку (valid, rejected)
# valid су трансформисани исправни редови
# rejected су очишћени неисправни редови и дупликати, са колоном reason
# (дупликати за разлог треба да имају 'duplicate')
# Output: 107 елемената за валидне и 18 за одбијене

def split_orders(df: pd.DataFrame, products: pd.DataFrame) -> tuple:
    df = clean_orders(df)
    unique, duplicates = remove_duplicates(df)
    duplicates = duplicates.assign(reason='duplicate')

    products_ids = set(products['product_id'])

    reason = unique.apply(lambda row : validate_order(row, products_ids), axis= 1)

    valid = transform_orders(unique[reason == 'OK'], products)
    rejected = pd.concat([unique[reason != 'OK'].assign(reason= reason[reason != 'OK']), duplicates])

    return valid, rejected

# orders_df, products_df  = extract_with_out_write(RAW_DIR)
# display(split_orders(orders_df, products_df)[0])
# display(split_orders(orders_df, products_df)[1])

# 10. (10 поена) Агрегација. Написати функцију revenue_by(df: pd.DataFrame, column: str) -> pd.DataFrame која сабира total по вредностима задате колоне и враћа DataFrame са колонама [column, 'revenue'], сортиран од највећег промета
# Input: valid, 'category'
# Output: jerseys 488290.0, balls 66470.0, caps 59940.0, scarves 38070.0, accessories 25130.0

def revenue_by(df: pd.DataFrame, column: str) -> pd.DataFrame:

    result = df.groupby(column)['total'].sum().round(2).reset_index(name='revenue') # reset_index(name='revenue') daje ime novoj koloni

    return result.sort_values('revenue', ascending= False).reset_index(drop= True) # reset_index(drop= True) ovo generise nove indexe (0, 1,2..), da ne koristi stare(0,7,5)

orders_df, products_df  = extract_with_out_write(RAW_DIR)
split = split_orders(orders_df, products_df)

revenue_by(split[0], 'city')

# 11. (10 поена) Load. Написати функцију load(valid: pd.DataFrame, rejected: pd.DataFrame, processed_dir: str) -> dict која у processed_dir уписује 4 CSV фајла и враћа број уписаних редова по фајлу
# clean_orders.csv, rejected_orders.csv, revenue_by_city.csv, revenue_by_category.csv
# load(valid, rejected, PROCESSED_DIR) -> {'clean_orders.csv': 107, 'rejected_orders.csv': 18, 'revenue_by_city.csv': 9, 'revenue_by_category.csv': 5}

def load(valid: pd.DataFrame, rejected: pd.DataFrame, processed_dir: str) -> dict:
    outputs = {
        'clean_orders.csv': valid,
        'rejected_orders.csv': rejected,
        'revenue_by_city.csv': revenue_by(valid, 'city'),
        'revenue_by_category.csv': revenue_by(valid, 'category'),
    }
    for name, df in outputs.items():
        df.to_csv(os.path.join(processed_dir, name), index=False)
    return {name: len(df) for name, df in outputs.items()}

# 12. (5 поена) Run. Написати функцију run_pipeline(raw_dir: str, processed_dir: str) -> dict која покреће цео pipeline и враћа резиме
# Резиме уписати и у summary.csv (у processed_dir), са заглављем metric, value
# Input: run_pipeline(RAW_DIR, PROCESSED_DIR)
# Output: {'total_rows': 125, 'duplicates': 3, 'valid_rows': 107, 'rejected_rows': 18, 'total_revenue': 677900.0}

from datetime import datetime

def log(message: str, path: str) -> None:
    with open(path, 'a') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {message}\n")


def run_pipeline(raw_dir: str, processed_dir: str) -> dict:
    log_path = os.path.join(processed_dir, 'pipeline.log')
    orders, products = extract(raw_dir)
    log(f'Extracted {len(orders)} orders and {len(products)} products', log_path)
    valid, rejected = split_orders(orders, products)
    log(f'Split: {len(valid)} valid, {len(rejected)} rejected', log_path)
    load(valid, rejected, processed_dir)
    summary = {
        'total_rows': len(orders),
        'duplicates': int((rejected['reason'] == 'duplicate').sum()),
        'valid_rows': len(valid),
        'rejected_rows': len(rejected),
        'total_revenue': round(float(valid['total'].sum()), 2),
    }
    pd.DataFrame(list(summary.items()), columns=['metric', 'value']).to_csv(
        os.path.join(processed_dir, 'summary.csv'), index=False)
    log(f'Loaded files: {summary}', log_path)
    return summary

summary = run_pipeline(RAW_DIR, PROCESSED_DIR)
summary