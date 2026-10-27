USE bootcamp.northern_star;

-- 1 zadatak: Za sezonu 2024/25 prikažite igrače i ukupan broj golova koje su postigli. Prikažite samo igrače koji su postigli bar jedan gol.
--            Pomoću DENSE_RANK() rangirajte igrače prema ukupnom broju golova, od najvećeg ka najmanjem. Igrači sa istim brojem golova treba da imaju isti rang.
WITH golovi AS(
    SELECT
    me.player_id, 
    p.first_name AS ime_igraca,
    p.last_name AS prezime_igraca,
    COUNT(me.event_type) AS total_goals
FROM match_events me
JOIN matches m ON m.match_id = me.match_id
JOIN players p ON p.player_id = me.player_id
WHERE me.event_type IN ('goal', 'penalty_goal') AND m.season = '2024/25'
GROUP BY me.player_id, p.first_name, p.last_name
)
SELECT
    ime_igraca, prezime_igraca, total_goals,
    DENSE_RANK() OVER(ORDER BY total_goals DESC) AS rank_igraca
FROM golovi g
ORDER BY rank_igraca;   -- ovaj ORDER BY garantuje redosled sortiranja a onaj ORDER BY iz zagrade samo po cemu da rangira tj. po cemu da dodeljuje vrednost za rang

-- 2 zadatak: Za sezonu 2024/25 prikažite tri igrača sa najviše postignutih golova za svaki klub.
--            Prikažite naziv kluba, ime i prezime igrača i broj postignutih golova. Pomoću ROW_NUMBER() odredite redosled igrača unutar svakog kluba, od najvećeg ka najmanjem broju golova.
WITH golovi_po_klubu AS (
SELECT
    me.player_id, 
    t.team_name AS klub,
    p.first_name AS ime_igraca,
    p.last_name AS prezime_igraca,
    COUNT(me.event_type) AS total_goals
FROM match_events me
JOIN matches m ON m.match_id = me.match_id
JOIN players p ON p.player_id = me.player_id
JOIN teams t ON t.team_id = me.team_id
WHERE me.event_type IN ('goal', 'penalty_goal') AND season = '2024/25'
GROUP BY me.player_id,t.team_name, ime_igraca, prezime_igraca
)
SELECT
    klub, ime_igraca, prezime_igraca, total_goals,
    ROW_NUMBER() OVER(PARTITION BY klub ORDER BY total_goals DESC) AS rn
FROM golovi_po_klubu
QUALIFY rn <= 3;    -- da nema ovog uslova dao bi sve igrace, ali ovde ne moze WHERE more qualify zato sto koristimo ROW NUMBER, Zato sto se WHERE IZVRSAVA PRE PROZORSKE FUNKCIJE

-- 3 zadatak: Za sezonu 2024/25 prikažite sve utakmice svakog kluba, broj golova koje je klub postigao i broj golova koje je postigao u svojoj prethodnoj utakmici.
--            Pomoću LAG() pronađite broj golova iz prethodne utakmice. Izračunajte i razliku između broja golova na tekućoj i prethodnoj utakmici. Rezultate sortirajte po nazivu kluba i datumu utakmice.
WITH utakmice AS (
SELECT
    m.match_id AS mec_id,
    m.kickoff_ts AS datum,
    m.home_team_id AS team_id,
    th.team_name AS klub,
    'domacin' AS strana,
    m.home_goals AS golovi
FROM matches m
JOIN teams th ON th.team_id = m.home_team_id
WHERE season = '2024/25'
UNION ALL
SELECT
    m.match_id AS mec_id,
    m.kickoff_ts AS datum,
    m.away_team_id AS team_id,
    ta.team_name AS klub,
    'gost' AS strana,
    m.away_goals AS golovi
FROM matches m
JOIN teams ta ON ta.team_id = m.away_team_id
WHERE season = '2024/25'
)
SELECT
    DATE(datum) AS datum, klub,
    golovi AS postignuti_golovi,
    LAG(golovi) OVER(PARTITION BY team_id ORDER BY datum) AS golovi_prethodni_mec,
    golovi - golovi_prethodni_mec AS razlika
FROM utakmice
ORDER BY klub, datum;