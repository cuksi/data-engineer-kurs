import pandas as pd

path = '/Volumes/bootcamp/northern_star/raw_2025_26/'
data = pd.read_parquet(path + 'matches_2025_26.parquet')

# 1. Analiza rezultata utakmica:
# 1.1. Pronaći sve utakmice u kojima su oba tima postigla bar po jedan gol.
data.loc[(data['home_goals'] > 0) & (data['away_goals'] > 0)]
# Rezultat ukupno 178 utakmica

# 1.2. Pronaći sve utakmice u kojima je domaćin pobedio sa tačno jednim golom razlike.
data.loc[(data['home_goals'] - data['away_goals']) == 1]
# Rezultat ukupno 105 utakmica

# 1.3. Koliko utakmica je završeno rezultatom 0:0?
data.loc[(data['home_goals'] == 0) & (data['away_goals'] == 0)]
len(data.loc[(data['home_goals'] == 0) & (data['away_goals'] == 0)])
# Rezultat ukupno 26 utakmica

# 1.4. Prikazati 10 utakmica sa najviše ukupno postignutih golova.
data['total_goals'] = data['home_goals'] + data['away_goals']
data.sort_values('total_goals', ascending= False).head(10)

# PRVI NACIN 2. ZADATKA
# 2. Analiza jednog tima
# Za tim po izboru: -> Westerfell Town - WFT
# 1.Prikazati sve utakmice u kojima je učestvovao.
data.loc[(data['home_team'] == 'WFT') | (data['away_team'] == 'WFT')]

# Resenje ukupno 38 utakmica odigrao tim

# 2.Koliko je puta pobedio, izgubio i odigrao nerešeno?
data['result'] = 'Draw'
data.loc[((data['home_goals'] > data['away_goals']) & (data['home_team'] == 'WFT')) | ((data['home_goals'] < data['away_goals']) & (data['away_team'] == 'WFT')), 'result'] = "Win"
data.loc[((data['home_goals'] < data['away_goals']) & (data['home_team'] == 'WFT')) | ((data['home_goals'] > data['away_goals']) & (data['away_team'] == 'WFT')), 'result'] = "Lost"
data.loc[((data['home_team'] == 'WFT') | (data['away_team'] == 'WFT')), 'result', ].value_counts()
# Resenje:
# result
# Win     13
# Draw    13
# Lost    12

# 3.Koliko je golova postigao kao domaćin, a koliko kao gost?
domacin = data.loc[data['home_team'] == 'WFT']
print(f'Ukupno postignutih golova kao domacin: {domacin['home_goals'].sum()}')
# Resenje 27 golova

gost = data.loc[data['away_team'] == 'WFT']
print(f'Ukupno postignutih golova kao gost: {gost['away_goals'].sum()}')
# Resenje 18 golova

# 4.Pronaći utakmicu u kojoj je postigao najviše golova.
if domacin['home_goals'].max() > gost['away_goals'].max():
    display(domacin.sort_values('home_goals', ascending= False).head(1))
elif domacin['home_goals'].max() < gost['away_goals'].max():
    display(gost.sort_values('away_goals', ascending= False).head(1))
else:
    print('Maksimalni broj golova na utakmici u kod kuce i u gostima je isti')
    display(domacin.sort_values('home_goals', ascending= False).head(1))
    display(gost.sort_values('away_goals', ascending= False).head(1))
    
# NAPOMENA DRUGI NACIN 2. ZADATKA DAJE ISTO RESENJE KAO PRVI NACIN IZNAD ISTOG ZADATKA. OVDE JE KORISTENA MASKA ALI NA KRAJU DAJE TACNO RESENJE UZ UPOZORENJE: SettingWithCopyWarning:
# 2. Analiza jednog tima
# Za tim po izboru: -> Westerfell Town - WFT
# 1.Prikazati sve utakmice u kojima je učestvovao.
all_games = data.loc[(data['home_team'] == 'WFT') | (data['away_team'] == 'WFT')]
all_games
# Resenje ukupno 38 utakmica odigrao tim

# 2.Koliko je puta pobedio, izgubio i odigrao nerešeno?
all_games['result'] = 'Draw'
all_games.loc[((all_games['home_goals'] > all_games['away_goals']) & (all_games['home_team'] == 'WFT')) | ((all_games['home_goals'] < all_games['away_goals']) & (all_games['away_team'] == 'WFT')), 'result'] = "Win"
all_games.loc[((all_games['home_goals'] < all_games['away_goals']) & (all_games['home_team'] == 'WFT')) | ((all_games['home_goals'] > all_games['away_goals']) & (all_games['away_team'] == 'WFT')), 'result'] = "Lost"
all_games['result'].value_counts()
# Resenje:
# result
# Win     13
# Draw    13
# Lost    12

# 3.Koliko je golova postigao kao domaćin, a koliko kao gost?
domacin = all_games.loc[all_games['home_team'] == 'WFT']
print(f'Ukupno postignutih golova kao domacin: {domacin['home_goals'].sum()}')
# Resenje 27 golova

gost = all_games.loc[all_games['away_team'] == 'WFT']
print(f'Ukupno postignutih golova kao gost: {gost['away_goals'].sum()}')
# Resenje 18 golova

# 4.Pronaći utakmicu u kojoj je postigao najviše golova.
if domacin['home_goals'].max() > gost['away_goals'].max():
    display(domacin.sort_values('home_goals', ascending= False).head(1))
elif domacin['home_goals'].max() < gost['away_goals'].max():
    display(gost.sort_values('away_goals', ascending= False).head(1))
else:
    print('Maksimalni broj golova na utakmici u kod kuce i u gostima je isti')
    display(domacin.sort_values('home_goals', ascending= False).head(1))
    display(gost.sort_values('away_goals', ascending= False).head(1))

# 3. Analiza stadiona
# 1.Prikazati sve različite stadione na kojima su odigrane utakmice.
data.loc[data['kickoff_ts'].notna(), 'stadium'].value_counts()

# 2.Pronaći stadion na kojem je odigrano najviše utakmica.
data.loc[data['kickoff_ts'].notna(), 'stadium'].max()
# Na svima je odigran jednak broj utakmica

# 3.Za svaki stadion izračunati prosečnu posećenost.
data.groupby('stadium')['attendance'].mean().round(2)

# 4.Prikazati pet stadiona sa najvećom prosečnom posećenošću.
data.groupby('stadium')['attendance'].mean().round(2).nlargest(5)
