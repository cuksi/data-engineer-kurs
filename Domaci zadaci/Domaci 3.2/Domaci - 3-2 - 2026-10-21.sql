USE bootcamp.northern_star;

--=================================OSNOVNI NIVO=================================--

-- 1 zadatak: Prikažite naziv svakog kluba i naziv stadiona na kojem igra domaće utakmice.
SELECT
    t.team_name,
    COALESCE(s.stadium_name, 'Nema stadion')
FROM teams t
LEFT JOIN stadiums s ON s.stadium_id = t.stadium_id;
-- Harbor City FC nema stadion, u polju stadium_id je NULL tj. nema upisan stadion.

--2 zadatk: Prikažite ime i prezime igrača i naziv kluba za koji je igrao u sezoni 2024/25. Uklonite duplikate iz rezultata.
SELECT
    DISTINCT p.player_id, p.first_name, p.last_name, t.team_name
FROM players p
JOIN player_match_stats pms ON pms.player_id = p.player_id
JOIN teams t ON t.team_id = pms.team_id
JOIN matches m ON m.match_id = pms.match_id 
WHERE m.season = '2024/25'
ORDER BY p.player_id;
-- Rezultat 582, postoje igraci koji su menjali klub u toku sezone oni su zadrzani

-- 3 zadatak:Prikažite datum odigravanja utakmice, naziv stadiona i broj gledalaca za sve utakmice u sezoni 2024/25.
SELECT
 DATE(m.kickoff_ts) AS datum,
  s.stadium_name AS naziv_stadiona,
  COALESCE(CAST(m.attendance AS STRING), 'NEMA PODATKA') AS posecenost
FROM matches m
JOIN stadiums s ON s.stadium_id = m.stadium_id
WHERE m.season = '2024/25';
-- Ukupno 380 rezultata

--=================================SREDNJI NIVO=================================--

-- 1 zadatak: Prikažite sve utakmice za koje nije evidentiran broj gledalaca. Prikažite datum, domaći klub i gostujući klub.
SELECT
    DATE(m.kickoff_ts) AS datum,
    t_domaci.team_name AS domaci_klub,
    t_gosti.team_name AS gostujuci_klub
FROM matches m
JOIN teams t_domaci ON t_domaci.team_id = m.home_team_id
JOIN teams t_gosti ON t_gosti.team_id = m.away_team_id
WHERE m.attendance IS NULL
ORDER BY m.kickoff_ts;
-- Ukupno 17 rezultata

-- 2 zadatak: Pronađite stadione na kojima nije odigrana ni jedna utakmica u sezoni 2024/25.
SELECT
    s.stadium_name
FROM stadiums s
LEFT JOIN matches m ON m.stadium_id = s.stadium_id AND m.season = '2024/25'
WHERE m.match_id IS NULL;
-- Rezultat 1 stadion -> Fairhaven Lane

-- 3 zadatak: Za svaki klub izračunajte ukupan broj žutih kartona koje su dobili njegovi igrači u sezoni 2024/25. Rezultat sortirajte opadajuće prema broju kartona
-- yellow_card ; second_yellow
SELECT
    t.team_name,
    SUM(
        CASE WHEN me.event_type IN ('yellow_card', 'second_yellow') THEN 1 
             ELSE 0 END
    ) AS ukupan_broj_zutih_kartona
FROM teams t
JOIN match_events me ON me.team_id = t.team_id
JOIN matches m ON m.match_id = me.match_id
WHERE m.season = '2024/25'
GROUP BY t.team_name
ORDER BY ukupan_broj_zutih_kartona DESC;

--=================================NAPREDNI NIVO=================================--

-- zadatak 1: Pronađite pet igrača sa najvećim brojem asistencija u sezoni 2024/25. Prikažite ime igrača i broj asistencija.
SELECT
    p.first_name, p.last_name,
    COUNT(*) AS broj_asistencija
