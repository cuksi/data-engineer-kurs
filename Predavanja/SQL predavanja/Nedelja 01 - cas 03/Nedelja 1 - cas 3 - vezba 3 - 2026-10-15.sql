-- 1 zadatak
SELECT 
    stadium_name, attendance
FROM bootcamp.northern_star.matches_flat
WHERE stadium_name = 'National Stadium'
ORDER BY attendance DESC;
-- Ukupno 3 utakmice

-- 2 zadatak
SELECT 
    DISTINCT home_team, stadium_name
FROM bootcamp.northern_star.matches_flat;

-- Brackley Harriers -> Brackley Road AND Brackley Athletic	-> Brackley Road;
-- Dunmore County -> Dunmore Park AND Dunmore Celtic -> Dunmore Park
-- Ukupno 2 tima dele stadion

-- 3 zadatk home_goals_ht
SELECT 
    home_team, home_goals_ht, home_goals, away_team, away_goals_ht, away_goals
FROM bootcamp.northern_star.matches_flat
WHERE home_goals_ht > away_goals_ht AND (home_goals < away_goals OR home_goals = away_goals);
-- Domacin nije dobio ukupno 50 utakmica i ako je vodio na poluvremenu

-- 4 zadatak
SELECT 
    kickoff_ts,home_team, home_goals, away_team, away_goals
FROM bootcamp.northern_star.matches_flat
WHERE home_goals > 0 AND away_goals > 0 AND kickoff_ts >= '2025-01-01' AND kickoff_ts <= '2025-01-31';
-- ukupno 23 utakmica je imalo golove na obe strane

-- 5 zadatak
SELECT 
    DISTINCT first_goal_scorer, first_goal_minute
FROM bootcamp.northern_star.matches_flat
WHERE first_goal_minute > 80;
-- Ukupno 20 razlicitih igraca je dalo prvi gol posle 80 minuta