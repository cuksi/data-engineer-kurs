# 1.
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 2.
def safe_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        None

print(safe_int("25"))
print(safe_int("-10"))
print(safe_int("abC"))

# 3.
def get_grade(grades: dict, student: str) -> int | None:
    try:
        return grades[student]
    except KeyError:
        return None


print(get_grade({"Ana": 5, "Marko": 4, "Jovana": 5}, "Marko"))
print(get_grade({"Ana": 5, "Marko": 4, "Jovana": 5}, "Petar"))

# 4.
import csv

def read_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            reader = csv.reader(f)

            result = "" # ispod for petlja je napravljena zato sto je trazeno da iz funkcije na izlazu bude string a ne list
            for r in reader:
                result += str(r)
        return result
    except FileNotFoundError:
        return "File not found."

print(read_file("./data/raw/teams.csv"))
print(read_file("./greska/data/raw/teams.csv"))

# 5.
def sum_numbers(values: list) -> float:
    result = 0.0
    for v in values:
        try:
            result += float(v)
        except ValueError:
            continue
    return result

print(sum_numbers(["10", "5.5", "abc", "3", "hello"]))

# 6.
def get_age(csv_line: str) -> int | None:
    list_split = csv_line.split(",")
    try:
        return int(list_split[1])
    except ValueError:
        return None
    except IndexError:
        return None
    
print(get_age("Ana,22"))
print(get_age("Marko,abc"))
print(get_age("Jovana"))