FROM match_events me
JOIN players p ON p.player_id = me.related_player_id
JOIN matches m ON m.match_id = me.match_id
WHERE m.season = '2024/25' AND me.event_type = 'goal'
GROUP BY p.first_name, p.last_name
ORDER BY broj_asistencija DESC
LIMIT 5;
-- Rezultat:
-- first_name	last_name	broj_asistencija
-- Oliver	    Harrison	14041
-- Joe	        Barnes	    12730
-- Elliot	    Harrison	12196
-- Curtis	    Barnes	    11579
-- Théo	        Laurent	    11286

-- 2 zadatak: Pronađite tri igrača sa najvećim ukupnim brojem odigranih minuta u sezoni 2024/25. Prikažite ime igrača, klub i ukupan broj minuta.
SELECT
    p.first_name, p.last_name,
    t.team_name AS naziv_kluba,
    SUM(pms.minutes_played) AS ukupno_minuta
FROM player_match_stats pms
JOIN players p ON p.player_id = pms.player_id
JOIN matches m ON m.match_id = pms.match_id
JOIN teams t ON t.team_id = pms.team_id
WHERE m.season = '2024/25'
GROUP BY p.first_name, p.last_name, naziv_kluba
ORDER BY ukupno_minuta DESC;
-- Resenje prva cetri igraca imaju istu minutazu
-- first_name	last_name	naziv_kluba	            ukupno_minuta
-- Ibrahima	    Ndiaye	    Ashford Rovers	        3240
-- Jonas	    Müller	    Westmere Town	        3240
-- Morgan	    Nolan	    Redcliffe Athletic	    3240
-- Aaron	    Lowe	    Kingsbridge City	    3240

-- 3 zadatak: Za svaku sezonu prikažite broj isključenja po klubovima. Računajte događaje red_card i second_yellow. Uključite samo klubove koji su imali najmanje jedno isključenje.
SELECT
    m.season, t.team_name,
    SUM(
        CASE WHEN me.event_type IN ('second_yellow', 'red_card') THEN 1 END
    ) AS broj_iskljucenja
FROM match_events me
JOIN teams t ON t.team_id = me.team_id
JOIN matches m ON m.match_id = me.match_id
GROUP BY m.season, t.team_name
HAVING broj_iskljucenja >= 1
ORDER BY m.season, broj_iskljucenja DESC;
-- Rezultat 35 klubova

--********************************************************************************************************************************************
--***************************************************************DODATNI ZADACI***************************************************************
--********************************************************************************************************************************************

--=================================OSNOVNI NIVO=================================--

-- 1 zadatak: Za svakog sudiju prikažite njegovo ime i broj utakmica koje je sudio. Uključite i sudije koje nisu sudile ni jednu utakmicu.
SELECT
    r.referee_name AS ime_sudije,
    COUNT(m.kickoff_ts) AS broj_utakmica
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id
GROUP BY r.referee_name
ORDER BY broj_utakmica DESC;
-- Resenje jedan sudija je sudio 41 utakmicu (Mark Halsey-Brown) a jedan sudija nije sudio ni jednu (Paul Tierney-Ross)

-- 2 zadatak: Prikažite imena i prezimena igrača koji nemaju ni jedan zapis u tabeli player_match_stats.
SELECT
    p.first_name, p.last_name
FROM players p
LEFT JOIN player_match_stats pms ON pms.player_id = p.player_id
WHERE pms.player_id IS NULL;
-- Ukupno 31 igrac

-- 3 zadatak: Prikažite broj golova koji je svaki klub postigao kao domaćin u sezoni 2024/25. Rezultat sortirajte od najvećeg ka najmanjem broju golova.
SELECT
    t.team_name AS ime_kluba,
    SUM(m.home_goals) AS golovi_domacina
FROM matches m
JOIN teams t ON t.team_id = m.home_team_id
WHERE season = '2024/25'
GROUP BY ime_kluba
ORDER BY golovi_domacina DESC;

