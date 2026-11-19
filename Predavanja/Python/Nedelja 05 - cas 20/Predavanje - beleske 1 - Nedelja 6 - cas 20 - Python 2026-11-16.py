%sql
CREATE VOLUME IF NOT EXISTS bootcamp.northern_star.prodavnica;

import pandas as pd

R = '/Volumes/bootcamp/northern_star/prodavnica/dostave.csv'

df = pd.read_csv(R)

print(df.head(3))
print(df.info())
print(df.shape)
print(df.describe())

# df.groupbu('kolona')  # primer kako se pise

df.groupby('city')
df.groupby('city')['delivery_fee'].mean()

df.groupby('city', as_index= False)['delivery_fee'].mean()  # ovde ovaj dodatak as_index= False se koristi ako nam umesto imena gradova (u nasem slucaju) ispise indexe, preko ovoe komande to gasimo

df.groupby('city')['delivery_fee'].mean().reset_index() # ovo je isto kao u gore iznad, samo umesto komande as_index= False koristimo metod reset_index()

df.groupby('courier')['delivery_fee'].sum()

df.groupby('courier')['delivery_fee'].count()   # count broji vrednosti koje nam ne nedostaju

df.groupby('courier')['delivery_fee'].max()

df.groupby('courier').agg(      # ovo agg() koristi vise funkcija agregacije
    broj_dostava = ('delivery_id', 'count'),    #  broj_dostava ovo je naziv nove kolone, unutar zagrade (kolona nad kojom hocemo nesto da radimo, drugi argument je naziv agregatne funkcije)
    ukupna_cena = ('delivery_fee', 'sum')       # ovo se zove imenovana agregacija, zato sto smo dali nazive novih kolona
)     

df.groupby('city')['distance_km'].agg(['min', 'max'])       # ovo se zove NEimenovana agregacija, zato sto nismo dali naziv novih kolona

# df.groupby(['kolona_1', 'kolona_2'])      # ovo je sintaksa za grupisanje po dve kolone

df.groupby(['city', 'courier'])['delivery_fee'].mean()  # ovo je primer za grupaciju po dve kolone, imamo za svaki gradi koliko koja kourirska sluzba ima delivery_fee

df.groupby(['city', 'courier']).agg(
    broj_dostava = ('delivery_id', 'count'),
    prosecna_cena = ('delivery_fee', 'mean'),
    ukupna_udaljenost = ('distance_km', 'sum')
)

zones = pd.DataFrame({'zone_id': [1, 2, 3, 4], 
                      'region': ['Jug', 'Centralna Srbija', 'Vojvodina', 'Centralna Srbija'],
                      'zone_name': ['Zona A', 'Zona B', 'Zona C', 'Zona D']
                    })

# Spajanje dva DataFrame-a
# df1.merge(df2, on= 'kolona', how= 'inner')    # izgled sintakse, on je kolona po kojoj povezujemo kolone, inner tip spajanja

merged = df.merge(
    zones,
    on= 'zone_id',
    how= 'inner'    # ako hocemo drugo spajanje upisemo left, right...
)

merged.head()

# left_on, right_on ovo je spajanje DataFrame-a kada nemam isti naziv kolona po kojim spajamo

zones2 = pd.DataFrame({'id': [1, 2, 3, 4], 
                      'region': ['Jug', 'Centralna Srbija', 'Vojvodina', 'Centralna Srbija'],
                      'zone_name': ['Zona A', 'Zona B', 'Zona C', 'Zona D']
                    })

merged2 = df.merge(
    zones2,
    left_on = 'zone_id',  # ovo je spajanje po koloni iz leve tabele to je nas df
    right_on = 'id',      # ovo je spajanje po koloni iz desne tabele koja se zove zones2
    how = 'left'
    )

merged2.head()
