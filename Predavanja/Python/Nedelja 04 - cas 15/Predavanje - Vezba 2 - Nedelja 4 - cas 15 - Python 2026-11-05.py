# 8. Написати функцију clean_text(text: str) -> str која враћа текст без почетних и крајњих размака, и све карактере претвара у мала слова
# Input: ' DATA engineErinG '
# Output: 'data engineering'
test = "DATA engineErinG"

def clean_text(text):
    return text.strip().lower()

print(clean_text(test))
# 9. Написати функцију convert_to_commas(text: str) -> str која мења карактер | са , и враћа нови стринг
# Input: 'apple|orange|cherry'
# Output: 'apple,banana,cherry'
test2 = "apple|orange|cherry"

def convert_to_commas(text):
    return text.replace("|", ",")

print(convert_to_commas(test2))
# 10. Написати функцију get_extension(filename: str) -> str која враћа екстензију прослеђеног фајла
# Input: 'annual_report_2025.md'
# Output: 'md'
test3 = "annual_report_2025.md"

def get_extension(filename):
    lista = filename.split(".")
    return lista[-1]

print(get_extension(test3))
# 11. Префикси наших фактура увек почињу са ITB, написати функцију is_valid_invoice(invoice: str) -> bool која проверава да ли је име фактуре валидно
# Input1: 'ITB-01'
# Output1: True
# Input2: 'CSV-01'
# Output2: False
test4 = "ITB-01"
test5 = "CSV-01"

def is_valid_invoice(invoice):
    return invoice.startswith("ITB")

print(is_valid_invoice(test4))
print(is_valid_invoice(test5))
# 12. Написати функцију combine_tags(tags: list) -> str која враћа тагове спојене са -
# Input: ['python', 'data', 'structures']
# Output: 'python-data-structures'
test6 = ['python', 'data', 'structures']

def combine_tags(tags):
    return "-".join(tags)

print(combine_tags(test6))
# 13. Написати функцију format_team_info(csv_line: str) -> str која лепо исписује информације о тиму
# Input: FK Jedinstvo, Bela Palanka\n
# Output: 'FK Jedinstvo is from Bela Palanka.'
test7 = "FK Jedinstvo, Bela Palanka\n"

def format_team_info(csv_line):
    clean = csv_line.strip().split(",")
    return f"{clean[0]} is from {clean[1]}"

print(format_team_info(test7))
# 14. Написати функцију extract_username(csv_line: str) -> str која из email поља извлачи username
# Сваки csv ред ће имати форму из примера (редослед колона је исти)
# Input: 101,alice@company.com,IT\n
# Output: 'alice'
test8 = "101,alice@company.com,IT\n"

def extract_username(csv_line):
    clean = csv_line.split(",")
    clean_final = clean[1].split("@")
    return clean_final[0]

print(extract_username(test8))

# profino resenje
def extract_username2(csv_line: str):
    # clean = csv_line.strip()
    # parts = clean.split(",")
    # email = parts[1]

    # ovo ispod je isto ovo gore sa linija 16,17,18 samo kraci zapis
    email = csv_line.strip().split(",")[1]
    parts = email.split("@")
    name = parts[0]

    #jos kraci zapis
    # name2 = csv_line.strip().split(",")[1].split("@")[0]    # ali pitanje koliko je ovo pregledno

    return name


extract_username2("101,alice@company.com,IT\n")
# 15. Написати функцију average_salary(csv_lines: list) -> float која рачуна просечну плату
# Input: ["name,salary", "Alice,50000", "Bob,60000"]
# Output: 55000.0
test9 = ["name,salary", "Alice,50000", "Bob,60000"]

def average_salary(csv_lines):
    sum = 0
    count = 0
    for i in csv_lines:
        lista = i.split(",")
        if lista[1].isdigit():
            sum += int(lista[1])
            count +=1

    return sum / count

print(average_salary(test9))

# profino resenje
def average_salary2(csv_lines):
    total_salary = 0.0

    for line in csv_lines[1:]:
        total_salary += int(line.split(",")[1])

    return total_salary / len(csv_lines[1:])

print(average_salary2(test9))