--=================================SREDNJI NIVO=================================--

-- 1 zadatak: Za svaku sezonu prikažite broj golova koje su postigli igrači na pozicijama FW, MF i DF. Rezultat grupišite prema sezoni i poziciji igrača.
-- goal ; penalty_goal
SELECT
    m.season,
    CASE WHEN p.position LIKE 'DF' THEN 'DF' 
         WHEN p.position LIKE 'MF' THEN 'MF' 
         WHEN p.position LIKE 'FW' THEN 'FW' END AS pozicija,
    COUNT(*) AS golovi
FROM matches m
JOIN match_events me ON me.match_id = m.match_id
JOIN players p ON p.player_id = me.player_id
WHERE me.event_type IN ('goal', 'penalty_goal')
GROUP BY m.season, pozicija
ORDER BY m.season, pozicija;
-- Resenje drugacijeg izgleda tabele nego na casu
-- season	    pozicija	golovi
-- 2023/24	    DF	        126
-- 2023/24	    FW	        532
-- 2023/24	    MF	        352
-- 2024/25	    DF	        138
-- 2024/25	    FW	        525
-- 2024/25	    MF	        370

-- Ispod resenje kao na casu, vezba
SELECT
    m.season AS sezona,
    SUM(
        CASE WHEN p.position LIKE 'DF' THEN 1 END
    ) as df,
    SUM(
        CASE WHEN p.position LIKE 'MF' THEN 1 END
    ) as mf,
    SUM(
        CASE WHEN p.position LIKE 'FW' THEN 1 END
    ) as fw
FROM matches m
JOIN match_events me ON me.match_id = m.match_id
JOIN players p ON p.player_id = me.player_id
WHERE me.event_type IN ('goal', 'penalty_goal')
GROUP BY m.season;
-- Resenje izgleda kao na casu
-- sezona	    df	    mf	    fw
-- 2023/24	    126	    352	    532
-- 2024/25	    138	    370	    525

-- 2 zadatak: Za svaki stadion prikažite njegov naziv i ukupan broj gledalaca na utakmicama odigranim na njemu. Uključite i stadione za koje nema evidentiranih utakmica.
SELECT
    s.stadium_name AS ime_stadiona,
    SUM(m.attendance) AS ukupan_broj_gledalaca
FROM stadiums s
LEFT JOIN matches m ON m.stadium_id = s.stadium_id
GROUP BY s.stadium_name
ORDER BY ukupan_broj_gledalaca DESC;
-- Resenje ima 22 stadiona sa ukupnim brojem gledaoca.

-- 3 zadatak: Za svakog sudiju prikažite broj različitih utakmica u kojima je dosuđen penal, bez obzira na to da li je penal realizovan. Uključite i sudije za koje nema takvih utakmica.
SELECT
    r.referee_name AS ime_sudije,
    COUNT(DISTINCT me.match_id) AS broj_utakmica_sa_penalom
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id
LEFT JOIN match_events me ON me.match_id = m.match_id AND me.event_type IN ('penalty_miss', 'penalty_goal')
GROUP BY r.referee_name
ORDER BY broj_utakmica_sa_penalom;

--=================================NAPREDNI NIVO=================================--

-- 1 zadatak: Za svaki klub prikažite naziv kluba i broj utakmica koje je odigrao kao domaćin u sezoni 2024/25. Rešite zadatak na dva načina:
-- - koristeći INNER JOIN;
-- - koristeći LEFT JOIN.
-- Objasnite da li se rezultati razlikuju i zašto. Obratite pažnju na klubove koji nemaju ni jednu domaću utakmicu.

SELECT
    t.team_name AS ime_tima,
    COUNT_IF(m.home_team_id IS NOT NULL) AS broj_utakmica
FROM teams t
JOIN matches m ON m.home_team_id = t.team_id  AND m.season = '2024/25'
GROUP BY ime_tima;

