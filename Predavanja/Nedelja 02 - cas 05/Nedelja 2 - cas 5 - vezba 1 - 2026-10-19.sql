-- 1 zadatak
SELECT
 season,
 attendance,
 COUNT(*) AS att_null
FROM matches_flat
GROUP BY season, attendance
HAVING attendance IS NULL;
-- Ukupno 17 utakmica
-- 2023/24 - ukupno 8 utakmica
-- 2024/25 - ukupno 9 utakmica

-- 2 zadatak
SELECT
    stadium_name,
    MIN(attendance) AS min_att,
    MAX(attendance) AS max_att
FROM matches_flat
GROUP BY stadium_name
ORDER BY max_att DESC;
-- Ukupno 22 rezultata. Stadion sa najvecom posetom Harbourside Park -> 50922.

-- 3 zadatak
SELECT
    season,
    SUM(home_goals) AS sum_home_goals,
    SUM(away_goals) AS away_goals
FROM matches_flat
GROUP BY season;
-- 2023/24 -> domacini 591 gol, gosti 455 golova
-- 2024/25 -> domacini 587 golova, gosti 505 golova

--4 zadatak
SELECT
    date_format(kickoff_ts, 'EEEE') AS weekday,
    COUNT(*) AS matches, 
    AVG(home_goals + away_goals) AS goals_per_match
FROM matches_flat
--WHERE status = 'played'
GROUP BY date_format(kickoff_ts, 'EEEE')
ORDER BY matches DESC;
-- Ukupno 6 rezultata, najvise se igra Subotom (Saturday) -> 573

-- 5 zadatak
SELECT
    referee_name,
    SUM(home_red_cards + away_red_cards) AS sum_red_cards
FROM matches_flat
GROUP BY referee_name
HAVING SUM(home_red_cards + away_red_cards) >= 5
ORDER BY referee_name DESC;
-- Ukupno 12 sudija, Sudija Stuart Attwell-Jones je dao najvise crvenih kartona 7

-- 6 zadatak
SELECT
    home_team,
    AVG(home_goals) AS avg_home_goals
FROM matches_flat
WHERE season = '2024/25'
GROUP BY home_team
HAVING AVG(home_goals) > 2;
-- Ukupno 3 rezultata, klubovi: Kingsbridge City, Northport United, Castlebrook United.

-- 7 zadatak
SELECT
    date_format(kickoff_ts, 'MMMM') as mesec,
    SUM(home_goals + away_goals) AS tot_month_goals
FROM matches_flat
GROUP BY mesec
ORDER BY tot_month_goals DESC;
-- u Decembry 282 gola.

----------------------------
------ DOdatni zadaci-------
----------------------------

-- 1 zadatak
SELECT
    home_team,
    COUNT(*) AS broj_utakmica,
    SUM(home_goals) AS tot_goals_home,
    AVG(home_goals) AS avg_goals
FROM matches_flat
GROUP BY home_team
HAVING COUNT(*) >= 10
ORDER BY broj_utakmica DESC;
-- Ukupno 23 kluba

-- 2 zadatak
SELECT
    season,
    COUNT(*) AS broj_utakmica,
    SUM(away_goals) AS golovi_gosta
FROM matches_flat
WHERE away_goals >= 3
GROUP BY season;
-- 2023/24 -> broj utakmica = 52 - broj golova gostiju = 184
-- 2024/25 -> broj utakmica = 65 - broj golova gostiju = 226