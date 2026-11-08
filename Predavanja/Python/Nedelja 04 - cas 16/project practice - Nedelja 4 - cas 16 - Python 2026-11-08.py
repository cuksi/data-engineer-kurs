# 1. Написати функцију clean_row(row: dict) -> dict која враћа нови речник у коме су свим вредностима уклоњени почетни и крајњи размаци
# Не мењати оригинални речник
# Помоћ: dict comprehension (слично као list comprehension, али може и без тога)
# Input: {'name': ' Ana Petrović ', 'department': ' finance ', 'salary': '120000'}
# Output: {'name': 'Ana Petrović', 'department': 'finance', 'salary': '120000'}

def clean_row(row: dict):
    result = {k : v.strip() for (k,v) in row.items()}
    return result

clean_row({"name":"  Ana Petrović ", "department":"  finance ", "salary": "120000"})

# 2. Написати функцију valid_names(path: str) -> list која враћа имена запослених чија је плата исправна
# Користити csv.DictReader и функцију clean_row из задатка 36
# Плата је исправна ако је цео број (помоћ: isdigit())
# Input: 'data/raw/employees.csv'
# Output: ['Ana Petrović', 'marko jovanović', 'Nikola Đorđević']

import csv

path = "./data/raw/employees.csv"

def valid_names(path: str):
    with open(path, "r") as f:
        employees = list(csv.DictReader(f))
    
    count = 0
    for e in employees:
        employees[count] = clean_row(e)
        count += 1
    
    names_empl = [e["name"] for e in employees if e["salary"].isdigit()]
    
    return names_empl

valid_names(path)

# 3. Написати функцију salary_by_department(path: str) -> dict која сабира плате по одељењима
# Редове са неисправном платом прескочити
# Назив одељења претворити у велика слова
# Помоћ: слично задатку (merge_inventories)
# Input: 'data/raw/employees.csv'
# Output: {'IT': 120000, 'HR': 80000, 'FINANCE': 95000}

import csv

path = "./data/raw/employees.csv"

def salary_by_department(path: str):
    with open(path, "r") as f:
        employees = list(csv.DictReader(f))

    departments_salary = {}
    for e in employees:
        if e["salary"].isdigit():
            department = e["department"].upper()
            salary = int(e["salary"])
            if department not in departments_salary:
                departments_salary[department] = salary
            else:
                departments_salary[department] += salary

    return departments_salary

print(salary_by_department(path))

# 4. Написати функцију add_bonus(path_in: str, path_out: str) -> int која у нови фајл уписује само запослене са исправном платом, са додатом колоном bonus (10% плате, цео број)
# Користити csv.DictReader, csv.DictWriter и функцију clean_row
# Помоћ: fieldnames за нови фајл = reader.fieldnames + ['bonus']
# Враћа број уписаних редова
# Input: 'data/raw/employees.csv', 'data/processed/employees_bonus.csv'
# Output: 3
# Садржај фајла након позива:
# name,department,salary,bonus
# Ana Petrović,it,120000,12000
# marko jovanović,HR,80000,8000
# Nikola Đorđević,finance,95000,9500

import csv

path_in = "./data/raw/employees.csv"
path_out = "./data/processed/employees_bonus.csv"

def add_bonus(path_in: str, path_out: str):
    with open(path_in, "r") as f:
        reader = csv.DictReader(f)
        naziv_kolona = reader.fieldnames
        emp_list = list(reader)

    final_list = [clean_row(e) for e in emp_list if e["salary"].isdigit()]
    for fl in final_list:
        fl["bonus"] = int(int(fl["salary"]) * 0.1)

    with open(path_out, "w") as f:
        writer = csv.DictWriter(f, fieldnames= (naziv_kolona + ["bonus"]))
        writer.writeheader()
        writer.writerows(final_list)

    return len(final_list)

print(f"Total number of changes: {add_bonus(path_in, path_out)}")

# 5. Написати функцију split_valid_invalid(path_in: str, valid_path: str, invalid_path: str) -> tuple која исправне и неисправне редове уписује у два различита фајла
# Сваки ред прво очистити функцијом clean_row
# Неисправни редови добијају нову колону reason:
# плата је празна → 'missing_salary'
# плата није цео број → 'invalid_salary'
# Враћа торку (број_исправних, број_неисправних)
# Input: 'data/raw/employees.csv', 'data/processed/valid.csv', 'data/processed/invalid.csv'
# Output: (3, 2)
# Садржај фајла invalid.csv након позива:
# name,department,salary,reason
# Jelena Ilić,IT,,missing_salary
# Ivana Marković,hr,abc,invalid_salary

import csv

path_in = "./data/raw/employees.csv"
path_valid = "./data/processed/valid.csv"
path_invalid = "./data/processed/invalid.csv"

def split_valid_invalid(path_in: str, valid_path: str, invalid_path: str):
    with open(path_in, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        emply_list = list(reader)

    valid_list = []
    invalid_list = []
    for e in emply_list:
        if e["salary"].isdigit():
            valid_list.append(clean_row(e))
        else:
            invalid_list.append(clean_row(e))
    
    for il in invalid_list:
        if il["salary"] == "":
            il["reason"] = "missing_salary"
        else:
            il["reason"] = "invalid_salary"

    with open(valid_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames= header)
        writer.writeheader()
        writer.writerows(valid_list)

    with open(invalid_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames= header + ["reason"])
        writer.writeheader()
        writer.writerows(invalid_list)

    return (len(valid_list), len(invalid_list))

print(f"Number of valid data : Number of invalid data {split_valid_invalid(path_in, path_valid, path_invalid)}")