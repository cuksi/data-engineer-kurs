-- 1 zadatak
SELECT 
    away_team, away_goals, season
FROM bootcamp.northern_star.matches_flat
WHERE season ='2024/25' AND away_goals >= 4;
-- Ukupno 22 utakmice

-- 2 zadatak
SELECT 
    home_team, away_team, season
FROM bootcamp.northern_star.matches_flat
WHERE season = '2023/24' AND (home_team = 'Kingsbridge City' OR away_team = 'Kingsbridge City');
-- Ukupno 38 utakmica

-- 3 zadatak
SELECT 
    *
FROM bootcamp.northern_star.matches_flat
WHERE referee_name = 'Daniel Price' AND kickoff_ts >= '2024-12-1' AND kickoff_ts <= '2024-12-31';
-- Ukupno je sudio u 4 utakmice

-- 4 zadatak
SELECT 
    away_team, away_goals, home_team, home_goals, season
FROM bootcamp.northern_star.matches_flat
WHERE season = '2023/24' AND away_goals - home_goals >= 2;
-- ukupno 58 pobeda gostujuceg tima

-- 5 zadatak
SELECT 
    home_team, home_goals, away_team, away_goals
FROM bootcamp.northern_star.matches_flat
WHERE (home_team = 'Northport United' OR away_team = 'Northport United') AND (home_goals = away_goals);
-- Ukupno je zavrseno 15 utakmica nereseno kluba Northport United

-- 6 zadatak
SELECT 
    home_team, away_team, first_goal_scorer
FROM bootcamp.northern_star.matches_flat
WHERE first_goal_scorer = "Mattéo O'Brien";
-- Ukupno je bio strelac prvog gola u 21 utakmici.