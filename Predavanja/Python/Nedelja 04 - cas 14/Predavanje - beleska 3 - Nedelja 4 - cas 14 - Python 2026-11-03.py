# Torke = Tuple ne moze da se menja

utakmica = ("Partizan", "Zvezda", 2, 1)

print(utakmica)

print(utakmica[0])
lista = [10, 20, 30]
torka = (10, 20, 30)

lista[0] = 100  # ovde smo promenili vrednost prvo clana liste
print(lista)

# torka[0] = 100  # TypeError: 'tuple' object does not support item assignment - Tuple ne moze da se menja

a = (5)     # ovo je INT
b = (5,)    # a ovo je TUPLE sa jednim elementom zato sto ima zarez iza 5

print(type(a))
print(type(b))

lista.pop() # ako ne dodamo nista onda izbacuje zadnji clan izlist
print(lista)

lista.pop(1) # a ako zadamo index onda izbacuje taj element iz liste
print(lista)
# append(value) adds a value to the end
# insert(index, value) adds a value at a chosen position
# pop() removes the last item
# remove(value) removes the first matching value
# len(list) gives the number of items
# sort() puts items in order

# Slicing list list[start:end]
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4]) # uzmi od prve do cetvrte, ovde vazi da ne ukljucujemo desni broj
print(numbers[:3]) # ovo je od prve do trece, ovde vazi da ne ukljucujemo desni broj
print(numbers[3:]) # ovo je od treceg pa do kraja
print(numbers[:])   # ovo ce uzeti celu listu
form = ["W", "D", "L", "W", "W"]
goals = [3, 1, 0, 2, 4]

print(form[1:4])
print("L" in form)  # ovo je da proveri jel ima L u listi i vraca true ili false
print("K" in form) 
# Raspakivanje primer:

def result(home, away):
    if home > away:
        return "W", 3
    elif home == away:
        return "D", 1
    
    return "L", 0

letter, pts = result(2, 1)  # sad se razultat ove funkcije smesta u ove promenljive
print(letter, pts)

score = (3, 1)
home, away = score  # ovo je raspakivanje torke
print(result(home, away))
# Raspakivanje torke kroz petlju

def points(goals_for, goals_against):
    if goals_for > goals_against:
        return 3
    elif goals_for == goals_against:
        return 1
    else:
        return 0

scores = [(2,1), (0,0), (1,3), (4,2)]

total = 0

for home, away in scores:
    total = total + points(home, away)
    print("Unutar petlje", total)

print(total)