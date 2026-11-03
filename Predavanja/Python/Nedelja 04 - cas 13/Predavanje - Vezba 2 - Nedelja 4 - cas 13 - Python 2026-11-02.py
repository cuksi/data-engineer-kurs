# 7. Исход утакмице. Испишите Home win, Away win, Draw у зависности од вредности променљивих goals_home и goals_away
goals_home = 3
goals_away = 5

if goals_home > goals_away:
    print("Home win")
elif goals_home == goals_away:
    print("Draw")
elif goals_home < goals_away:
    print("Away win")
# 8. За дату температуру одредити категорију: (испод 5 - Cold, од 5 до 20 - Mild, од 20 до 30 - Warm, и од 30 навише - Hot)
# Напомена: лева вредност се увек укључује, док се десна не укључује (20 је Warm)
temperature = 30
if temperature < 5:
    print("Cold")
elif temperature >= 5 and temperature < 20:
    print("Mild")
elif temperature >= 20 and temperature < 30:
    print("Warm")
else:
    print("Hot")
# 9. Опсези. Помоћу for и range испишите сваки низ у једном реду:
# бројеве 0–9
# непарне бројеве од 1 до 20
# минуте полувремена у корацима од 15 (0 15 30 45)
# бројеве од 100 до 50 уназад у корацима од 10.
print("Brojevi od 0 do 9")
i = 0
for i in range(0,10):
    print(i, end=" - ")  # ovo end = ", " end= sluzi da se rezultati ispisuju u istom redu, ovo sto se nalazi unutar navodnika je delimiter odnosno kako razdvaja rezultate ispisa (moze da se upise bilo sta za delimiter)

print("\nNeparni brojevi")
b = 20
for b in range(1, 20):
    if b%2 != 0:
        print(b, end=", ")  # ovo end = ", " end= sluzi da se rezultati ispisuju u istom redu, ovo sto se nalazi unutar navodnika je delimiter odnosno kako razdvaja rezultate ispisa (moze da se upise bilo sta za delimiter)  

print("\nMinute poluvremena")
minutes = 0
for minutes in range(0, 45, 15):
    print(minutes, end=" * ")   # ovo end = ", " end= sluzi da se rezultati ispisuju u istom redu, ovo sto se nalazi unutar navodnika je delimiter odnosno kako razdvaja rezultate ispisa (moze da se upise bilo sta za delimiter)

print("\nBrojevi od 100 do 50 unazad u koracima od 10")
c = 100
for c in range(100, 50, -10):
    print(c, end="; ")  # ovo end = ", " end= sluzi da se rezultati ispisuju u istom redu, ovo sto se nalazi unutar navodnika je delimiter odnosno kako razdvaja rezultate ispisa (moze da se upise bilo sta za delimiter)
# 10. Одбројавање до почетка. Помоћу петље while одбројте од 10 до 1, исписујући сваки број, а затим испишите Kick-off!.
# Затим измените програм тако да се петља раније заустави помоћу break када стигне до 3 и уместо тога испише Match delayed
x = 10
while x > 0:
    print(x)
    x -= 1
print("Kick-off!")

y = 10
while y > 0:
    print(y)
    y -= 1
    if y == 3:
        print("Match delayed.")
        break
# 11. Добродошлица тимовима, користите петљу и f-стринг да испишете по један ред за сваки тим.
# Шаблон: Welcome to the league, <име_тима>!
teams = ['Northport United', 'Riverside FC', 'Hillcrest City', 'Bayview Rovers']

for t in teams:
    print(f"Welcome to the league, {t}!")
# 12. Генерисање SQL упита. Помоћу петље испишите по један упит за сваки стадион
# Шаблон: SELECT * FROM matches_flat WHERE stadium = '<име_стадиона>';
stadiums = ['Arena North', 'Lakeside Park', 'Old Mill Ground']

for s in stadiums:
    print(f"SELECT * FROM matches_flat WHERE stadium = '{s}';")
# 13. Израчунајте укупну посећеност из листе attendances. Израчунајте затим и просек.
attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]
total_attendance = 0
count = 0
for att in attendances:
    total_attendance += att
    count += 1
# print(count)
print("Total attendance: ", total_attendance)
print(f"Average attendance: {total_attendance / count}")
# 14. За form = 'WWDLWDLLWW' пребројте све и израчунајте бодове Резултат треба да буде у следећој форми: W: 5, D: 2, L: 3, Points: 17
form = 'WWDLWDLLWW'
points = 0
wins = 0
draws = 0
loses = 0
for f in form:
    if f == "W":
        points += 3
        wins += 1
    elif f == "D":
        points += 1
        draws += 1
    elif f == "L":
        loses += 1

print(f"W: {wins}, D: {draws}, L: {loses}, Points: {points}")
# 15. Прођите кроз attendances и за сваку утакмицу испишите по један ред са њеним редним бројем и категоријом величине: Large (30.000 или више), Medium (15.000 или више) или Small. На крају испишите колико је утакмица било у категорији Large.
#Пример: једног реда: Match 1: 18200 fans – Medium.
attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]
order = 0
large_num = 0
for atten in attendances:
    if atten > 30000:
        category = "Large"
        large_num += 1
    elif atten >= 15000:
        category = "Medium"
    else:
        category = "Small"
    print(f"Match {order + 1}: {atten} fans - {category}")

print(f"Games with fans in category Large: {large_num}")
# 16. Клуб жели укупно 100.000 навијача ове сезоне. Помоћу петље сабирајте посећеност утакмицу по утакмицу и зауставите се чим збир достигне 100.000.
# Испишите после које утакмице је циљ достигнут и колики је тада био збир.
attendances = [18200, 32454, 27890, 41020, 15300, 22750, 35600, 12900]

visit = 0
krug = 0

while visit <= 100000:
    visit = visit + attendances[krug]
    krug += 1
    # print(f"Krug = {krug}, posecenost = {visit}")

print(f"Posle {krug} utakmice ukupna gledanost je dostigla {visit} posetilaca.")