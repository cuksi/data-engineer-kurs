# izgled if petlje:
# if condition:   
#     line 1
#     block body
#     line 3
#     ...
#     line n
# elif condition2:
#     line 1
#     block body
#     line 3
#     ...
#     line n
# elif condition3:
#     block body
# else:
#     line 1
#     block body
#     line 3
#     ...
#     line n

# Koji uslovi postoje: <, >, <=, >=, ==, !=
# and, or

attendance = 10000
size = None     #ovo definisemo sa nekom ddefault vrednoscu radi sigurnosti ako ne updane ni u jedan uslov da ne izbaci gresku da promenljiva nije definisana

if attendance >= 30000:
    print("I've entered first block")
    size = "Large"
elif attendance >= 15000 and attendance < 30000:    # ovo nije potrebno ovde and attendance < 30000 jer ako nam je redosled ovaka moze bez ovoga
    print("I've entered second block")
    size= "Medium"
else:
    print("I've entered else block")
    size = "Small"

print("Provided attendance category: ", size)
attendances = [32454, 23456, 32987, 21345, 29945]

# primer for petlje
for a in attendances:
    print("Generating report for attendance: ", a)

print("We are finished.")
# f-string (format string)

year = 2026
text = f"Year is {year}. Test"

# text = f"Year is {year + 3}. Test"  # primer sa racunanjem u f-stringu

print(text)
# SELECT * FROM matches_flat WHERE weather = 'clear'

weather_condtions = ["fog", "clear", "snow", "rain"]

for condition in weather_condtions:
    print(f"SELECT * FROM matches_flat WHERE weather = '{condition}';")     # voditi racuna ovde nam treba jedan navodnik da bi definisali string u SQL-u tako da moramo da ga dodamo
    print(condition)

    print(f'SELECT * FROM matches_flat WHERE weather = \'{condition}\';')   # ovo je primer kada je jedan apostrof onda mora escape \
# Niska (isto sto i String) niz karaktera

form = "WDLWWWDL"
points = 0

for result in form:
    print("Current result: ", result)
    if result == "W":
        points = points + 3
    elif result == "D":
        points = points + 1
    print("After match: ", points)

print("-----------------")  # ili \n za za new line
print("Final points: ", points)
form = "WL  R,E,M;S9KD1DLWWL"   # W D L i dalje treba da gledamo ove iste karaktere
list_form = ["W", "L", " ", " ", " ", " ", "R", "," "itd...."]  # ovo gore from je isto kao da smo ga pisali ovako kao listu

for result in form:
    print("Current result: ", result)
    if result == "W":
        points = points + 3
    elif result == "D":
        points = points + 1
    print("After match: ", points)
    
print("\nFinal points: ", points)
n = 10

while n > 0:
    print(f"n: {n}")
    n = n - 3   # Update vrednosti iz petlje ide na kraju da bi stigli prvo da iskoristimo tu vrednost
print(f"After loop, n: {n}")
attendances = [32454, 23456, 32981, 21345, 29945, 98123]
x = 32981
count = 0 # how many times loop started
found_x = False # Flag - da li je nesto pronadjeno ili nije

for a in attendances:
    count = count + 1
    if x  == a:
        found_x = True
        break # komanda za prekid petlje

print("Is x found? ", found_x)
print("Count: ", count)
# Range uvek definise vrednosti u napred nije kao inkrement i ako je taj rezultat, nego on generise u napred sve vrednosti a nakon toga postuje zadate uslove.
rng = range(5)  # [0, 1, 2, 3, 4]
print("-------------------------------")
for i in rng:
    i = i + 10
    print(i)
print("-------------------------------")
for b in range(4, 16):  # range(start, stop , step), leva strana uvek ukljucena a desna nije u Python-u
    b = b / 2  
    print(b)   
print("-------------------------------")
for c in range(4, 16, 2):  # range(start, stop , step), leva strana uvek ukljucena a desna nije u Python-u
    print(c)   
print("-------------------------------")
for d in range(1, 11, 2):  # range(start, stop , step), leva strana uvek ukljucena a desna nije u Python-u
    print(d)   

for u in range(100, 5, -3):     # range(start, stop , step), leva strana uvek ukljucena a desna nije u Python-u. Ovde idemo u nazad
    print(u)