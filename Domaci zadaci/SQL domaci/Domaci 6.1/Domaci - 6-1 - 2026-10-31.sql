USE bootcamp.sandbox;

-- 1 zadatak: Kreiranje dimenzije igrača: Na osnovu tabele players napravite tabelu dim_player koja sadrži sledeće kolone: player_id, ime, prezime, poziciju i nacionalnost igrača. Koliko redova ima novokreirana tabela?
CREATE OR REPLACE TABLE dim_player AS
SELECT player_id, first_name, last_name, position, nationality
FROM bootcamp.northern_star.players;

SELECT * FROM dim_player;
SELECT COUNT(*) FROM dim_player;
-- Resenje ima 681 red.

-- 2 zadatak: Kreiranje dimenzije datuma i činjenične tabele: Napravite tabelu dim_date na isti način kao na predavanju. Zatim napravite tabelu fact_player_match na osnovu tabela player_match_stats i matches. 
--              Tabela treba da sadrži sledeće kolone: match_id, date_key, player_id, team_id, minutes_played, shots, passes i rating. U tabelu uključite samo podatke koji se odnose na odigrane utakmice.
--              Kolika je granularnost tabele fact_player_match, odnosno šta predstavlja jedan njen red? Koliko redova ima ova tabela?
CREATE OR REPLACE TABLE dim_date AS
SELECT CAST(DATE_FORMAT(d, 'yyyyMMdd') AS INT) AS date_key,
       d                                       AS full_date,
       DATE_FORMAT(d, 'EEEE')                  AS weekday_name,
       DAYOFWEEK(d) IN (1, 7)                  AS is_weekend,
       CASE WHEN MONTH(d) >= 7 THEN CONCAT(YEAR(d), '/', SUBSTRING(CAST(YEAR(d) + 1 AS STRING), 3, 2))
            ELSE CONCAT(YEAR(d) - 1, '/', SUBSTRING(CAST(YEAR(d) AS STRING), 3, 2))
       END                                     AS season
FROM (SELECT EXPLODE(SEQUENCE(DATE'2023-07-01', DATE'2025-06-30', INTERVAL 1 DAY)) AS d);

CREATE OR REPLACE TABLE fact_player_match AS
SELECT 
    m.match_id,
    CAST(DATE_FORMAT(m.kickoff_ts, 'yyyyMMdd') AS INT) AS date_key,
    pms.player_id,
    pms.team_id,
    pms.minutes_played,
    pms.shots,
    pms.passes,
    pms.rating
FROM bootcamp.northern_star.matches m
JOIN bootcamp.northern_star.player_match_stats pms ON pms.match_id = m.match_id
WHERE m.status = 'played';

SELECT * FROM fact_player_match;
-- Resenje: Svaki red ovo nove tabele predstavlja statistiku igraca koliko je igrao, šuteve, paseve i ocenu na kom meču i kada.
SELECT COUNT(*) FROM fact_player_match;
-- Resenje: ova tabela ima 30400 redova.

-- 3 zadatak: Prosečna ocena igrača po poziciji: Koristeći napravljene dimenzije i činjeničnu tabelu, izračunajte prosečnu ocenu (rating) igrača za svaku poziciju tokom sezone 2024/25. Prikažite poziciju i odgovarajuću prosečnu ocenu.
SELECT
    dp.position, 
    ROUND(AVG(fpm.rating), 2) AS prosecna_ocena
FROM fact_player_match fpm
JOIN dim_date dd ON dd.date_key = fpm.date_key
JOIN dim_player dp ON dp.player_id = fpm.player_id
WHERE dd.season = '2024/25' AND NOT ISNAN (fpm.rating)
GROUP BY dp.position;
-- Resenje:
-- position	    prosecna_ocena
-- FW	        6.79
-- DF	        6.64
-- MF	        6.72
-- GK	        6.6

-- 4 zadatak: Dodavanje broja golova u činjeničnu tabelu: Proširite tabelu fact_player_match dodavanjem kolone koja predstavlja broj golova koje je svaki igrač postigao na određenoj utakmici. 
--             Koliki je ukupan zbir golova svih igrača u tabeli fact_player_match?
CREATE OR REPLACE TABLE fact_player_match AS
SELECT
    m.match_id,
    CAST(DATE_FORMAT(m.kickoff_ts, 'yyyyMMdd') AS INT) AS date_key,
    pms.player_id,
    pms.team_id,
    pms.minutes_played,
    pms.shots,
    pms.passes,
    pms.rating,
    COALESCE(g.golova, 0) AS golova
FROM bootcamp.northern_star.matches m
JOIN bootcamp.northern_star.player_match_stats pms ON pms.match_id = m.match_id
LEFT JOIN (
    SELECT match_id, player_id, COUNT(*) AS golova
    FROM bootcamp.northern_star.match_events
    WHERE event_type IN ('goal', 'penalty_goal')
    GROUP BY match_id, player_id
) g ON g.match_id = pms.match_id AND g.player_id = pms.player_id
WHERE m.status = 'played';

SELECT SUM(golova) AS ukupno_golova FROM fact_player_match;
-- Resenje: ukupno 2043 gola.