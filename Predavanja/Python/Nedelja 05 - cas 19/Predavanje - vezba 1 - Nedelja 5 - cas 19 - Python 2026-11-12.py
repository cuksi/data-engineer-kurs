import pandas as pd
import os

path = '/Volumes/bootcamp/northern_star/raw_2025_26/'

# 1. Учитати matches_2025_26.parquet у DataFrame m и одговорити: колико има редова и колона, како се зову колоне и како изгледа првих пет редова?
# Output: (380, 17)

data = pd.read_parquet(path + 'matches_2025_26.parquet')

data.shape
# Resenje ukupno 380 redova i 17 kolona, nazivi i izgled
# match_id:int64
# season:object
# matchday:int64
# kickoff_ts:datetime64[us]
# original_kickoff_ts:datetime64[us]
# status:object
# home_team:object
# away_team:object
# home_goals:int64
# away_goals:int64
# home_goals_ht:int64
# away_goals_ht:int64
# stadium:object
# referee:object
# attendance:Int64
# weather:object
# match_report:object

data.head(5)
# Prvih 5 redova
# match_id	season	matchday	kickoff_ts	original_kickoff_ts	status	home_team	away_team	home_goals	away_goals	home_goals_ht	away_goals_ht	stadium	referee	attendance	weather	match_report
# 0	2526001	2025/26	1	2025-08-16 13:30:00	NaT	FT	RVA	STH	0	2	0	0	Crowsnest	Pieter de Vries	15812	Rain	Stormhaven FC won 2-0 away at Ravenscar Albion...
# 1	2526002	2025/26	1	2025-08-16 16:00:00	NaT	FT	NPM	IVU	2	1	2	0	Harbour Park	Ingrid Solberg	24865	Cloudy	Northport Mariners beat Ironvale United 2-1, a...
# 2	2526003	2025/26	1	2025-08-16 16:00:00	NaT	FT	BRU	KLT	1	1	0	1	Ridgeway Stadium	Marco Ferretti	11794	Rain	Brackenridge United and Kelda Town drew 1-1, a...
# 3	2526004	2025/26	1	2025-08-16 16:00:00	NaT	FT	GMW	HGA	1	1	1	1	Estuary Ground	James Whitlock	21120	Clear	Glenmouth Wanderers and Harrowgate Athletic dr...
# 4	2526005	2025/26	1	2025-08-16 18:30:00	NaT	FT	AFV	TBF	1	1	0	1	Vale Park	Aleksandar Ilić	14517	Rain	Ashford Vale and Thornbridge FC drew 1-1, a ga...

# 2. Помоћу info() и isna().sum() пронаћи које колоне имају празне вредности и колико

data = pd.read_parquet(path + 'matches_2025_26.parquet')
data.info()

data.isna().sum()
# Kolona original_kickoff_ts ima 372 Null vrednosti i kolona attendance ima 6 Null vrednosti

# 3. Учитати исте податке из matches_2025_26.csv и упоредити dtypes колона kickoff_ts, original_kickoff_ts и attendance са Parquet верзијом
# Затим CSV учитати поново са parse_dates=[...]
# Питање: зашто је attendance и даље float64, а у Parquet фајлу цео број?

data_parquet = pd.read_parquet(path + 'matches_2025_26.parquet', columns= ['kickoff_ts', 'original_kickoff_ts', 'attendance'])
data_csv = pd.read_csv(path + 'matches_2025_26.csv')

data_parquet.dtypes
data_csv.dtypes
# kickoff_ts => parquet(type: datetime64[us]), csv(type: object); original_kickoff_ts => parquet(type: datetime64[us]), csv(type: object); attendance => parquet(type: Int64), csv(type: float64)

data_csv2 = pd.read_csv(path + 'matches_2025_26.csv', parse_dates=['kickoff_ts', 'original_kickoff_ts'])
# attendance u csv-u je i dalje float64 zato sto imamo par Null vrednosti koje spadaju pod Not a Number (NaN), a u pandas NaN upada u float64

# 4. Помоћу os.path.getsize упоредити величину CSV и Parquet фајла са утакмицама
# Колико пута је CSV већи?

parquet_size = os.path.getsize(path + 'matches_2025_26.parquet')
csv_size = os.path.getsize(path + 'matches_2025_26.csv')

print(f"CSV file je veci {csv_size / parquet_size} puta od Parquet file-a")

# 5. Помоћу describe() одговорити: колико голова у просеку дају домаћини, а колико гости, и колика је највећа посета?

data = pd.read_parquet(path + 'matches_2025_26.parquet')

data.describe() # ovo je jedan nacin gde se sve izlista, ispod za svaku kolonu posebno

data['home_goals'].describe()   # Prosek golova kod kuce = 1.384211
data['away_goals'].describe()   # Prosek golova u gostima = 0.963158
data['attendance'].describe()   # Najveca poseta = 30419.0

data[['home_goals', 'away_goals', 'attendance']].describe().loc[["mean", "max"]] # ovo je za sve tri trazene kolone i samo mean i max

# 6. Помоћу value_counts() одговорити: какво време је било најчешће и која три судије су судила највише утакмица?

