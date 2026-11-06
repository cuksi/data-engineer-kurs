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

path = "data/raw/teams.csv"

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