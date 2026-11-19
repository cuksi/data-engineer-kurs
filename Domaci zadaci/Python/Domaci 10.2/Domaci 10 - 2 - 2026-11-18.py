import numpy as np

# 1. Sistem beleži broj aktivnih korisnika tokom 12 uzastopnih sati.
# Potrebno je:
# Prikazati broj korisnika za peti sat.
# Prikazati broj korisnika za poslednja četiri sata.
# Izračunati ukupan broj aktivnih korisnika kroz svih 12 sati.
# Izračunati prosečan broj korisnika po satu.
# Pronaći sat sa najvećim brojem korisnika.

active_users = np.arange(1, 13)

print(f'Broj korisnika za peti sat: {active_users[4]}')
print(f'Broj korisnika za poslednja 4 sata: {active_users[-4:]}')
print(f'Ukupan broj korisnika: {np.sum(active_users, axis= 0, keepdims= True)}')
print(f'Prosecan broj korisnika po satu: {np.mean(active_users)}')
print(f'Sat sa najvecim brojem korisnika: {np.argmax(active_users) + 1}, broj korisnika za taj sat: {active_users[np.argmax(active_users)]}')

# 2. Sistem beleži CPU, RAM i disk usage za pet različitih servera.
# Redovi predstavljaju servere, a kolone CPU, RAM i disk usage.
# Potrebno je:
# Prikazati dimenzije matrice.
# Prikazati broj servera i broj metrika.
# Izračunati prosečnu vrednost svake metrike.
# Izračunati prosečnu potrošnju resursa za svaki server.
# Pronaći server sa najvećom prosečnom potrošnjom resursa.

servers = np.arange(64, 1024, 64).reshape(5,3)

print(f'Dimenzija matrice: {servers.ndim}')
print(f'Broj servera: {servers.shape[0]} i broj metrika: {servers.shape[1]}')
print(f'Prosecna vrednost svake metrike: {np.mean(servers, axis= 0)}')

avg_res_servers = np.mean(servers, axis= 1)
print(f'Prosecna potrosnja resursa za svaki server: {avg_res_servers}')

print(f'Server sa najvecom potrosnjom resursa: {np.argmax(avg_res_servers) + 1}')

# 3. Sistem beleži vreme izvršavanja 15 različitih procesa u sekundama. Potrebno je:
# Pronaći sve procese koji su trajali duže od 100 sekundi.
# Pronaći procese koji su trajali između 40 i 100 sekundi.
# Izbrojati procese koji su trajali kraće od 50 sekundi.
# Pronaći indekse procesa koji su trajali duže od 100 sekundi.
# Izračunati prosečno vreme izvršavanja svih procesa.

process = np.arange(10, 160, 10)

print(f'Procesi koji su trajali duze od 100 sekundi: {process[process > 100]}')
print(f'Procesi koji su trajali duze od 40 sekundi a krace od 100 sekundi:  {process[(process >= 40) & (process < 100)]}')
print(f'Ukupan broj procesa koji su trajali krace od 50 sekundi: {process[process < 50].size}')
print(f'Indeksi procesa koji su trajali duze od 100 sekundi: {np.where(process > 100)[0]}')
print(f'Prosecno vreme izvrsavanja svih procesa: {np.mean(process)}')

# 4. Prodavnica beleži prihode od četiri različite kategorije proizvoda tokom šest meseci. Redovi predstavljaju kategorije proizvoda, a kolone mesece. Potrebno je:
# Izračunati ukupan prihod svake kategorije proizvoda.
# Izračunati ukupan prihod za svaki mesec.
# Pronaći kategoriju proizvoda sa najvećim ukupnim prihodom.
# Pronaći mesec sa najvećim ukupnim prihodom.
# Izračunati prosečan prihod po kategoriji proizvoda.
# Izračunati prosečan mesečni prihod svih kategorija.

products = np.arange(1,25).reshape(4,-1)

total_cat = np.sum(products, axis= 1)
print(f'Ukupan prihod svake kategorije proizvoda: {total_cat}')
total_month = np.sum(products, axis= 0)
print(f'Ukupan prihod za svaki mesec: {total_month}')
print(f'Kategorija proizvoda sa najvecim ukupnim prihodom: {np.argmax(total_cat) + 1}')
print(f'Mesec sa najvecim ukupnim prihodom: {np.argmax(total_month) + 1}')
print(f'Prosecan prihod po kategoriji proizvoda: {np.mean(products, axis= 1)}')
print(f'Prosecan mesecni prihod svih kategorija: {np.mean(products, axis= 0)}')

# 5. Sistem beleži prosečne dnevne temperature tokom 15 dana. Neki podaci nedostaju ili nisu validni.
# Validna temperatura mora biti između -20 i 50 stepeni.
# Potrebno je:
# Identifikovati nedostajuće vrednosti.
# Identifikovati nevalidne temperature (vrednosti manje od -20 ili veće od 50).
# Pronaći indekse nevalidnih vrednosti.
# Izračunati broj nedostajućih i nevalidnih vrednosti.
# Izračunati procenat nevalidnih i nedostajućih zapisa zajedno.
# Kreirati novi niz koji sadrži samo validne temperature.
# Izračunati prosečnu temperaturu bez nedostajućih i nevalidnih vrednosti.

temps = np.array([-50.0, -40.0, np.nan, -20.0, -10.0, 0.0, 10.0, np.nan, 30.0, 40.0, 50.0, np.nan, 70.0, 80.0, 90.0])

missing_values = np.isnan(temps)
print(f'Nedostajuce vrednosti: {missing_values}')
print(f'Nevalidne temperature: {np.where((temps >= -20) & (temps <= 50), 'Valid', 'Invalid')}')
print(f'Indeksi nevalidinh vrednosti: {np.where((temps >= -20) & (temps <= 50))[0]}')

sum_not_valid = np.where((temps >= -20) & (temps <= 50), 0, 1).sum()
print(f'Ukupno broj nedostajucih i nevalidinh vrednosti: {sum_not_valid}')
print(f'Procenat nevalidinh i nedostajucih zapisa zajedno: {((sum_not_valid/len(temps)) * 100).round(2)}')

valid_temps = temps[(temps >= -20) & (temps <= 50)]

print(f'Prosecna temeperatura od validnih vrednosti: {np.mean(valid_temps).round(2)}')
