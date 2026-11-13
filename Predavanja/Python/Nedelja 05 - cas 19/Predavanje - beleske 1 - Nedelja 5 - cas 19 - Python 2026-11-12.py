# %sql
# CREATE VOLUME IF NOT EXISTS bootcamp.northern_star.raw_2025_26;

# Ovo je komentovan block da se ne bi pokretao svaki put ili slucajno pa da imamo duplikate
# import zipfile
# zipfile.ZipFile('/Volumes/bootcamp/northern_star/raw_2025_26/nsl_2025_26.zip') \
#     .extractall('/Volumes/bootcamp/northern_star/raw_2025_26/')

import pandas as pd
R = '/Volumes/bootcamp/northern_star/raw_2025_26/'

m = pd.read_parquet(R + 'matches_2025_26.parquet')

# m.shape
# m.columns
# m.dtypes
# m.head(2)
# m.info()
# m.isna().sum()
# m.describe()
# m['weather'].value_counts()
m['weather'].nunique()

# MOJE BELESKE SA CASA

# m.shape # daje ukupnio broj redova, i kolona (380,17)

# m.columns # daje kolone

# m.dtypes # daje tipove podataka

# m.head()    #daje prvih 5 redova, NaT skracenica od Not a Time
# m.head(2)   # ovde smo zadali da vrati samo 2 reda

# m.info()    # informacije o podacima

# m.isna()      # ovo je da vidimo koliko nam podataka fali, gde je True tu je Null vrednost a gde je False to ima vrednost

# m.isna().sum()  # ovo nam daje pregled koliko u kojoj koloni nam fali podataka tj koliko Null vrednosti imamo

# m.describe()    # daje opis kolona

# m.iloc[0, 6 : 8]  # ovo je da citamo iz DataFrame red i zeljene kolone (prvi red, od 6 do 8 kolone)
# m.iloc[:, 6 : 8]  # ovo je da citamo iz DataFrame red i zeljene kolone (sve redove, od 6 do 8 kolone)

# m['weather']    #daje pregled svih vremena

# m['weather'].value_counts() #daje broj koliko kojih ima

# m['weather'].nunique()  #daje jedinstvena vremena

# len(m['weather'].nunique()) # koliko ukupno ima razlicitih, broj

# m.[['kickoff_ts']].dtypes   # mora dupla zagrada [[]] inace nam nece vratiti lepo 

# # Pandas za sta nije siguran koji je data type on pise object sto je u stvari string
# # Pandas Nan = Not a Number kada ima tj. kada fali vrednost on je nekad pise kao float posto mu NaN spada u float
# # Pandas ako ima razlicit type za iste kolone kad ih spajamo moze da pravi problem. Recimo attendace je jednom int a drugi put float (zato sto fale vrednosti) mogao bi biti problem da treba da spojimo te dve tabele

m = pd.read_parquet(R + 'matches_2025_26.parquet')
c = pd.read_csv(R + 'matches_2025_26.csv', parse_dates=['kickoff_ts', 'original_kickoff_ts'])

print(m[['kickoff_ts', 'original_kickoff_ts', 'attendance', 'away_goals']].dtypes)
print(c[['kickoff_ts', 'original_kickoff_ts', 'attendance', 'away_goals']].dtypes)

import os

csv_size = os.path.getsize(R + 'matches_2025_26.csv')
parquet_size = os.path.getsize(R + 'matches_2025_26.parquet')

csv_size / parquet_size

s = pd.read_parquet(R + 'player_match_stats')   # ovo je da ucita sve parquet fajlove iz glavnog foldera tj. sve sub foldere
s.shape # da vidimo koliko redova i koliko kolona (redovi, kolone)

m1 = pd.read_parquet(R + 'player_match_stats', filters=[('matchday','=',1)])    # ovde i ako je ime foldera mora da se pise kao tuple, levo od jednako prvi clan, drugi clan =, a treci clan desno od jednako
m1.shape
m1.dtypes

