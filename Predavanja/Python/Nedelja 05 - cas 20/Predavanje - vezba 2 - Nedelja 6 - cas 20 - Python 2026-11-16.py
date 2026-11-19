import numpy as np
# Zamisltite da sistem svakog sata belezi broj transkacija.
# Kreirati Numpy niz koji sadrzi broj transkacija za 10 uzastopnih sati.
# - Prikazi broj transkacija za treci sat.
# - Prikazati podatke za poslednja tri sata.
# - Izracunaj ukupan broj transkacija.
# - Izracunati prosecan broj transkacija po satu.

transkacije = np.array([120, 150, 180, 200, 170, 190, 220, 210, 160, 140])

print(transkacije[2])
print(transkacije[-3:])
print(transkacije.sum())
print(transkacije.mean())

# Potrebno je:
# - Pronaci sve procese koji su trajali duze od 60 sekundi.
# - Pronaci procese koji su trajali izmedju 30 i 100 sekundi.
# - Pronaci indekse procesa koji su trajali duze od 60 sekundi.
# - Izbrojati procese koji su trajali duze od 100 sekundi.
# Tehnike: Boolean indexing, np.where(), np.sum()

execution_times = np.array([12, 45, 67, 120, 34, 89, 150, 23, 56, 200])

l_p_1 = execution_times[execution_times > 60]
print(l_p_1)

l_p_2 = execution_times[np.where((execution_times > 30) & (execution_times < 100))]
print(l_p_2)

l_p_3 = np.where(execution_times > 60)
print(l_p_3)

print(f'Ukupno procesa koji su trajali od 60 sekundi: {l_p_1.size}')
