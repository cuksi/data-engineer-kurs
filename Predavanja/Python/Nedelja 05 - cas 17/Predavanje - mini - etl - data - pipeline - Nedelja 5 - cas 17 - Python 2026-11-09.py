# 24. 
def read_orders(path: str) -> list:
    # otvori fajl
    # pretvori redove u recnike
    # sve recnike smesti u listu

# 25.
def clean_order(order: dict) -> dict:
    # napravi kopiju order-a
    # strip, za sve vrednosti (sve kljuceve)
    # invoice_id - upper
    # customer i city - title
    
# 26.
def validate_order(order: dict) -> str:
    # Redom provere:
        # invoice_id        -> "invalid invoice"
        # quantity missing  -> "invalid ..."
        # quantit invalid   -> "invalid ..."
        # unit_price        -> "invalid ..."

# 27.
def transform_order(order: dict) -> dict:
    # int(order["quantity"])
    # float(order["unit_price"])
    # order["total"] = quantity * unit_price

# 28.
def split_orders(orders: list) -> tuple:
    # Svaki red iz orders - clean_order
    # Svaki ociscen red - validate_order:
        # Ako "OK" onda valid (+ transform)
        # Ako bilo sta drugo onda rejected (+ reason)

# 29.
def revenue_by(orders: list, column: str) -> dict:
    # Izdvajamo kolonu "column" i stavljamo je kao kljuc recnika
    # Ako je "column" = city : {"Beograd" : 5555, "Novi Sad" : 45845454, ....}
    # Za svaki order iz orders sabiramo "ukupno"

# 30.
def write_orders(path: str, orders: list) -> int:
    # Uzmi sve "orders" i upisi ih u fajl

# 31.
def run_pipeline(input_path: str, output_dir: str) -> dict:
    # read_order(input_path)
    # split_order(valid, rejected)
    # revenue_by....
    # write to file (valid -> clean_orders, rejected -> rejected_orders)