m2 = pd.read_parquet(R + 'player_match_stats', columns= ['player_id', 'minutes_played', 'rating'])  # ovde smo izabrali odredjene kolone i samo se one vracaju
m2.shape

m = pd.read_parquet(R + 'matches_2025_26.parquet')

m['referee'] #Series
m[['referee', 'attendance']]    # ovde duple zagrade jer su dve kolone ovo je DataFrame

m.loc[m['match_id'] == 2526001] # ovo izvlaci sve kolone za ovaj match_id koji smo zadali

m.loc[m['match_id'] == 2526001, ['home_goals', 'away_goals']]   # ovo prikazuje samo ove dve kolone koje smo zadali 'home_goals', 'away_goals' za ovaj trazeni match_id

# Filtering
m.loc[m['weather'] == 'Snow']
len(m.loc[m['weather'] == 'Snow'])  # ovo daje koliko ih je

m.loc[m['home_team'].isin(['NPM', 'IVU'])]
len(m.loc[m['home_team'].isin(['NPM', 'IVU'])])

m.loc[m['matchday'].between(1, 5)]
len(m.loc[m['matchday'].between(1, 5)])

m.loc[(m['weather'] == 'Snow') & (m['attendance'] > 20000)] # and
m.loc[(m['weather'] == 'Snow') | (m['attendance'] > 20000)] # or

m.query("weather == 'Snow' and attendance > 20000") # adrugi nacin ispisa

m.sort_values('attendance', ascending= False)   # sortiranje po jednoj koloni

m.sort_values(['matchday', 'kickoff_ts'], ascending= False) # sortiranje po vise kolona

m.nlargest(5, 'attendance') # 5 najvecih

m['month'] = m['kickoff_ts'].dt.month   # ovako pravimo novu kolonu month pomcu dt.month. dt je datetime skraceno sa pod funkcijama unutar pandasa

m['month'] # ovo su sve utakmice kog su meseca igrane
m['month'].value_counts()   # koliko je koga meseca odigrano utakmica

m['crowd'] = 'normal'   # nova kolona koju smo kreirali ce za sve redove imati Normal
m.loc[m['attendance'] >= 20000, 'crowd'] = 'large'  # ovde smo promenili gde je ispunjen uslov da promeni Large

m['crowd']

m['home_team'].str.contains('N')

# Poceli sa vodjstvom a ispustili prednost
m['ht_state'] = 'tie'
m.loc[m['home_goals_ht'] > m['away_goals_ht'], 'ht_state'] = 'home lead'
m.loc[m['home_goals_ht'] < m['away_goals_ht'], 'ht_state'] = 'away lead'
m['ht_state'].value_counts()

slipped_home = m.loc[(m['ht_state'] == 'home lead') & (m['away_goals'] >= m['home_goals'])]  # moraju zagrade kada koristimo & zato sto ima prednost u odnosu na ==
slipped_away = m.loc[(m['ht_state'] == 'home lead') & (m['away_goals'] <= m['home_goals'])]
len(slipped_home)    # koliko utakmica ispunjava gornji uslov, slipped je DataFrame vrsta object-a, DataFrame je skup vrednosti
len(slipped_away) 

(slipped_home['home_goals'] == slipped_home['away_goals']).sum()    # ovde je Series je jedna kolona unutar DataFrames boolean vrednosti

# Zimske utakmice koje su igrane uvece
# Meseci 12 1 2
# Uvece 19+

# winter_evening = m.loc[((m['kickoff_ts'].dt.month.isin([12, 1, 2])) & (m['kickoff_ts'].dt.hour >= 19))]   # ovde se koristi m.loc pa nije uslov nego vraca vrednosti

# len(winter_evening)

winter_evening = ((m['kickoff_ts'].dt.month.isin([12, 1, 2])) & (m['kickoff_ts'].dt.hour >= 19))    # ovde je winter_evening dat kao uslov i ne vraca vrednosti zato sto je samo uslov

m.loc[winter_evening, 'attendance'].mean().round(2)

m.loc[~winter_evening, 'attendance'].mean().round() # ~ tilda daje obrnuto od onog prethodnog
