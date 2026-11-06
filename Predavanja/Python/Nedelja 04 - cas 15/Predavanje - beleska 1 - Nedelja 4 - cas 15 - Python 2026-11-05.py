# Sets

# 2,4,6,8   - skup parnih brojeva
# 1,3,5,7   - skup neparnih brojeva
# raspored elemanta u skupu ne znamo kako ce biti ispisani, nemaju odredjeni redosled. Ali ne mogu da imaju duplikate

lista = [1,2,-5,3,4,1,-5,2,1,1,4,6,7,8]

distinct_list = []
for e in lista:
    if e in distinct_list:
        continue    # ovo je komanda da preskoci, tj da zavrsi taj krug petlje i da nastavi dalje, tako da ispod continue nece nastaviti nego krenuti novi krug
    distinct_list.append(e)

print(distinct_list)

set_from_lista = set(lista)
print(set_from_lista)   # ovo je ispis seta (skupa bez duplikata), redosled ne mora da znaci da ce biti po redu nego je nasumicno

print(list(set_from_lista))     # ovo je da vratim set (skup) u listu

# Moze i Tupple da se pretvori u set tj. skup
set1 ={1, 2, 3 ,4}     # set tj. skup definise se viticastim zagradama
set2 = {2, 4, 6, 8, 10}

print(set1 - set2)  # Difference, razlika skupova
print(set2 - set1)

print(set1 & set2)  # Intersect, presek skupa seta

print(set1 | set2)  #Union, unija dva skupa tj. seta

set1.add(999)  # ovo je funkcija za dodavanje u set tj. skup
print(set1)

set3 = {}   # ne rpavi se set tj. skup ovako zato sto ako dodamo ispod neku vrednost bice greska jer ga vidi kao dictionary
#set3.add(3)
print(type(set3))   # ovde se viidi da ga ne vidi kao set nego dictionary

set4 =set()   # ako nam treba prazan set tj. skup on se pravi ovako
print(type(set4))   # a ovde se vidi da ga vidi kao set
# Dictionary tj recnik

team = { "team_id" : 10,                # recnik se isto definise sa viticastim zagradama
        "team_name" : "Jedinstvo",
        "points" : 45,
        "stadium_name" : "Rajko Mitic"
        }

print(team)                 # nacini na koje mozemo da ispisujemo dictionary vrednosti
print(team["team_id"])
print(team["points"])
print(team["team_name"])        # pozivanje iz naseg dictionary-a koji smo mi napravili onda mozemo ovako inace ako ne znamo pozivamo iz baze onda se preporucuje da se koristi get()

# print(team["total_goals"])  # ovode izbacuje gresku jer smo trazili nesto sto nema -> KeyError: 'total_goals'

print(team.get("total_goals"))  # ovde ce da vrati None jer ga trazimo preko funkcije get()

print(team.get("total_goals", 0))   # ovde smo zdali default vrednost koju da vrati ako ga nema u recniku, ali ovo ne dodaje u recnik samo prikazuje nama

team["total_goals"] = 10    # ovo je kako dodajemo u dictionary key : value par
print(team)

# team["total_goals"] = team["total_goals"]  +  2 # ovo je isti zapis kao ovaj ispod
team["total_goals"] += 2 
team["points"] += 3

print(team)
teams = [       # primer liste koja sadrzi dictionary
    { 
     "team_id" : 10,                
     "team_name" : "Jedinstvo",
     "points" : 45,
     "stadium_name" : "Rajko Mitic"
    },
    { 
     "team_id" : 10,                
     "team_name" : "Jedinstvo",
     "points" : 45,
     "stadium_name" : "Rajko Mitic"
    },
    { 
     "team_id" : 10,                
     "team_name" : "Jedinstvo",
     "points" : 45,
     "stadium_name" : "Rajko Mitic"
    },
]
# ... count_chars(text: str) -> dict
# Broji karaktere reci
# "hello" -> {"h" : 1, "e" : 1, "l" : 2, "o" : 1}

def count_chars(text):
    frequnecy = {}  # Empty dictionary

    for c in text:
        if frequnecy.get(c) is None:
            frequnecy[c] = 1
        else:
            frequnecy[c] += 1
    return frequnecy

print(count_chars("hello"))

# drugi nacin
def count_chars2(text):     # isto vraca ali je losiji nacin zato sto imamo dve petlje, na malom primeru se nevidi razlika, ali da je vise slova ovao resenje bi duze trajalo
    frequnecy = {} 

    for c in text:
        frequnecy[c] = 0
    for c in text:
        frequnecy[c] += 1
    return frequnecy

print(count_chars2("hello"))

# treci nacin
def count_chars3(text):     # isto vraca ali je losiji nacin zato sto imamo dve petlje, na malom primeru se nevidi razlika, ali da je vise slova ovao resenje bi duze trajalo
    frequnecy = {}

    for c in text:
        frequnecy[c] = frequnecy.get(c, 0) + 1  # ovde definisemo default vrednost da je nula i onda dodamo samo jedan za svaki put, a ako imamo vrednost onda ce biti ta vrednost a ne default i dobijamo tacno resenje
    return frequnecy

print(count_chars3("hello"))
# ... find_common_tags(tags1: tuple, tags2: tuple) -> set
def find_common_tags(tags1, tags2):
    return set(tags1) & set(tags2)

print(find_common_tags(("python", "sql", "programming"), ("sql", "data", "programming")))


# drugi nacin
def find_common_tags2(tags1, tags2):
    common_set = set()

    for e in tags1:
        if e in tags2:
            common_set.add(e)
    return common_set

print(find_common_tags2(("python", "sql", "programming"), ("sql", "data", "programming")))