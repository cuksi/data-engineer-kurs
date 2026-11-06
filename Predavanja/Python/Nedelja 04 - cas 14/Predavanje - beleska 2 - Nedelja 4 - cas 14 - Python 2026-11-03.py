import math     # ovde je uvezen cao math modul

print(math.sqrt(64))   # koren

print(math.pi)
from math import sqrt   # ovde je uvezena odredjena funkcija iz math modula

print(sqrt(64))   # koren

# print(pi) # ovo sad ne radi jer smo uvezli samo jednu funkciju sqrt
import math as m   # ovo je novi naziv za math modul da imamo kraci zapis i lakse pozivanje

print(m.sqrt(64)) 
from math import sqrt, factorial    # ovo kako se uvozi vise funkcija iz modula

print(sqrt(64))

print(factorial(3))
import datetime

danas = datetime.date.today()
print(danas)

print(danas.year)

print(danas.month)

print(danas.day)
import datetime

vreme = datetime.time(14, 30, 45)   # 14 je sat, 30 je minuta, 45 su sekunde

print(vreme)

print(vreme.hour)

print(vreme.minute)

print(vreme.second)
import datetime

trenutno = datetime.datetime.now()

print(trenutno)

print(trenutno.year)
print(trenutno.day)
print(trenutno.hour)
import datetime

datum1 = datetime.date(2026, 11, 1)
datum2 = datetime.date(2026, 11, 3)

razlika = datum2 - datum1

print(razlika)  # posto nema vreme racuna od 00:00

print(razlika.days)     # ispisuje razliku u broju dana
import datetime

danas = datetime.date.today()

za_pet_dana = danas + datetime.timedelta(days = 5)  # ovo je funkcija da odemo 5 dana u napred

print(za_pet_dana)
import datetime

# Formatiranje datuma
danas = datetime.date.today()
formatiran_datum = danas.strftime("%d.%m.%Y")     # funkcija za formatiranje datuma, procenat je obavezan jer nam sluzi da kaze sta da uzmemo. Veliko Y je 2026 a malo  je 26
print(formatiran_datum)
import datetime

datum = datetime.datetime.strptime("03.11.2026", "%d.%m.%Y")    # od stringa pravi datetime format, ide prvo string sa datumom a onda ide format po kome je upisan

print(datum)
import math

print(math.ceil(21.7))  # zaokruzuje na vecu vrednost

print(math.floor(21.7)) # zaokruzuje na manju vrednost