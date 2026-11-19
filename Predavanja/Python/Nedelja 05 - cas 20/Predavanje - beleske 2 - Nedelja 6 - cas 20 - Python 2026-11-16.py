prices = [100, 200, 300, 400, 500]

new_prices = []
for price in prices:
    new_prices.append(price * 1.10)

print(new_prices)

import numpy as np

prices = np.array([100, 200, 300, 400, 500])

new_prices = prices * 1.10  # ovaj postupak se zove vektorizacija

print(new_prices)

# try:                        # ovo je nacin kako se pise da uvezemo jedan modul a ako ga nema da uveze drugi
#     import cupy as xp       # cupy je isto sto i numpy, sa tim sto numpy se izvrsava na procesoru CPU i pisan je u C, a cupy je pisan u Python-u i izvrsava se na grafickoj karti GPU
# except:                         
#     import numpy as xp

list_a = [1, 2, 3, 4, 5]

a = np.array(list_a, dtype= float)  # ovo je nacin kako da se odredi tip promenljive iz liste, Numpy sam dodeljuje tip ali ovako mozemo sami da ga definisemo

lista1 = [1, 2, 3]
lsita2 = [4, 5, 6]

b = np.array([lista1, lsita2])
print(b)

print(f'Broj dimenzija: {b.ndim}')   # vraca broj dimenzija
print(f'Broj elemenata: {b.size}')   # broj elemenata
print(f'Broj redova i kolona: {b.shape}')   # broj redova i kolona

list_a = [1, 2, 3, 4, 5]
a = np.array(list_a)
print(a.shape)

c = np.array([[1], [2], [3]])
print(c.shape)

d = np.array([[1, 2, 3]])
print(d.shape)

a = np.arange(0, 16).reshape((2, 2, 4)) # ovaj reshape vraca novi niz zato sto ovde kreiramo novi niz pomocu reshape-a
print(a)
print(a.shape)

# ovaj ispod reshape ne vraca novi niz jer koirstimo postojeci da ga preraspodelimo
a2 = a.reshape((16, 1))
a3 = a.reshape((4, 1, 4))
a4 = a.reshape((1, 8, -1))  # -1 automatski racuna 3 dimenziju, ako nismo sigurni koliko mozemo
a5 = a.reshape((-1, 8, 1))  # moze -1 i na prvom mestu ali ne moze u isto vreme na dva mesto, ovo ne moze (-1, 8, -1)

print(a2)
print(a3)
print(a4)
print(a5)

a1 = np.zeros((2, 3))   # ovo je kako se pravi n niz sa nulama
print(a1)

a2 = np.ones((2, 4))    # ovo je kako se pravi n niz sa jedinicama
print(a2)

a3 = np.empty((2, 3))   # ovo je prazan niz, ciji ce elementi biti oni iz memorije koji su koristeni, nama su sad nule jer smo ih koristili. Ali nekad mogu da budu cudni brojevi, jer dobijamo bajtove koji su zateceni u memoriji
print(a3)               # ovo je jeftinija operacija (sto se tice procesora) nego da popunjavamo sa nulama i jedinicama, samo cita iz memorije bez upisivanja

matrix = np.arange(0, 16).reshape((4, 4))

print(matrix)
print(matrix[2][0]) # jedan nacin preko indeksa da dobijemo vrednost iz matrice
print(matrix[2, 0]) # drugi nacin preko indeksa da dobijemo vrednost iz matrice

print(matrix[2:4, 0:3]) # slicing iz Python-a

print(matrix[2:, :3])   # ovo nije isto kao ovo ispod, ovde se prvo odnosi na redove 2: a onda na kolone :3
print(matrix[2:][:3])   # a ovde se gleda uzima iz cele matrice 2:, pa opet iz cele matrice ali sad od one od dobijene :3, racuna se zasebno zato sto je u odvojenim zagradama []

# lista[::2]    # ovde je uzeto od pocetka do kraja ali korak je 2

m = np.arange(0, 6).reshape((2, 3))
a1 = np.array([[-2, 0, 10], [0, 5, 3]])

print(m)
print(a1)

print(m + a1)   # sabiranje po komponentama

print(m * a1)   # mnozenje po komponentama

print(m + 2)    # dodaje dva po komponentama

a1 = np.arange(0, 4).reshape(4, 1)
b1 = np.arange(0, 16).reshape(4,4)

print(a1)
print(b1)

print(a1 + b1)  # ovo moze da se sabere zato sto je jedna dimenzija zajednicka, sabira kolonu a1 sa svakom kolonom b1. Ovo moze zato sto je (4,1) u a1 a da je (4,2) ne bi moglo da se sabere bila bi greska
                # moze da se izvrsi matematicka operacija i ako su razlicitih dimenzija ali jedna mora da bude jedinica kod jednog


# ovo ispod se odnosi na broadcasting i to se koristi za formiranje dimenzija iz postojecih matrica
# (5, 2, 3) (5, 1, 3)   # moze
# (5, 2, 3) (5, 7, 3)   # ne moze

# (3, 1, 5) (1, 7, 5) # moze -> dobice se (3, 7, 5)


# ovo je ispod kako se vrsi matricno mnozenje:
# mathmul() # preko ove funkcije
# a @ b # ili pomocu @

m = np.arange(0, 6).reshape((2, 3))
print('m=\n{}'.format(m))
print('xp.sum(m) = {}'.format(np.sum(m)))
print('xp.sum(m, axis = 0) = {}'.format(np.sum(m, axis= 0)))    # sabira kolone
print('xp.sum(m, axis = 1, keepdims = True) =\n{}'.format(np.sum(m, axis= 1, keepdims= True)))  # sabira redove, ovo keepdims= True cuva sumu u svom redu, inace ih vrati u istom redu

# np.isnan()
# np.nanmean()  # ovo izbegava NaN vrednosti, ovo se koristi kada nismo sigurni jel imamo NaN vrednosti
# np.mean() # a ovo ce vratiti NaN ako je jedna vrednost NaN

data = np.array([10, 20, np.nan, 40])

print(np.isnan(data))
print(np.nanmean(data))

a = np.array([10, 20, 30, 40, 50])

indeksi = np.where(a > 20)  # ovo je kako se postavlja logicki uslov, dobicemo indekse gde je a vece od 20, INDEKSE a ne vrednosti

print(a)
print(indeksi)

print(a[np.where(a > 20)])  # ovo ce da vrati elemente gde je ispunjen uslov a ne indekse
print(a[a > 20])  # ovo je isto gore samo krace (ovo je direktno logicko indeksiranje)

# np.where(uslov, vrednost_tacno, vrednost_netacno) # sintaksa za where sa 3 elementa
rezultat = np.where(a > 20, 1, 0)   # ovo je primer za ovo gore sa tri elementa, kada je tacno vratice 1 a kada je netacno vratice 0 i bice prikazano u matrici
print(rezultat)

rezultat = np.where(a > 20, 'Jeste', 'Nije')   # moze i nesto drugo umesto 1 i 0, na primer kao ovde string
print(rezultat)
