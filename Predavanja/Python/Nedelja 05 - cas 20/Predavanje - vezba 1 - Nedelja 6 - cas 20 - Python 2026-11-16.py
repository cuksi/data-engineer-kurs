import pandas as pd

path = '/Volumes/bootcamp/northern_star/prodavnica/dostave.csv'

df = pd.read_csv(path)

zones = pd.DataFrame({'zone_id': [1, 2, 3, 4], 
                      'region': ['Jug', 'Centralna Srbija', 'Vojvodina', 'Centralna Srbija'],
                      'zone_name': ['Zona A', 'Zona B', 'Zona C', 'Zona D']
                    })

# # Zadatak 1 – Analiza dostava po gradu
# Izračunati prosečnu cenu dostave za svaki grad.
# Rezultat treba da sadrži:
# - grad;
# - prosečnu cenu dostave.
# Sortirati rezultat opadajuće prema prosečnoj ceni.

df.groupby('city')['delivery_fee'].mean().sort_values(ascending= False)

# Zadatak 2 – Analiza kurirskih službi
# Za svaku kurirsku službu izračunati:
# 1) Broj obavljenih dostava.
# 2) Ukupnu cenu svih dostava.
# 3) Prosečnu cenu dostave.
# 4) Prosečnu udaljenost dostave.
# Rezultat treba da bude jedan DataFrame sa odgovarajućim nazivima kolona.

# df.head()

df.groupby('courier').agg(
    broj_obavljenih_dostava = ('delivery_id', 'count'),
    ukupna_cena_dostave = ('delivery_fee', 'sum'),
    prosecna_cena_dostave = ('delivery_fee', 'mean'),
    prosecna_udaljenost_dostave = ('distance_km', 'mean')
).round(2)

# Zadatak 3 – Gradovi i kurirske službe
# Za svaku kombinaciju grada i kurirske službe izračunati:
# - broj dostava;
# - minimalnu cenu dostave;
# - maksimalnu cenu dostave;
# - prosečnu cenu dostave.
# Sortirati rezultate po gradu, a zatim po prosečnoj ceni dostave opadajuće.

result = df.groupby(['city', 'courier']).agg(
    broj_dostava = ('delivery_fee', 'count'),
    min_cena = ('delivery_fee', 'min'),
    max_cena = ('delivery_fee', 'max'),
    prosecna_cena = ('delivery_fee', 'mean')
    )

result = result.sort_values(
    by = ['city', 'prosecna_cena'],
    ascending = [True, False]
)

result

# Zadatak 4 – Povezivanje sa šifarnikom zona
# Povezati tabelu dostava sa šifarnikom zona.
# Koristiti left spajanje.
# Rezultat treba da sadrži sve kolone iz obe tabele.

merge = df.merge(
    zones,
    on= 'zone_id',
    how= 'left'
)

merge.head()

# Zadatak 5 – Analiza dostava po regionima
# Povezati tabelu dostava sa šifarnikom zona.
# Zatim, za svaki region izračunati:
# 1) Broj dostava.
# 2) Prosečnu cenu dostave.
# 3) Ukupnu cenu svih dostava.
# 4) Prosečnu udaljenost dostave.
# Rezultat treba da bude jedan DataFrame.

merge.groupby('region').agg(
    broj_dostava = ('delivery_id', 'count'),
    prosecna_cena_dostave = ('delivery_fee', 'mean'),
    ukupna_cena_svih_dostava = ('delivery_fee', 'sum'),
    prosecna_udaljenost_dostave = ('distance_km', 'mean')
). round(2)

#  6. Završni zadatak – Analiza kurirskih službi po regionima
# Koristeći tabelu dostava i šifarnik zona:
# 1. Povezati tabele pomoću `merge()`.
# 2. Grupisati podatke po regionu i kurirskoj službi.
# 3. Za svaku kombinaciju izračunati:
#    - broj dostava;
#    - ukupnu cenu dostava;
#    - prosečnu cenu dostave;
#    - maksimalnu udaljenost.
# 4. Sortirati rezultate po regionu, a zatim po ukupnoj ceni opadajuće.
# Rezultat treba da bude jedan DataFrame.

merge_2 = df.merge(
    zones,
    on= 'zone_id',
    how= 'left'
)

merge_2.head()

result = merge_2.groupby(['region', 'courier']).agg(
    broj_dostava = ('delivery_id', 'count'),
    ukupna_cena_dostave = ('delivery_fee', 'sum'),
    prosecna_cena_dostave = ('delivery_fee', 'mean'),
    maksimalna_udaljenost = ('distance_km', 'max')
).round(2)

result.sort_values(
    by= ['region', 'ukupna_cena_dostave'],
    ascending= [True, False]
)

result
