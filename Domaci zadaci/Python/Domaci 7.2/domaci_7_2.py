# 1. Napisati program kojim se prevodi temperatura iz Celzijusove skale u Farenhajtovu skalu, ako je odgovarajuca formula oblika T[◦F] = T[◦C] · 1.80 + 32. 
# Na ulazu se unosi vrednost temperature u stepenima Celzijusa (realan broj) a ispisuje se vrednost temperature u stepenima Farenhajta.
def celzijus_u_farenhajt(temp):
    return temp * 1.8 + 32

print(f"30 stepeni po Celzijusu je {celzijus_u_farenhajt(30)} po Farenhajtu")

# 2. Napisati program koji za uneti redni broj dana u nedelji (od 1 do 7) ispisuje naziv tog dana (ponedeljak - nedelja). Ukoliko je unet broj koji nije izmedju 1 i 7, ispisati Pogresan unos.
def dan_u_nedelji(dan):
    if dan == 1:
        return print("Ponedeljak")
    elif dan == 2:
        return print("Utorak")
    elif dan == 3:
        return print("Sreda")
    elif dan == 4:
        return print("Cetvrtak")
    elif dan == 5:
        return print("Petak")
    elif dan == 6:
        return print("Subota")
    elif dan == 7:
        return print("Nedelja")
    
    return print("Pogresan unos.")

dan_u_nedelji(1)    # test
dan_u_nedelji(4)    # test
dan_u_nedelji(8)    # test

# 3. Napisati program koji racuna najveci negativni element u listi.
lista_negativni = [-3, -5, -1, -7, 16]  # za test
def negativni(lista):
    target = lista[0]
    for i in lista:
        if target < i and i < 0:
            target = i
    return target

print(negativni(lista_negativni))    # test

# 4. Napisati program koji racuna srednju vrednost i standardnu devijaciju liste razlomljenih brojeva. Srednja vrednost i standardna devijacija racunaju se po formulama
from math import sqrt

lista_srednji_broj = [1, 2, 3, 4, 5, 6, 7, 8]   # za test
def srednja_vrednost(lista):
    brojilac = 0
    imenilac = len(lista)
    for i in range(imenilac + 1):
        brojilac += i
    return brojilac / imenilac

def standardna_devijacija_liste(lista):
    borjilac_suma = 0
    imenilac_razlika = len(lista) - 1
    for i in lista:
        borjilac_suma += (i - srednja_vrednost(lista))**2
    
    return sqrt(borjilac_suma / imenilac_razlika)

print(srednja_vrednost(lista_srednji_broj))    # test
print(standardna_devijacija_liste(lista_srednji_broj))    # test

# 5. Napisati program koji racuna broj parnih elemenata date liste
test = [1, 2, 3, 4, 5, 6, 7]    # za test

def parni(lista_parni):
    count = 0
    for i in lista_parni:
        if i % 2 == 0:
            count += 1
    
    return count

print(parni(test))    # test

# 6. Napisati program koji racuna sume elemenata liste celih brojeva koji su deljivi sa 2 odnosno sa 3. Dve sume jedna za deljive sa dva a druge za deljive sa tri
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]    # za test

def sume(lista):
    suma2 = 0
    suma3 = 0
    for i in lista:
        if i % 2 == 0:
            suma2 += i
        elif i % 3 == 0:
            suma3 += i
    return (suma2, suma3)

print(sume(lista3))    # test

# 7. Napisati program koji za dati niz karaktera (string) koji se sastoji samo od cifara 0-9 racuna koliko puta se javlja svaka cifra.
lista4 = "0122333444456677788889"   # za test

def brojac_brojeva(lista):
    result = []
    kontrolna_lista = []
    for i in lista:
        ukupan_broj = lista.count(i)
        if i not in kontrolna_lista:
            kontrolna_lista.append(i)
            result.append(f"Broj {i} se ponavlja {ukupan_broj} puta")
    return result

print(brojac_brojeva(lista4))    # test

## Drugi nacin da cuva u zaseban tuple
def brojac_brojeva2(lista):
    result = []
    kontrolna_lista = []
    for i in lista:
        ukupan_broj = lista.count(i)
        if i not in kontrolna_lista:
            kontrolna_lista.append(i)
            result.append((i, ukupan_broj))
    return result

print(brojac_brojeva2(lista4))    # test

# 8. Napisati program koji racuna:
# 8.1 Broj krajnjih pozitivnih elemenata liste. Ako poslednji element nije pozitivan, rezultat je 0.
# 8.2 Maksimalni broj uzastopnih jednakih elemenata liste.
# 8.3 Broj razlicitih elemenata liste.

lista_negativna = [-1, -2, 3, 4, 4, 4, -5]  # za test
lista_pozitivna = [1, -2, -3, 4, -4, -4, 5, 6, 6]   # za test
lista_pozitivna2 = [1, -2, -3, 4, -4, -4, 5, 6, 6, 7, 7, 7, 7, 7, 8]    # za test

def program_broj_krajnjih(lista):
    zadnji_element = lista[-1]
    broj_pozitivnih_na_kraju = 0
    if zadnji_element > 0:
        for i in reversed(lista):
            if i > 0:
                broj_pozitivnih_na_kraju += 1
            else:
                break
    return broj_pozitivnih_na_kraju

def max_uzastopni(lista):
    maks = 0
    count = 0
    for i in lista:
        temp_maks = 0
        for j in lista[count:len(lista)+1]:
            if i == j:
                temp_maks += 1
                if temp_maks > maks:
                    maks = temp_maks
            elif i !=j:
                temp_maks = 0
        count += 1
    return maks

def razliciti_elementi(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    return len(result)

def finalni_program(lista):
    krajnji = program_broj_krajnjih(lista)
    if krajnji <= 0:
        return 0
    else:
        uzastopni = max_uzastopni(lista)
        razliciti = razliciti_elementi(lista)
        return (f"Broj krajnjih pozitivnih elemenata: {krajnji}; Maksimalni broj uzastopnih: {uzastopni} Broj razlicitih elemenata liste: {razliciti}")

print(finalni_program(lista_negativna))    # test
print(finalni_program(lista_pozitivna))    # test
print(finalni_program(lista_pozitivna2))    # test