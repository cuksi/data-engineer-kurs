dirty_input = "   RePOrt_2026.Pdf      \n"

cleaned = dirty_input.strip().lower()   # strip() birse white space ispred i iza, lower() stavlja sve u mala slova

# cleaned = dirty_input.strip()\   
#                      .lower()\
#                      .upper()     # ova kosa crta gore iznad na kraju govori da se ignorise enter na kraju i da je sve jedan red. U tom redu ne moze comment

print(cleaned)
broken_data = "Alice;Engineering;45000"

print(broken_data.replace(";", ","))    # menjamo tacku zarez u zarez
# How to skip comments

row = "# HW to skip this"
print(row)

if row.startswith("#"):    # Ovo vraca true ako je tacno
    print("skipping comment...")
email = "alice@company.com"

email2 = "alice@company.com@hjv@jhvbhjv@jhbghvb@hahf"

print(email.split("@"))
print(email2.split("@"))


parts = email.split("@")
parts[1] = "hidden.com"

print(parts)

print("@".join(parts))  # sa cime spajamo i onda sta spajamo, join() je metod za spajanje
x = ["test", "spajanje"]

print("####".join(x))
# CSV
# "id,name,email"
# "1,alice,alice@compan.com\n"

def parse_csv_line(line):
    clean = line.strip()
    cols = clean.split(",")

    return {"id" : cols[0], "name" : cols[1], "email" : cols[2]}

parse_csv_line("1,alice,alice@compan.com\n")
def parse_csv_line(line):
    clean = line.strip()
    cols = clean.split(",")

    return {"id" : cols[0], "name" : cols[1], "email" : cols[2]}

employee = []

csv_line = [
    "1,alice,alice@compan.com\n",
    "2,bob,bob@company.com\n",
    "3,sara,sara@company.com\n"
]

for line in csv_line:
    employee.append(parse_csv_line(line))

print(employee)