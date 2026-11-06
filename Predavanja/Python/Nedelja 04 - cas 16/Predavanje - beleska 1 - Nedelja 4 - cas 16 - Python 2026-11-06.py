f = open("./resources/test.json")   # ovo je lokacija gde nam je file koji je zapamcen pod f
print(f.read())     # funkcija read za citanje file-a
f.close()   # posle svakog open() moramo close() jer ako ne uradimo close() taj file nije dostupan drugima koji hoce da pristupe file-u

# drugi nacin otvaranja file-a BOLJI i onaj koji se preporucuje
with open("./resources/test.json", "r") as f:    # kada koristimo ovo with onda ne moramo da pisemo close() to radi automatski, ovo r kao drugi parametar oznacava samo citanje
    print(f.read())
import json     # ovo je modul koji nam omugacava da lakse manipulisemo sa json-om

with open("./resources/test.json", "r") as f:
    data_dict = json.load(f)

saved_payment_methods = data_dict["customer"]["profile"]["preferences"]["saved_payment_methods"][0]["type"]      # kako se krecemo kroz vise dictionary-a i listi u jednom file-u

print(saved_payment_methods)

for payment_method in saved_payment_methods:
    print(payment_method["type"])
import json

with open("./resources/test.json", "r") as f:
    data_dict = json.load(f)

items = data_dict["cart"]["items"]

pricings = []

for item in items:
    pricings.append(item["pricing"])

print(pricings)

total_price = 0
for p in pricings:
    total_price += p["unit_price"] * p["quantity"]

print(total_price)
import json

# with open("./data/raw/teams.csv", "r", encoding="utf-8") as f: # ovo encoding=utf-8 je ako radimo na windows-u da bi prepoznao č,ć ... ч,ћ,ш....
with open("./data/raw/teams.csv", "r") as f:    # r odnosno read je po default ako ga i ne upisemo
    for line in f:
        print(repr(line))
import csv

with open("./data/raw/teams.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)   # posto smo ovde prvi put pokrenuli reader sa next() funkcijom on kada ga pokrenemo sledeci put on ce krenuti iz sledeceg reda jer pamti poziciju. Gleda prvi ne procitan red, ponasa se kao iterator
    print(header)
    for row in reader:
        print(row)
rows = [
    ["team", "points"],
    ["FK Jedinstvo", 34]
]

with open("./data/processed/short.csv", "w") as f:  # ovde koristimo write sto je oznaceno kao drugi parametar sa w. Koristimo write ako hocemo da pravimo novi file i da upisemo vrednosti
    csv.writer(f).writerows(rows)   #ovde se koristi upis vise redova od jedanput

row = ["FK Radnički", "Niš"]

with open("./data/processed/short.csv", "a") as f:  # ovde koristimo append to je drugi parametar a i ovo koristimo kada hocemo da dodam nesto u file, ako koristimo write on napravi novi file i obrise prethodno
    csv.writer(f).writerow(row) # ovde se koristi upis jednog reda
with open("./data/raw/teams.csv", "r") as f:
    teams = list(csv.DictReader(f))

print(teams)

# List comprehension - nacin kako se prave liste lakse
points = [int(t["points"]) for t in teams]

top = [t for t in teams if int(t["points"]) > 30]

top2 = [(t["team"], int(t["points"])) for t in teams if int(t["points"]) > 30]

print(max(points))
print(top)
print(top2)
import csv
# ... read_teams(path:str) -> str
# points int

def read_teams(path: str):
    with open(path, "r") as f:
        teams = list(csv.DictReader(f))
    
    for t in teams:
        t["points"] = int(t["points"])
    
    return teams

read_teams("./data/raw/teams.csv")
import csv

# ... save_teams(path_in: str, path_out: str, min_points: int) -> int broj upisanih redova

def save_teams(path_in: str, path_out: str, min_points: int):
    teams = read_teams(path_in)

    top = [t for t in teams if t["points"] >= min_points]

    with open(path_out, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["team", "city", "points"])   # ovo fieldnames je header lista i to je obavezno da se upise
        writer.writeheader()    # header se ne broji u broj upisanih redova, ako ovo ne pokrenemo necemo ima header u file-u i ako su zadati gore u fieldname listi
        writer.writerows(top)

    return len(top)

print(save_teams("./data/raw/teams.csv", "./data/processed/top_teams.csv", 30))