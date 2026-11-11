import csv
def write_key_value(path: str, data: dict, headers: list) -> None:
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data.items())
def read_orders(path: str) -> list:
    with open(path) as f:
        return list(csv.DictReader(f))
    
len(read_orders('./data/raw/orders.csv'))

def clean_order(order: dict) -> dict:
    cleaned_order = { key:value.strip() for key, value in order.items() }
    cleaned_order['invoice_id'] = cleaned_order['invoice_id'].upper()
    cleaned_order['customer'] = cleaned_order['customer'].title()
    cleaned_order['city'] = cleaned_order['city'].title()
    return cleaned_order

clean_order({'invoice_id': 'itb-002', 'customer': 'ana jovanović', 'city': 'NOVI SAD'})
def is_positive_int(text: str) -> bool:
    try:
        return int(text) > 0
    except:
        return False

def validate_order(order: dict) -> str:
    if not order['invoice_id'].startswith('ITB'):
        return 'invalid_invoice'
    if order['quantity'] == '':
        return 'missing_quantity'
    if not is_positive_int(order['quantity']):
        return 'invalid_quantity'
    if not is_positive_int(order['unit_price']):
        return 'invalid_price'
    
    return 'OK'

validate_order({'invoice_id': 'ITB-007', 'customer': 'Ivana Marković', 'city': 'NOVI SAD', 'quantity': '-3', 'unit_price': '1500'})
def transform_order(order: dict) -> dict:
    result = dict(order)
    result['quantity'] = int(result['quantity'])
    result['unit_price'] = float(result['unit_price'])
    result['total'] = result['quantity'] * result['unit_price']
    return result
def split_orders(orders: list) -> tuple:
    valid, rejected = [], []

    for order in orders:
        cleaned_order = clean_order(order)
        reason = validate_order(cleaned_order)

        if reason == 'OK':
            valid.append(transform_order(cleaned_order))
        else:
            cleaned_order['reason'] = reason
            rejected.append(cleaned_order)
    
    return valid, rejected
# order - city, invoice_id, quantity, unit_price, total
def revenue_by(orders: list, column: str) -> dict:
    result = {}

    for order in orders:
        key = order[column]
        result[key] = result.get(key, 0) + order['total']

    return result

# {'Laptop': 262000.0, 'Miš': 3000.0, 'Monitor': 22000.0, 'Tastatura': 7000.0}
#  {'Beograd': 85000.0, 'Novi Sad': 25000.0, 'Kragujevac': 85000.0, 'Niš': 99000.0}
def write_orders(path: str, orders: list) -> int:
    if not orders:
        return 0
    
    with open(path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)
    
    return len(orders)
def run_pipeline(input_path: str, output_dir: str) -> dict:
    orders = read_orders(input_path)
    valid, rejected = split_orders(orders)

    write_orders(output_dir + '/clean_orders.csv', valid)
    write_orders(output_dir + '/rejected_orders.csv', rejected)

    write_key_value(
        output_dir + '/revenue_by_city.csv',
        revenue_by(valid, 'city'),
        ['city', 'revenue']
    )

    summary = {
        'total_rows': len(orders),
        'valid_rows': len(valid),
        'rejected_rows': len(rejected),
        'total_revenue': sum(order['total'] for order in valid)
    }

    write_key_value(
        output_dir + '/summary.csv',
        summary,
        ['metric','value']
    )

    return summary
run_pipeline('./data/raw/orders.csv', './data/processed')