# 1. Napisati funkciju get_even_positions(data: tuple) -> tuple koja vraća elemente torke koji se nalaze na parnim indeksima (0, 2, 4...).
# Input: (10, 20, 30, 40, 50, 60)
# Output: (10, 30, 50)
test1 = (10, 20, 30, 40, 50, 60)

def get_even_positions(data: tuple):
    result = []
    count = 1
    for i in data:
        if count % 2:
            result.append(i)
        count += 1
    
    return tuple(result)

print(get_even_positions(test1))
# 2. Napisati funkciju find_exclusive_students(group1: set, group2: set) -> set koja vraća studente koji se nalaze u prvoj grupi, ali ne i u drugoj.
# Input: {'Ana', 'Marko', 'Jovan', 'Milica'},
#        {'Marko', 'Milica', 'Petar'}
# Output: {'Ana', 'Jovan'}
test2 = {"Ana", "Marko", "Jovan", "Milica"}
test3 = {"Marko", "Milica", "Petar"}

def find_exclusive_students(group1: set, group2: set):
    return group1 - group2

print(find_exclusive_students(test2, test3))
# 3. Napisati funkciju clean_tags(text: str) -> str koja obrađuje tekst sa tagovima.
# Potrebno je:
# Razdvojiti tagove koji su odvojeni karakterom |
# Ukloniti početne i krajnje razmake svakog taga
# Sva slova pretvoriti u mala slova
# Spojiti tagove karakterom -
# Input: ' Python | DATA | SQL ' 
# Output: 'python-data-sql'
test4 = " Python | DATA | SQL "

def clean_tags(text: str):
    temp = text.split("|")
    result_list = []
    for i in temp:
        result_list.append(i.strip().lower())

    return "-".join(result_list)

clean_tags(test4)
# 4. Napisati funkciju count_products(csv_lines: list) -> dict koja analizira porudžbine iz CSV podataka i vraća ukupan broj naručenih proizvoda.
# Svaki red sadrži ime kupca, naziv proizvoda i količinu, razdvojene zarezom. Prvi red predstavlja zaglavlje i treba ga zanemariti.
# Ako se isti proizvod pojavljuje u više redova, sabrati njegove količine.
# Input: [
# 'customer,product,quantity',
# 'Alice,laptop,2',
# 'Bob,mouse,3',
# 'Alice,laptop,1',
# 'Charlie,keyboard,2',
# 'Bob,mouse,1'
# ]
# Output: {
# 'laptop': 3,
# 'mouse': 4,
# 'keyboard': 2
# }
test5 = [
"customer,product,quantity",
"Alice,laptop,2",
"Bob,mouse,3",
"Alice,laptop,1",
"Charlie,keyboard,2",
"Bob,mouse,1"
]

def count_products(csv_lines: list):
    new_list = csv_lines[1:]
    result_dict = {}
    for i in new_list:
        temp_list = i.strip().split(",")
        if temp_list[1] in result_dict:
            result_dict[temp_list[1]] = result_dict[temp_list[1]] + int(temp_list[2])
        else:
            result_dict[temp_list[1]] = int(temp_list[2])

    return result_dict

print(count_products(test5))