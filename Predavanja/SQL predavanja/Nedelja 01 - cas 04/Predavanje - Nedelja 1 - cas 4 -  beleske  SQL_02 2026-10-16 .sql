USE bootcamp.northern_star;

SELECT * FROM matches_flat;

SELECT
CONCAT(home_team_code, ' ', home_goals, ' - ', away_goals, ' ', away_team_code) AS `rezultat`, -- ovi tikovi se koriste da je pisano cirilicom ili tako nesto pa da prihvati ili ako imamo vise reci
CONCAT(first_goal_minute, '+', first_goal_added_time) AS `Vreme prvog gola - ne radi`, 
CONCAT(
    first_goal_minute,
    COALESCE(CONCAT('+', first_goal_added_time))
) AS `Vreme prvog gola`,
LENGTH(first_goal_scorer),
first_goal_scorer
FROM matches_flat;

SELECT * FROM matches_flat WHERE LOWER(home_team_code) = 'elw'; -- LOWER prebacuje u mala slova

SELECT LOWER(home_team_code) FROM matches_flat WHERE LOWER(home_team_code) = 'elw'; -- ovde ce da i prikaze u malim slovima posto smo stavili LOWER kod SELCTA-a

SELECT INITCAP(home_team_code) FROM matches_flat WHERE LOWER(home_team_code) = 'elw';  -- INITCAP prebacuje prvo slovo u veliko

-- UPPER
-- TRIM uklanja razmake sa pocetka i kraja

SELECT -- kada selektujemo funkciju, prevucemo je da poplavi i stavimo strelicu misa na nju ispise sta radi ta funkcija
    kickoff_ts,
    DATE(kickoff_ts) AS match_Date,-- daje samo datum
    HOUR(kickoff_ts) AS sati, -- daje samo sate
    MINUTE(kickoff_ts) AS minuti,  -- daje samo minute
    DAYOFWEEK(kickoff_ts) as day_of_week, -- daje dan u nedelji ali daje dane kao brojeve u nedelji, broj 1 je nedelja
    DATEDIFF(kickoff_ts, original_kickoff_ts) AS days_postponed -- koliko je dana proslo
FROM matches_flat
WHERE original_kickoff_ts IS NOT NULL;

-- ROUND za zaokruzivanje

SELECT
    ABS(home_goals - away_goals) as `diff` -- ABS funkcija daje abolutnu vrednost, daje vrednost ako je negativna u plusu
FROM matches_flat;

-- SELECT 1 / 0; -- ovo daje gresku namerno

SELECT try_divide(1,0); -- ovo ce probati ako uspe dace rezultat a ako ne moze dace NULL