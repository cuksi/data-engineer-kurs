# Pravilo na databricks-u da se sve pise na vrhu u gornjem code block-u tako da imamo sve na jednom mestu sto koristimo u celom notebook-u
import csv

path = "./data/raw/orders.csv"
def write_key_value(path: str, data: dict, headers: list) -> None:
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data.items())
# 24. 

def read_orders(path: str) -> list:
    # otvori fajl
    # pretvori redove u recnike
    # sve recnike smesti u listu
    
    with open(path, "r") as f:
        return list(csv.DictReader(f))
        
print(read_orders(path))
# 25.
def clean_order(order: dict) -> dict:
    # napravi kopiju order-a
    # strip, za sve vrednosti (sve kljuceve)
    # invoice_id - upper
    # customer i city - title
    result = {k : v.strip() for k,v in order.items()}

    for key in result:
        if key == "customer" or key == "city":
            result[key] = result[key].title()
        elif key == "invoice_id":
            result[key] = result[key].upper()

    return result

print(clean_order({'invoice_id': 'itb-001', 'date': '2025-01-05', 'customer': '     marko petrović ', 'city': 'beograd', 'product': 'Laptop', 'quantity': '1', 'unit_price': '85000'}))
# 26.
def is_positive(text: str) -> bool:    
    # prvi nacin
    try:
        return int(text) > 0
    except ValueError:
        return False
    
    #drugi nacin direktno u return
    # return text.isdigit() and int(text) > 0

def validate_order(order: dict) -> str:
    # Redom provere:
        # invoice_id        -> "invalid invoice"
        # quantity missing  -> "invalid ..."
        # quantit invalid   -> "invalid ..."
        # unit_price        -> "invalid ..."

        # Ako nema gresaka -> "OK"
    if not order["invoice_id"].startswith("ITB"):
        return "invalid_invoice"
    if order["quantity"] == "":
        return "missing_quantity"
    
    # moje resenje, profino ispod za ovaj deo
    # try:
    #     if int(order["quantity"]) <= 0:
    #         return "invalid_quantity"
    #     if int(order["unit_price"]) <= 0:
    #         return "invalid_price"
    # except ValueError:
    #     return "invalid_price"

    if not is_positive(order["quantity"]):
        return "invalid_quantity"
    if not is_positive(order["unit_price"]):
        return "invalid_price"
    
    return "OK"

validate_order({'invoice_id': 'ITB-001', 'date': '2025-01-05', 'customer': ' Marko Petrović ', 'city': 'Beograd', 'product': 'Laptop', 'quantity': 'abc', 'unit_price': '20'})
# 27.
def transform_order(order: dict) -> dict:
    # int(order["quantity"])
    # float(order["unit_price"])
    # order["total"] = quantity * unit_price

    new_dict = order.copy() # ili new_dict = dict(order) je isto, zato sto ako stavimo samo jednako onda nije nova kopija nego pokazujemo u memoriji na isti objekat, menjamo mu samo ime
    # ovde nije morao loop, posto je samo jedan red, Dictionary nije list da ima vise tako da je to jedan red i onda smo mogli direktno samo da pozivamo
    for k in new_dict:
        if k == "quantity":
            new_dict[k] = int(new_dict[k])
        elif k == "unit_price":
             new_dict[k] = float(new_dict[k])
    
    new_dict["total"] = new_dict["quantity"] * new_dict["unit_price"]

    return new_dict

print(transform_order({'invoice_id': 'ITB-001', 'date': '2025-01-05', 'customer': '     marko petrović ', 'city': 'beograd', 'product': 'Laptop', 'quantity': '2', 'unit_price': '85000'}))
# 28.
def split_orders(orders: list) -> tuple:
    # Svaki red iz orders - clean_order
    # Svaki ociscen red - validate_order:
        # Ako "OK" onda valid (+ transform)
        # Ako bilo sta drugo onda rejected (+ reason)

    valid = []
    rejected = []
    for order in orders:
        temp_list = clean_order(order)
        reason = validate_order(temp_list)
        if reason == "OK":
            valid.append(transform_order(temp_list))
        else:
            temp_list["reason"] = reason
            rejected.append(temp_list)

    return (valid, rejected)

print(split_orders(read_orders(path)))
# 29.
def revenue_by(orders: list, column: str) -> dict:
    # Izdvajamo kolonu "column" i stavljamo je kao kljuc recnika
    # Ako je "column" = city : {"Beograd" : 5555, "Novi Sad" : 45845454, ....}
    # Za svaki order iz orders sabiramo "ukupno"

    result = {}
    for order in orders:
        key = order[column]
        result[key] = result.get(key, 0) + order["total"]   # ovaj total je dodat u jednoj od prethodnih funkcija
    
    return result
# 30.
def write_orders(path: str, orders: list) -> int:
    # Uzmi sve "orders" i upisi ih u fajl

    if not orders:
        return 0

    with open(path, "w") as f:
        writer = csv.DictWriter(f, fieldnames= orders[0].keys())    # funkcija keys() nam vraca kljuceve
        writer.writeheader()
        writer.writerows(orders)

    return len(orders)
# 31.
def run_pipeline(input_path: str, output_dir: str) -> dict:
    # read_order(input_path)
    # split_order(valid, rejected)
    # revenue_by....
    # write to file (valid -> clean_orders, rejected -> rejected_orders)

    orders = read_orders(input_path)
    valid, rejected = split_orders(orders)

    write_orders(output_dir + "/clean_orders.csv", valid)
    write_orders(output_dir + "/rejected_orders.csv", rejected)

    write_key_value(
        output_dir + "/revenue_by_city.csv",
        revenue_by(valid, "city"),
        ["cit", "revenue"]
    )

    summary = {
        "total_rows" : len(orders),
        "valid_rows" : len(valid),
        "rejected_rows" : len(rejected),
        "total_revenue" : sum(order["total"] for order in valid)
    }

    write_key_value(
        output_dir + "/summar.csv",
        summary,
        ["metric", "value"]
    )

    return summary
run_pipeline("./data/raw/orders.csv", "./data/processed")