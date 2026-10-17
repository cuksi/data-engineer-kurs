USE bootcamp.northern_star;

-- 1 zadatak
-- Posto je jedan uslov bio dvosmislen (čiji naslov (`match_report`) sadrži reč `goal`) imaju dva resenja sa opisom koje resenje sta dobija za rezultat.
SELECT
match_report
FROM matches_flat
WHERE match_report ILIKE '%goal%';
-- Ukupno 41 utakmica, ovde ce da nadje sve utakmice gde se trazena rec goal javlja kao rec i kao deo neke druge reci (Goalless)

SELECT
match_report
FROM matches_flat
WHERE match_report ILIKE '% goal %';
-- Ukupno 0 utakmica, , ovde ce biti prikazane utakmice samo gde postoji rec goal(kao zasebna rec, nije deo neke druge reci) u match_report-u

--2 zadatak
SELECT
coalesce(referee_name, 'Unknown') AS referee_name
FROM matches_flat LIMIT 20;

-- 3 zadatak
SELECT
match_report,
length(match_report) AS broj_znakova
FROM matches_flat
WHERE length(match_report) > 40;
-- Ukupno 537 utakmica

--4 zadatak
SELECT
home_team, away_team, home_goals, away_goals, kickoff_ts
FROM matches_flat
WHERE kickoff_ts >= '2025-01-01' AND kickoff_ts < '2025-01-16' ORDER BY kickoff_ts ASC;
-- Ukupno 31 utakmica

-- 5 zadatak
SELECT
match_id, home_team, away_team,
DATE(kickoff_ts) AS `Datum`,
dayofweek(kickoff_ts) AS `Dan u nedelji`
FROM matches_flat
WHERE dayofweek(kickoff_ts) = 6;
-- Rezultat 0, ni jedna utakmica nije odigrana petkom. 
-- PROVERA: Ima 23 utakmice odigrane u ponedeljak, 15 utakmica u utorak, 18 utakmica u sredu, 10 u četvrtak, 574 utakmica u subotu, 121 utakmica je odigrana u nedelju. Zbir daje ukupno 761 utakmica, sto znaci da sigurno nema ni jedna utakmica u petak tj. rezultat 0.

-- 6 zadatak
SELECT
home_team, away_team, attendance, season
FROM matches_flat
WHERE season = '2024/25' AND attendance BETWEEN 20000 AND 35000;
-- Ukupno 188 utakmica

-- 7 zadatak
SELECT
DISTINCT first_goal_scorer
FROM matches_flat
WHERE first_goal_scorer LIKE 'A%' OR first_goal_scorer LIKE '%-%';
-- Ukupno 22 prvih strelaca

-- 8 zadatak
SELECT
HOUR(kickoff_ts) AS `Vreme pocetka utakmice`,
concat(home_team, ' - ', away_team) AS `Nazivi timova`
FROM matches_flat
WHERE season = '2024/25'  AND HOUR(kickoff_ts) BETWEEN 18 AND 21;
-- Ukupno 12 utakmica

-- 9 zadatak
-- Posto je jedan uslov bio dvosmislen (čiji naslov sadrži reč `win`) imaju dva resenja sa opisom koje resenje sta dobija za rezultat.
SELECT
COUNT(kickoff_ts)
FROM matches_flat
WHERE year(kickoff_ts) = '2025' AND (month(kickoff_ts) IN (3, 4, 5)) AND match_report ILIKE '%win%';
-- Ukupno 5 utakmcia, ovde ce da nadje sve utakmice gde se trazena rec win javlja kao rec i kao deo neke druge reci (winner)

SELECT
COUNT(kickoff_ts)
FROM matches_flat
WHERE year(kickoff_ts)= '2025' AND month(kickoff_ts) IN (3, 4, 5) AND match_report ILIKE '% win %';
-- Ukupno 3 utakmice, ovde ce biti prikazane utakmice samo gde postoji rec win(kao zasebna rec, nije deo neke druge reci) u match_report-u

----------------------------------------------------------------------------------
--------------------------------- DODATNI ZADACI ---------------------------------

-- 1 zadatak
SELECT
count(match_id)
FROM matches_flat
WHERE referee_name IS NULL AND  attendance IS NULL;
-- Ukupno 0 utakmica
-- attendance nedostaje u nekoliko utakmica (17), ali referee_name je svuda popunjen zato je 0

-- 2 zadatak
SELECT
home_team, away_team,
DATE(kickoff_ts) AS `Datum odigravanja`
FROM matches_flat
WHERE DATE(kickoff_ts) >= '2025-03-01' AND DATE(kickoff_ts) < '2025-04-01'
ORDER BY DATE(kickoff_ts) ASC;
-- Ukupno 40 utakmica

-- 3 zadatak
SELECT
COUNT(kickoff_ts)
FROM matches_flat
WHERE DATE(kickoff_ts) >= '2024-12-19' AND DATE(kickoff_ts) < '2025-01-11';
-- Ukupno 51 utakmica

-- 4 zadatak
SELECT
DATE(kickoff_ts) AS `Datum utakmice`,
home_team AS `Domaći tim`,
away_team AS `Gostujući tim`,
coalesce(CAST(attendance as STRING), 'Unknown') AS attendance_status
FROM matches_flat;

-- 5 zadatak
SELECT
home_team, away_team, home_goals, away_goals,
home_goals + away_goals AS `Ukupno golova`,
DATE(kickoff_ts) AS `Datum utakmice`
FROM matches_flat
WHERE DATE(kickoff_ts) >= '2025-04-01' AND DATE(kickoff_ts) < '2025-05-01' AND (home_goals + away_goals) BETWEEN 2 AND 4
ORDER BY DATE(kickoff_ts) ASC;
-- Ukupno 22 utakmice

-- 6 zadatak
SELECT
DATE(kickoff_ts) AS `Datum utakmice`,
home_team, away_team,
CONCAT(home_goals_ht, ' : ', away_goals_ht) AS `Rezultat na poluvremenu`,
CONCAT(home_goals, ' : ', away_goals) AS `Rezultat na kraju utakmice`
FROM matches_flat
WHERE home_goals_ht = away_goals_ht AND NOT home_goals = away_goals;
-- Ukupno 244 utakmice