# 1. Написати класу Team са атрибутима name, city и points
# Метода is_top(min_points: int) -> bool враћа да ли тим има бар min_points бодова
# Метода __repr__ даје облик Team('FK Sloga', 19)
# Team('FK Sloga', 'Kraljevo', 19).is_top(30) враћа False
# print(Team('FK Sloga', 'Kraljevo', 19)) исписује Team('FK Sloga', 19)

class Team:
    def __init__(self, name, city, points):
        self.name = name
        self.cit = city
        self.points = points
    
    def is_top(self, min_points: int) -> bool:
        return self.points >= min_points
    
    def __repr__(self):
        return f"Team('{self.name}', {self.points})"

team = Team('FK Sloga', 'Kraljevo', 19)
print(team.is_top(30))
print(team)
# 2. Написати класу Employee са атрибутима name, department и salary
# Метода bonus() -> int враћа 10% плате као цео број (као у задатку 39)
# Employee('Ana Petrović', 'it', 120000).bonus() враћа 12000

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def bonus(self):
        return self.salary // 10
    
emply = Employee('Ana Petrović', 'it', 120000)
emply.bonus()
# 3. Додати класи Table две нове методе
# count() -> int враћа број редова
# head(n: int) -> Table враћа нову табелу са првих n редова
# read_table('data/raw/teams.csv').head(2).count() враћа 2
# Питање: зашто након count() више не можемо да наставимо ланац?

import csv
from pprint import pprint

class Table:
    def __init__(self, rows):
        self.rows = rows

    # __str__ ali veca praksa da se koristi __repr__
    def __repr__(self):
        return f"Table with {len(self.rows)} rows"
    
    def sort_by(self, column):
        return Table(sorted(self.rows, key=lambda r: int(r[column]), reverse=True))
    
    def count(self):
        return len(self.rows)
    
    def head(self, n: int):
        new_rows = self.rows[:n]
        return Table(new_rows)
    

def read_table(path):
    with open(path) as f:
        return Table(list(csv.DictReader(f)))
    
table = read_table("./data/raw/orders.csv")
pprint(table.count())

print(table.head(2).count())

# Ne moze vise da se nastavi niz zato sto return od count() nije vise objekat klase Table