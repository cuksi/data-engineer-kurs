# 1. · safe_int(text: str, default: int) -> int
# Претвара ниску у цео број, а ако не може враћа default.
# safe_int('42', 0) → 42 · safe_int('abc', 0) → 0 · safe_int('', -1) → -1

def safe_int(text: str, default: int):
    try:
        result = int(text)
        return result
    except:
        return default
    
print(safe_int("42", 0))
print(safe_int("abc", 0))
print(safe_int("", -1))

# Resenje profe
def safe_int_2(text: str, default: int):
    try:
        return int(text)
    except ValueError as e:
        return default
    

# 2. · safe_read(path: str) -> list
# Учитава CSV као листу речника; ако фајл не постоји, исписује поруку и враћа [].
# len(safe_read('data/raw/teams.csv')) → 4 · safe_read('data/raw/nema.csv') → []

import csv

def safe_read(path: str):
    try:
        with open(path, "r") as f:
            reader = list(csv.DictReader(f))
            return reader
    except FileNotFoundError as e:
        print("File not found \n", e)
        return []
    
print(safe_read("./data/raw/teams.csv"))
print(safe_read("data/raw/nema.csv"))

# Profino resenje
def safe_read_2(path: str):
    try:
        with open(path, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError as e:
        print(f"File not found: {path}")
        return []
    
print(safe_read_2("./data/raw/teams.csv"))
print(safe_read_2("data/raw/nema.csv"))
# 3. · sum_salaries(path: str) -> tuple
# Сабира исправне плате и броји прескочене редове. Користи try око int(), без isdigit().
# sum_salaries('data/raw/employees.csv') → (295000, 2)

import csv

def sum_salaries(path: str):
    suma = 0
    preskoceni_redovi = 0
    with open(path, "r") as f:
        reader = list(csv.DictReader(f))
        for row in reader:
            try:
                suma += int(row["salary"])
            except ValueError as e:
                preskoceni_redovi += 1
    
    return (suma, preskoceni_redovi)

print(sum_salaries("./data/raw/employees.csv"))

# Profino resenje
def sum_salaries_2(path: str):
    total, skipped = 0, 0   # drugi zapis vise promenljivih
    with open(path, "r") as f:
        for row in csv.DictReader(f):
            try:
                total += int(row["salary"])
            except ValueError:
                skipped += 1
    return total, skipped   # Tuple moze i ovako da se vrati ne mora u zagradu

print(sum_salaries_2("./data/raw/employees.csv"))