USE bootcamp.northern_star;

-- 1 zadatak
SELECT
    matchday, home_team,home_goals_ht, away_team, away_goals_ht, season,
    CONCAT('HT ', home_goals_ht, '-', away_goals_ht) AS ht_score
FROM matches_flat
WHERE matchday = 1 and season = '2024/25';
-- Ukupno 10 rezultata

-- 2 zadatak
SELECT
    *
FROM matches_flat
WHERE status = 'abandoned';
-- Ukupno 761

SELECT
    home_team_code, away_team_code, season,
    CONCAT(home_team_code, '-', away_team_code, ' ', season) AS match_label
FROM matches_flat
WHERE NOT status = 'abandoned';
-- Ukupno 760

-- 2 nacin
SELECT
    DISTINCT CONCAT(home_team_code, '-', away_team_code, ' ', season) AS match_label
FROM matches_flat;
-- Ukupno 760

------------------------------------------------------------------------------------
-- 3 nacin
SELECT
    CONCAT(home_team_code, '-', away_team_code, ' ', season) AS match_label
FROM matches_flat;

SELECT COUNT(*) AS broj_utakmica -- ovo je isto kao gore iznad samo sa COUNT()
FROM matches_flat;

SELECT COUNT(DISTINCT CONCAT(
    home_team_code, '-', away_team_code, ' ', season
)) AS broj_razlicitih_oznaka
FROM matches_flat;
-----------------------------------------------------------------------------------

-- 3 zadatak
SELECT
    home_team, away_team, kickoff_ts
FROM matches_flat
WHERE HOUR(kickoff_ts) >= 20;
-- Ukupno 28 utakmica

-- 4 zadatak
SELECT
    home_team, away_team, kickoff_ts
FROM matches_flat
WHERE DAYOFWEEK(kickoff_ts) = 2;
-- Ukupno 23 utakmice

-- 5 zadatak
SELECT
    stadium_name, stadium_capacity, attendance
FROM matches_flat
WHERE (stadium_capacity / 2) >= attendance;
-- Ukupno 4 utakmice

-- 6 zadatak
SELECT
    *
FROM matches_flat
WHERE DAYOFWEEK(kickoff_ts) = 4;
-- Ukupno 18 utakmica
-- neke od njih nemaju podatak za vreme, dve su odlozene i na jednoj nije bilo golova

-- 7 zadatak
SELECT
    DISTINCT first_goal_scorer
FROM matches_flat
WHERE length(first_goal_scorer) >= 19;
-- Strelci sa najduzim imenom Aleksandar Živković, Aleksandar Đorđević