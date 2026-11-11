# Napisati funkciju count_lines(path: str) -> int koja vraca broj nepraznih redova u fajlu

import csv

def count_lines(path: str):
    count = 0
    with open(path) as f:
        reader = list(csv.reader(f))
        for row in reader:
            if len(row) == 0:
                continue
            count += 1

        print(reader)

count_lines("./data/processed/valid.csv")

def count_lines_2(path: str):
    with open(path) as f:
        print([1 for row in f if len(row.strip())])
        print(sum(1 for row in f if len(row.strip())))  # ovaj 1 sluzi kao count isto kao u sql-u

count_lines("./data/processed/valid.csv")

count_lines_2("./data/processed/valid.csv")
# Napisati funkciju read_column(path: str, column: str) -> list koja vraca sve vrednosti jedne kolone csv fajla

def read_column(path: str, column: str):
    x = []
    with open(path) as f:
        reader = csv.DictReader(f)
        
        # if column not in reader.fieldnames:   # ovaj uslov je izbacen posto je u returnu dodat uslov if column in reader.fieldnames
        #     return []
        
        # for row in reader:    # kada bi ovo pokrenuli onda bi return bila prazna lista zato sto je reader prosao kroz ceo fajl i na kraju bi krenuo od kraja gde nema nsita i to je prazna lista
        #     print(row)
        
        return [rwo[column] for rwo in reader if column in reader.fieldnames]

read_column("./data/processed/valid.csv", "department")