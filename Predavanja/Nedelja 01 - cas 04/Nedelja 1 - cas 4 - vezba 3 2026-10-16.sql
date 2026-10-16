USE bootcamp.northern_star;

-- 1 zadatak
SELECT
    concat(home_team_code, ' ', home_goals, ' - ', away_goals, ' ', away_team_code) AS scoreline,
    dayofweek(kickoff_ts) AS day_of_week
FROM matches_flat
WHERE month(kickoff_ts) IN (1, 2, 12) AND match_report ILIKE '%late%';
-- Ukupno 14 utakmica

-- 2 zadatak
SELECT
    home_team, away_team, home_goals, away_goals,
    ABS(home_goals - away_goals) as gol_diff,
    attendance
FROM matches_flat
WHERE ABS(home_goals - away_goals) >= 4 AND (attendance < 20000 OR attendance IS NULL);
-- Ukupno 16 utakmica ako zaboravimo NULL imacemo manje utakmica 14 jer kad se resi logika u WHERE bloku dobicemo NULL sto WHERE preskace po pravilu

-- 3 zadatak
SELECT
    DISTINCT first_goal_scorer
FROM matches_flat
WHERE first_goal_scorer LIKE "%'%";
-- Ukupno 5 strelaca: Mattéo O'Brien, Eoin O'Neill, Sean O'Neill, Shane O'Neill, Cian O'Neill

-- 4 zadatak
SELECT
    home_team, home_manager,
    away_team, away_manager,
    DATE(kickoff_ts) AS datum
FROM matches_flat
WHERE home_manager IS NULL OR away_manager IS NULL;
-- Tim: Westmere Town; Datum: 2025-03-01

-- 5 zadatak
SELECT
    home_team, away_team,
    home_goals_ht, away_goals_ht,
    home_goals, away_goals
FROM matches_flat
WHERE home_goals_ht = away_goals_ht AND (home_goals > away_goals OR away_goals > home_goals);
-- Ukupno 244 utakmice