SELECT
    t.team_name AS ime_tima,
    COUNT_IF(m.home_team_id IS NOT NULL) AS broj_utakmica
FROM teams t
LEFT JOIN matches m ON m.home_team_id = t.team_id AND m.season = '2024/25'
GROUP BY ime_tima;
-- U resenju sa INNER JOIN imamo klubove samo za koje imamo podatke za tu sezonu, dok u LEFT JOIN imamo klubove i koji nisu igrali kod kuce te sezone (mozda su ispali iz lige).

-- 2 zadatak: Za svaki autogol u sezoni 2024/25 prikažite ime igrača, klub za koji je igrač nastupao na toj utakmici i klub kojem je gol priznat.
SELECT
    p.first_name AS ime_igrace,
    p.last_name AS prezime_igraca,
    t_nastup.team_name AS klub_nastup,
    t_priznat.team_name AS klub_priznat_gol
FROM match_events me
JOIN players p ON p.player_id = me.player_id
JOIN player_match_stats pms ON pms.player_id = me.player_id AND pms.match_id = me.match_id
JOIN teams t_nastup ON t_nastup.team_id = pms.team_id
JOIN teams t_priznat ON t_priznat.team_id = me.team_id
JOIN matches m ON m.match_id = me.match_id
WHERE m.season = '2024/25' AND me.event_type LIKE 'own_goal';
-- Ukupno 58 rezultata

-- 3 zadatak: Pronađite sve klubove koji imaju najmanje jednog igrača koji nema ni jedan zapis u player_match_stats. Prikažite naziv kluba i broj takvih igrača. 
-- Rezultat sortirajte opadajuće prema broju igrača.

SELECT
    t.team_name,
    COUNT(*) AS broj_igraca
FROM players p
LEFT JOIN player_match_stats pms ON pms.player_id = p.player_id
JOIN player_contracts pc ON pc.player_id = p.player_id 
JOIN teams t ON t.team_id = pc.team_id
WHERE pms.player_id IS NULL
GROUP BY t.team_name
ORDER BY broj_igraca DESC;

-- 4 zadatak: Za svaki grad prikažite broj odigranih utakmica i ukupan broj gledalaca. Pronađite grad sa najvećim ukupnim brojem gledalaca.
SELECT
    s.city AS grad,
    COUNT(m.home_team_id) AS broj_odigranih_utakmica,
    SUM(m.attendance) AS ukupan_broj_gledalaca
FROM stadiums s
JOIN matches m ON m.stadium_id = s.stadium_id
WHERE m.status = 'played'
GROUP BY s.city
ORDER BY ukupan_broj_gledalaca DESC;
-- Rezultat grad sa najvecim ukupnim brojem gledalaca je Northport = 2 957 364

select * from matches where status = 'abandoned';

-- 5 zadatak: Pronađite sudije koje su sudile utakmice u sezoni 2023/24, ali nisu sudile ni jednu utakmicu u sezoni 2024/25. Prikažite ime sudije i njegovu nacionalnost.
SELECT
    r.referee_id,
    r.referee_name AS ime_sudije, 
    r.nationality AS nacionalnost,
    COALESCE(m.season, 'NEMA') AS sezona_u_kojoj_je_sudio
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id 
WHERE m.season IS NULL;
-- Resenje: Ime sudije: Paul Tierney-Ross; Nacionalnost: England. Ovaj sudija nema ni jedan nastup ni u sezoni 2023/24 a ni u sezoni 2024/25 jer je poceo da sudi u sezoni 2025/26

SELECT
   DISTINCT r.referee_id, r.referee_name, r.nationality, m.season
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id 
WHERE m.season = '2023/24'
ORDER BY r.referee_id ASC;
-- Rezultat 19 sudija je sudilo u sezoni '2023/24'
-- Da li je tacno ovako kad se radi sa dva upita i da li moze da se resi sa jednim upitom?
