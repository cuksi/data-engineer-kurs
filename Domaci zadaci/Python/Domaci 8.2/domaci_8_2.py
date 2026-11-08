# 16. Написати функцију count_lines(path: str) -> int која враћа број непразних редова у фајлу
# Input: 'data/raw/teams.csv'
# Output: 5

import csv

path = "data/raw/teams.csv"

def count_lines(path: str):
    with open(path, "r") as f:
        reader = csv.reader(f)
        count = []

        for r in reader:
            count.append(r)
    
    return len(count)


print(count_lines(path))
# 17. Написати функцију read_column(path: str, column: str) -> list која враћа све вредности једне колоне CSV фајла
# Input: 'data/raw/teams.csv', 'city'
# Output: ['Bela Palanka', 'Niš', 'Beograd, Rakovica', 'Kraljevo']
# Ако колона не постоји, вратити празну листу []
import csv

path = "./data/raw/teams.csv"

def read_column(path: str, column: str):
    with open(path, "r") as f:
        teams = list(csv.DictReader(f))
    
    return [t["city"] for t in teams]

read_column(path, "city")
# 18. Написати функцију write_key_value(path: str, data: dict, headers: list) -> None која речник уписује у CSV фајл са две колоне
# Input: 'data/processed/summary.csv', {'rows': 10, 'valid': 6}, ['metric', 'value']
# Садржај фајла након позива:
# metric,value
# rows,10
# valid,6

import csv

path2 = "./data/processed/summary.csv"
data_dict1 = {"rows": 10, "valid": 6}
header_list1 = ["metric", "value"]

def write_key_value(path: str, data: dict, headers: list):
    result = [(k,v) for k,v in data.items()]
    with open(path, "w") as f:
        csv.writer(f).writerow(headers)
        csv.writer(f).writerows(result)

write_key_value(path2, data_dict1, header_list1)
# 19. Написати функцију get_header(path: str) -> list која враћа заглавље CSV фајла
# Користити csv.reader и next()
# Input: 'data/raw/teams.csv'
# Output: ['team', 'city', 'points']

import csv

path3 = "./data/raw/teams.csv"

def get_header(path: str):
    with open(path, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
    return header

print(get_header(path3))
# 20. Написати функцију read_rows(path: str) -> list која враћа све редове CSV фајла без заглавља, као листу листи
# Користити csv.reader
# Input: 'data/raw/teams.csv'
# Output: [['FK Jedinstvo', 'Bela Palanka', '34'], ['FK Radnički', 'Niš', '41'], ['FK Rakovica', 'Beograd, Rakovica', '28'], ['FK Sloga', 'Kraljevo', '19']]

import csv

path4 = "./data/raw/teams.csv"

def read_rows(path: str):
    with open(path, "r") as f:
        reader = csv.reader(f)
        header = next(reader)

        result_list = []

        for row in reader:
            result_list.append(row)

    return result_list

print(read_rows(path4))
# 21. Написати функцију total_points(path: str) -> int која враћа збир бодова свих тимова
# Користити csv.DictReader
# Input: 'data/raw/teams.csv'
# Output: 122

import csv

path5 = "./data/raw/teams.csv"

def total_points(path: str):
    with open(path, "r") as f:
        teams = list(csv.DictReader(f))
        points = [int(t["points"]) for t in teams]
        total_pts = 0
        for p in points:
            total_pts += p
    return total_pts

total_points(path5)
# 22. Написати функцију write_rows(path: str, rows: list) -> None која листу листи уписује у CSV фајл
# Input: 'data/processed/people.csv', [['name', 'age'], ['Ana', 20], ['Marko', 22]]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22

import csv

path6 = "./data/processed/people.csv"
input_list = [["name", "age"], ["Ana", 20], ["Marko", 22]]

def write_rows(path: str, rows: list):
    with open(path, "w") as f:
        writer = csv.writer(f).writerows(rows)

write_rows(path6, input_list)
# Написати функцију write_dicts(path: str, rows: list) -> None која листу речника уписује у CSV фајл
# Користити csv.DictWriter; заглавља су кључеви првог речника
# Input: 'data/processed/people.csv', [{'name': 'Ana', 'age': 20}, {'name':'Marko', 'age': 22}]
# Садржај фајла након позива:
# name,age
# Ana,20
# Marko,22

import csv

path7 = "./data/processed/people.csv"
input_list2 = [{"name": "Ana", "age": 20}, {"name":"Marko", "age": 22}]

def write_dicts(path: str, rows: list):
    with open(path, "w") as f:
        writer = csv.DictWriter(f, fieldnames= ["name", "age"])
        header = writer.writeheader()
        data = writer.writerows(rows)

write_dicts(path7, input_list2)