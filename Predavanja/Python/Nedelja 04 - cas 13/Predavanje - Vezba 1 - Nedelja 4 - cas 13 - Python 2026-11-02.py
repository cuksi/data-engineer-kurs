# 1. Направите променљиве: home_team (текст), attendance (цео број), ticket_price (реалан број - са децималом) и has_roof (тачно/нетачно) са неким вредностима.
# Испишите их све, а затим испишите и њихове типове

home_team = "Crvena Zvezda"
attendance = 41250
ticket_price = 18.5
has_roof = False

print(home_team, attendance,ticket_price, has_roof)

print(type(home_team), type(attendance),type(ticket_price), type(has_roof))




# 2. Допуните код тако да израчунава укупан приход од улазница
attendance = 41250
ticket_price = 18.5
total_amount = attendance * ticket_price
print("Ukupan prihod: " , total_amount)
# 3. Стадион је подељен на блокове од 1000 места, колико је испуњених блокова (//), а колико је навијача у блоку који није попуњен (%)?
attendance = 41250
fill_block = attendance // 1000
print("Ispunjeni blokovi: " , block_fill)

unfill_block = 41250 % 1000
print("Ne ispunjeni blok: ", unfill_block)
# 4. Исправити грешку у следећем коду. Ћелија испод избацује грешку. Покрените је, прочитајте поруку о грешци и исправите је на два начина: једном тако да резултат буде број 12, а једном тако да резултат буде текст '102'
goals_home = '10'
goals_away = 2
# Не мењајте код изнад ове линије
# print(goals_home + goals_away)  # -> vrsta greske koju izbacuje: TypeError: can only concatenate str (not "int") to str
print(int(goals_home) + goals_away)
print(goals_home + str(goals_away))
# 5. Направите листу са 5 назива стадиона. Испишите целу листу, а затим испишите колико карактера има име сваког стадиона.
stadiums = ["Marakana", "JNA", "Radnicki"]

print(stadiums)
print(len(stadiums[0]), len(stadiums[1]), len(stadiums[2]))
#6. Испишите трећи елемент, претпоследњи елемент (негативан индекс) и збор првог и последњег елемента.
# Затим у коментару напишите шта се дешава ако покушамо attendances[6] и зашто
attendances = [18200, 32454, 27890, 41020, 15300, 22750]

print("Treci element: ", str(attendances[2]))
print("Pretposlednji element: ", str(attendances[-2]))
print("Zbir prvog i poslednjeg elementa: ", str( attendances[0] + attendances[-1]))

print(attendances[6]) # ovde izbacuje gresku zato sto ovaj element ne postoji, imamo 6 elemenata u listi ali indeksi krecu od 0 tako da nema 6 nego je zadnji 5