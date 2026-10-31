USE bootcamp.northern_star;

SELECT COUNT(*) FROM matches_flat
WHERE attendance > 5;

SELECT 5 > NULL;

SELECT home_team, away_team, weather
FROM matches_flat
WHERE weather IN ('snow', 'fog'); --50

SELECT home_team, away_team, weather
FROM matches_flat
WHERE weather NOT IN ('snow', 'fog'); --637

SELECT home_team, away_team, weather
FROM matches_flat
WHERE weather IS NULL; --74

SELECT home_team, away_team, weather
FROM matches_flat
WHERE weather IS NOT NULL; --687


SELECT kickoff_ts
FROM matches_flat
WHERE kickoff_ts BETWEEN '2024-12-25' AND '2024-12-27'; -- 2024-12-25 00:00:00  |||| 2024-12-27 00:00:00 poredi ovaj datum ali samo za ova vremena 00:00:00

SELECT kickoff_ts
FROM matches_flat
WHERE kickoff_ts >= '2024-12-26' AND kickoff_ts < '2024-12-27'; -- ovde poredi sva vremena za ovaj datum

SELECT DISTINCT home_team FROM matches_flat
WHERE home_team LIKE '%United';

SELECT DISTINCT home_team FROM matches_flat
WHERE home_team LIKE '%U%'; -- ovaj search ima manje performanse od prethodnog jer mora vise slova da poredi, % znaci 0 ili vise karktera

SELECT DISTINCT home_team, home_team_code FROM matches_flat
WHERE home_team_code LIKE '_U_'; -- _ znaci jedan karakter

SELECT DISTINCT home_team, home_team_code FROM matches_flat
WHERE home_team_code LIKE 'U__'; -- ovde imaju dve crte znaci mora rec od tacno 3 karaktera

SELECT DISTINCT home_team, home_team_code FROM matches_flat
WHERE home_team_code ILIKE 'w__'; -- ovde ce da nadje neki tim posto ILIKE zanemariju velicinu slova

SELECT DISTINCT home_team, home_team_code FROM matches_flat
WHERE home_team_code LIKE 'w__'; -- ovde nece naci nista zato sto su kod LIKE bitna velicina slova

SELECT match_id, first_goal_scorer, home_goals, away_goals 
FROM matches_flat;

SELECT match_id, first_goal_scorer, home_goals, away_goals 
FROM matches_flat
WHERE first_goal_scorer IS NULL;

SELECT 
    match_id, 
    coalesce(first_goal_scorer, 'Nema golova'),  -- ova funkcija ide redom i gleda jel ima vrednost, ako naidje na NULL preskace ili upisuje zadatu vrednost
    home_goals, 
    away_goals 
FROM matches_flat;

SELECT
    coalesce(attendance, 0) AS Posecenost    
FROM matches_flat;

SELECT
    coalesce(NULL, NULL, 1, 2, 0)    -- ide do prve vrednost gde postoji tj. nije NULL i tu vrednost upisuje
FROM matches_flat;

SELECT
    coalesce(NULL, 2, NULL, 2 / 5, 0)    -- ovde iako postoji greska u kodu (greska: 2 / 5) nece je prijaviti zato sto nece ici dalje od 2 kod
FROM matches_flat;

SELECT
    coalesce(attendance, 0) AS `Posecenost stadiona`  -- ovo je ako hocemo da kolona ima naziv od dve reci koje su razdvojene
FROM matches_flat;