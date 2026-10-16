-- 1 zadatak
SELECT
    kickoff_ts, home_team, away_team,
    home_yellow_cards, away_yellow_cards, home_red_cards, away_red_cards,
    home_yellow_cards + away_yellow_cards + home_red_cards + away_red_cards AS total_cards
FROM bootcamp.northern_star.matches_flat LIMIT 10;

-- 2 zadatak
SELECT
    kickoff_ts, home_team, away_team,
    home_yellow_cards + away_yellow_cards + home_red_cards + away_red_cards AS total_cards
FROM bootcamp.northern_star.matches_flat ORDER BY total_cards DESC, kickoff_ts ASC LIMIT 10;
-- Uutakmici Elmsworth Wanderers protiv Brackley Harriers jed podeljeno najvise kartona, ukupno 5.

-- 3 zadatak
SELECT
    home_team, away_team, stadium_name, attendance
FROM bootcamp.northern_star.matches_flat ORDER BY attendance ASC LIMIT 5;
-- Na vrhu su prvo utakmice koje nemaju unete podatke za broj posecenosti.

SELECT
    home_team, away_team, stadium_name, attendance
FROM bootcamp.northern_star.matches_flat ORDER BY attendance ASC NULLS LAST LIMIT 5;

-- 4 zadatak
SELECT
    DISTINCT stadium_name
FROM bootcamp.northern_star.matches_flat;

-- 2 nacin 4 zadatka
SELECT
    COUNT(DISTINCT stadium_name)
FROM bootcamp.northern_star.matches_flat;
-- Imaju 22 razlicita stadiona u bazi.

SELECT
    DISTINCT stadium_city
FROM bootcamp.northern_star.matches_flat;

-- 2 nacin 4 zadatka
SELECT
    COUNT(DISTINCT stadium_city)
FROM bootcamp.northern_star.matches_flat;
--Ima 21 razlicit grad u bazi.

-- imaju u jednom gradu dva stadiona.

-- 5 zadatak

SELECT
    DISTINCT season, 
    home_team
FROM bootcamp.northern_star.matches_flat;

SELECT
    DISTINCT home_team, 
    season
FROM bootcamp.northern_star.matches_flat;

-- U oba sucaja ima 40 kombinacija, zato sto je broj klubova u ligi tokom sezone fiksan, tako da ce uvek biti isti broj.

---resenje profe
SELECT DISTINCT home_team, season
FROM bootcamp.northern_star.matches_flat ORDER BY season, home_team;

-- 6 zadatak
SELECT
    DISTINCT weather
FROM bootcamp.northern_star.matches_flat;

-- negde nije upisana vrednost za kolonu weather.

-- 7 zadatak
SELECT
    home_team, away_team, home_goals, away_goals,
    home_goals - away_goals AS home_goal_diff
FROM bootcamp.northern_star.matches_flat ORDER BY home_goal_diff DESC LIMIT 5;