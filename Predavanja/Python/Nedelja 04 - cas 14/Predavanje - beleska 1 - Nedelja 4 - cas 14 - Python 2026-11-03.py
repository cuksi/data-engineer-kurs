goals = [2, 1, 3, 0, 2]

total_goals = sum(goals)
matches = len(goals)
average_goals = round(total_goals / matches, 2)

print(average_goals)

goals2 = [1, 1, 0, 4, 2, 3]

total_goals2 = sum(goals2)
matches2 = len(goals2)
average_goals2 = round(total_goals2 / matches2, 2)

print(average_goals2)
# def <ime_funkcije>(<param1>, <param2>):   # izgleda kako se pise funkcija

def reci_zdravo(ime):
    print("Pozdrav", ime)

reci_zdravo("Marko")
reci_zdravo("Pera")

def reci_zdravoIP(ime, prezime):
    print(f"Zdravo {ime} {prezime}")

reci_zdravoIP("Goran", "Duric")

reci_zdravoIP(ime = "Goran", prezime = "Duric")     # drugi nacin, gde smo napisali imena parametara

reci_zdravoIP(prezime = "Duric", ime = "Goran")     # treci nacin i ako je izmesan redosled parametara nema greske jer su navedena imena parametara
def reci_zdravoIP1(ime = None, srednje = None, prezime= None):
    poruka = "Zdravo"

    if ime: # ovaj ispis je skraceni oblik za if ime IS NOT NAN
        poruka = poruka + " " + ime
    
    if srednje:
        poruka += " " + srednje

    if prezime:
        poruka += " " + prezime

    print(poruka)

reci_zdravoIP1()    # sta dobijamo kad pokrenemo funkciju bez argumenata, posto imamo uslove i zadate default vrednosti
reci_zdravoIP1("Goran") # ovde dobijamo samo jedan parametar, zato sto je ispunjen samo jedan uslov
reci_zdravoIP1("Goran", "Janko", "Duric")
reci_zdravoIP1(srednje = "Janko", ime = "Goran", prezime = "Duric")
def poslednja_cifra(x):
    return x % 10   # ovo vraca poslednju cifru

poslednja_cifra(12345)
season = "2024/25" # globalna
def label(club):
    note = "klub"   # lokalna

    return f"{note} {club} ({season})"

print(label("Kingsbridge Cit"))
# print (note)    # ne moze jer je lokalna funkcija unutar fukncije
def points(goals_for, goals_against):
    if goals_for > goals_against:
        return 3
    elif goals_for == goals_against:
        return 1
    else:
        return 0
    
print(points(3, 1), points(2,2), points(0,2))

total = points(2, 0) + points(1, 1) + points(0, 3)
print(total)
def fill_pct(attendance, capacity, decimals = 1):
    return round(attendance / capacity * 100, decimals)

print(fill_pct(37968, 47000))
print(fill_pct(37968, 47000, 2))
print(fill_pct(attendance = 37968, capacity = 47000))
def goals_difference(gf, ga):
    gd = gf - ga

result = goals_difference(66, 39)
print(result)   # Ovde je ispis None zato sto nismo stavili return u funkciju

def goals_difference2(gf, ga):
    gd = gf - ga
    return gd

result2 = goals_difference2(66, 39)
print(result2) 