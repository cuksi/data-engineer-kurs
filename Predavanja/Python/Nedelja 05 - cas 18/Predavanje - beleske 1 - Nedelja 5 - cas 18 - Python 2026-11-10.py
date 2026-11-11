import csv
print(type("Nis"))  # <class 'str'>
order ={
    "invoice_id" : "ITB-001",
    "quantity" : 10,
    "unit_price" : 1500
}
class Order:    # klasa pocinje velikim slovom
    def __init__(self, invoice_id, quantity, unit_price):     # dve donje crte kod naziva funkcija oznacava da je u pitanju specijalna funkcija
        self.invoice_id = invoice_id
        self.quantity = quantity
        self.unit_price = unit_price

    def total(self):
        return self.quantity * self.unit_price
    
    def is_valid(self):
        return self.invoice_id.startswith("ITB") and self.quantity > 0
    
    def __repr__(self):     # ovo je represent koji je metod koji opisuje klasu, ali je specijalna funkcija i ovde smo je prilagodili sebi
        return f"Order(\'{self.invoice_id}\',{self.quantity},{self.unit_price}, total is: {self.total()})"
    
    def is_total_price_larger_than(self, amount):
        return self.total() > amount
order1 = Order("ITB-002", 5, 35.5)
print(order1)
print(f"Invoice id: {order1.invoice_id}, total_price: {order1.total()}")

print(order1.is_valid())

order2 = Order("ITB", -3, 1500)
print(order2.is_valid())

print(order1)

print(order1.is_total_price_larger_than(150))
print(order1.is_total_price_larger_than(200))
import csv

class Table:
    def __init__(self, rows):
        self.rows = rows

    # __str__ ali veca praksa da se koristi __repr__
    def __repr__(self):
        return f"Table with {len(self.rows)} rows"
    
    # izbacuje manje od 
    def filter_less_than(self, column, min_value):
        return Table([row for row in self.rows if int(row[column]) > min_value])
    
    def select(self, columns):
        # za svaki red is self.rows
        # ako je kljuc u "columns" zadrzi tu vrednost
        return Table([{k : row[k] for k in columns} for row in self.rows])
    
    def sort_by(self, column): ...  # nije definisana funkcija, samo napisano ime ali posto imaju tri tacke onda ne izbacuje gresku
        # return Table ...
from pprint import pprint

"  novI sAD  ".strip().title().endswith("Sad")

with open("./data/raw/orders2.csv") as f:
    orders = list(csv.DictReader(f))
    table_orders = Table(orders)

pprint(table_orders.rows)
print(table_orders.filter_less_than("unit_price", 75000))

print(table_orders.filter_less_than("unit_price", 75000).rows)

pprint(table_orders.select(["customer", "invoice_id"]).rows)

filtered_table = table_orders.filter_less_than("unit_price", 75000)
selected_columns = filtered_table.select(["customer", "invoice_id"])

pprint(selected_columns.rows)

pprint(table_orders.filter_less_than("unit_price", 75000)
                   .select(["customer", "invoice_id"])
                   .rows)