data = pd.read_parquet(path + 'matches_2025_26.parquet')
data['weather'].value_counts()
# Najcesce vreme je Cloudy sa 129 utakmica

data['referee'].value_counts().head(3)
# Troje sudija koji su najcesce sudili:
# referee
# Lukas Brenner       34
# Pieter de Vries     32
# Milica Jovanović    32

# 7. Приказати само колоне matchday, home_team, away_team, home_goals и away_goals за утакмицу са match_id 2526134
# Помоћ: m.loc[услов, листа_колона]

m = pd.read_parquet(path + 'matches_2025_26.parquet')
m.loc[m['match_id'] == 2526134, ['matchday', 'home_team', 'away_team', 'home_goals', 'away_goals']]

# 8. Филтрирање
# Додати колону total_goals и избројати утакмице са бар 5 голова
# Колико утакмица је NPM добио на свом терену?
# Колико утакмица је одиграно у децембру 2025? (помоћ: поређење са датумима '2025-12-01')
# *Издвој утакмице које су почеле пре 14 или од 19 часова, по киши или снегу, са посетом већом од 15.000, и прикажи их сортиране по посети. Пази на заграде и знакове & и |

m['total_goals'] = m['home_goals'] + m['away_goals']

len(m[m['total_goals'] >= 5])

len(m.query('total_goals >= 5')) # drugi nacin preko query()
# Ukupno 28 utakmica sa bar 5 golova

npm = m.loc[(m['home_team'] == 'NPM') & (m['home_goals'] > m['away_goals'])]
npm.head()
len(npm)
# NPM je ukupno dobio 20 utakmica na svom terenu

len(m[(m['kickoff_ts'] >= '2025-12-01') & (m['kickoff_ts'] < '2026-01-01')])
# Ukupno 20 utakmica u decembru 2025

multi = m.loc[((m['kickoff_ts'].dt.hour < 14) | ((m['kickoff_ts'].dt.hour > 19))) & (m['weather'].isin(['Rain', 'Snow'])) & (m['attendance'] > 15000)]
multi.head()
len(multi)
# Ukupno 9 utakmica

multi.sort_values('attendance', ascending= False)

# 9. Сортирање
# Пет утакмица са највећом посетом: match_id, тимови, стадион и посета
# Када је одиграна прва, а када последња утакмица сезоне?

five_games = m.nlargest(5, 'attendance')[['match_id', 'home_team']]

m['kickoff_ts'].min(), m['kickoff_ts'].max()
# prva odigrana 2025-08-16 13:30:00
# poslednja odigrana 2026-05-03 16:30:00

# 10. Додати колоне goal_diff (голови домаћина минус голови госта) и result са вредностима 'H', 'D' или 'A'
# Помоћ: почетна вредност па m.loc[услов, 'result'] = ...
# Колико је било домаћих победа, нерешених и гостујућих победа? Колико је голова пало у целој сезони?

data = pd.read_parquet(path + 'matches_2025_26.parquet')

data['goal_diff'] = data['home_goals'] - data['away_goals']

data['result'] = 'H'
data.loc[data['home_goals'] == data['away_goals'], 'result'] = 'D'
data.loc[data['home_goals'] < data['away_goals'], 'result'] = 'A'

data['result'].value_counts()

# Resenje
# result
# H    188
# A    104
# D     88
# Name: count, dtype: int64

# 11. Додати колону weekday са именом дана почетка утакмице (помоћ: .dt.day_name())
# Колико утакмица је играно којим даном?
# Питање: зашто постоји тачно 7 утакмица уторком? (погледати original_kickoff_ts)

data = pd.read_parquet(path + 'matches_2025_26.parquet')

data['weekday'] = data['kickoff_ts'].dt.day_name()

data['weekday'].value_counts()
# Resenje:
# weekday
# Saturday     242
# Sunday       101
# Wednesday     30
# Tuesday        7

data.loc[data['original_kickoff_ts'].notna()]
# Ovih 7 utakmica sto je odigrano utorkom su odlozene utakmice, ukupno ih ima 7 a 8 odlozena je odigrana u sredu

# 12. Пронаћи све померене утакмице (оне које имају original_kickoff_ts) и додати колону delay_days: за колико дана је утакмица померена
# Помоћ: разлика два датума па .dt.days
# Колико их има, и какво је време било на тим утакмицама?

data = pd.read_parquet(path + 'matches_2025_26.parquet')

data['delay_days'] = 0
data.loc[data['original_kickoff_ts'].notna(), 'delay_days'] = (data['kickoff_ts'] - data['original_kickoff_ts']).dt.days

data.loc[data['original_kickoff_ts'].notna()]           # ovo je prikaz utakmica koje su odlozene i za koliko dana sa novom kolonom delay_days
print(data.loc[data['original_kickoff_ts'].notna()])    # ovo je prikaz utakmica koje su odlozene i za koliko dana sa novom kolonom delay_days

data['weather'].loc[data['original_kickoff_ts'].notna()].value_counts()
# Ukupno ima 8 odlozenih utakmica i vreme na svih 8 utakmica je bilo Snow
