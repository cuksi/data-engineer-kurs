import json
import os
from urllib.parse import urljoin

import pandas as pd
import requests

BASE_URL = 'https://cvijan.github.io/nss-api/v1/'
RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
def get_json(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

# get_json(BASE_URL + 'products/page-2.json')
# Странице. Написати функцију fetch_all(first_url: str) -> list која прати
# next линкове и враћа записе са свих страна у једној листи

def fetch_all(first_url: str) -> list:
    records = [] 
    url = first_url
    while url:
        page = get_json(url)
        records.extend(page['data'])
        url = urljoin(url, page['next']) if page['next'] else None
    return records

fetch_all(BASE_URL + 'products/page-1.json')
def save_raw(records: list, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

save_raw([{'id': 1, 'city': 'Niš'}], os.path.join(RAW_DIR, 'test.json'))
# Extract. Написати функцију extract(raw_dir: str) -> tuple која преузима све
# потребне податке са API-ја (orders и products) и враћа их као два DataFrame-а

def extract(raw_dir: str) -> tuple:
    orders = fetch_all(BASE_URL + 'orders/page-1.json')
    products = fetch_all(BASE_URL + 'products/page-1.json')
    
    save_raw(orders, os.path.join(raw_dir, 'orders.json'))
    save_raw(products, os.path.join(raw_dir, 'products.json'))

    orders_df = pd.json_normalize(orders, sep='_')
    orders_df = orders_df.rename(columns={'customer_name': 'customer', 'customer_city': 'city'})
    
    return orders_df, pd.DataFrame(products)

orders_df, products_df = extract(RAW_DIR)
# Clean. Написати функцију clean_orders(df: pd.DataFrame) -> pd.DataFrame

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ['order_id', 'customer', 'city', 'payment']:
        df[col] = df[col].str.strip()
    df['order_id'] = df['order_id'].str.upper()
    df['customer'] = df['customer'].str.title()
    df['city'] = df['city'].str.title().fillna('Unknown')
    return df

clean_orders(orders_df)
def remove_duplicates(df: pd.DataFrame) -> tuple:
    is_dup = df.duplicated('order_id', keep='first')
    return df[~is_dup], df[is_dup]

remove_duplicates(orders_df)

def validate_order(row: dict, product_ids: set) -> str:
    quantity = pd.to_numeric(row['quantity'], errors='coerce')
    price = pd.to_numeric(row['unit_price'], errors='coerce')
    if not row['order_id'].startswith('NSS-'):
        return 'invalid_order'
    if pd.isna(row['quantity']):
        return 'missing_quantity'
    if pd.isna(quantity) or quantity <= 0 or quantity != int(quantity):
        return 'invalid_quantity'
    if pd.isna(price) or price <= 0:
        return 'invalid_price'
    if row['product_id'] not in product_ids:
        return 'unknown_product'
    return 'OK'
def transform_orders(df: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['quantity'] = pd.to_numeric(df['quantity']).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price']).astype(float)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total'] = df['quantity'] * df['unit_price']
    names = products[['product_id', 'name', 'category']].rename(columns={'name': 'product_name'})
    return df.merge(names, on='product_id', how='left')
def split_orders(df: pd.DataFrame, products: pd.DataFrame) -> tuple:
    df = clean_orders(df)
    unique, duplicates = remove_duplicates(df)
    duplicates = duplicates.assign(reason='duplicate')
    product_ids = set(products['product_id'])
    reasons = unique.apply(lambda row: validate_order(row, product_ids), axis=1)
    valid = transform_orders(unique[reasons == 'OK'], products)
    rejected = pd.concat([unique[reasons != 'OK'].assign(reason=reasons[reasons != 'OK']), duplicates])
    return valid, rejected
def revenue_by(df: pd.DataFrame, column: str) -> pd.DataFrame:
    result = df.groupby(column)['total'].sum().round(2).reset_index(name='revenue')
    return result.sort_values('revenue', ascending=False).reset_index(drop=True)
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