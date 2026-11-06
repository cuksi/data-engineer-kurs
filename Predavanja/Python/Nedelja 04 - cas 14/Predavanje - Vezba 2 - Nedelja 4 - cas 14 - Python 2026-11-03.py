# 1. Ispisati današnji datum.
import datetime

print(datetime.datetime.now())
# Ispisati trenutnu godinu, mesec i dan.

sada = datetime.datetime.now()
print("Trenutna godina: ", sada.year)
print("Trenutni mesec: ", sada.month)
print("Trenutni dan: ", sada.day)
# 3. Izračunati koji će datum biti za 30 dana.
sada2 = datetime.datetime.now()
za_tridest = sada2 + datetime.timedelta(days= 30)

print(za_tridest)
# 4. Izračunati koliko dana ima između 1. januara 2026. i današnjeg datuma.
sada3 = datetime.date(2026, 11, 3)
target = datetime.date(2026, 1, 1)
razlika = sada3 - target

print(razlika)

# drugi nacin
target2 = datetime.date(2026, 1, 1)
razlika2 = datetime.date.today() - target

print(razlika2)
# 5. Ispisati današnji datum u formatu dd.mm.yyyy.
sada4 = datetime.date.today()
formatiran = sada4.strftime("%d.%m.%Y.")

print(formatiran)

# drugi nacin
formatiran2 = datetime.date.today().strftime("%d.%m.%Y.")

print(formatiran2)