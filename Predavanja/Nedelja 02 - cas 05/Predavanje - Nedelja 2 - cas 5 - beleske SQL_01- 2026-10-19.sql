SELECT * FROM bootcamp.northern_star.matches_flat;

SELECT
date_format(kickoff_ts, 'EEEE')
FROM bootcamp.northern_star.matches_flat;

SELECT
COUNT(*) AS all_matches,
COUNT(weather) AS weather_exists,
COUNT(DISTINCT referee_name) AS referees
FROM bootcamp.northern_star.matches_flat;

SELECT
    COUNT(*) AS all_matches,
    COUNT(weather) AS weather_exists,
    COUNT(DISTINCT referee_name) AS referees,
    SUM(home_goals + away_goals) AS total_goals,
    SUM(home_goals + away_goals) AS goals_per_match,
    MIN(attendance) AS min_att,
    MAX(attendance) AS max_att
FROM bootcamp.northern_star.matches_flat 
WHERE attendance > 0;

SELECT 
    AVG(attendance) AS average_attendance,
    SUM(attendance) / COUNT(attendance) AS verage_attendance_zero_v2,   -- ovo je provera za AVG iz gore prethodnog reda
    AVG(COALESCE(attendance, 0)) AS average_attendance_zero, -- ovo je posto preskace NULL pa da dobijemo tacnu vrednost za podatke i ako nije odigrana
    SUM(attendance) / COUNT(*) AS verage_attendance_zero_v2   -- ovo je provera za AVG iz gore prethodnog reda, da uracuna i sa NULL 
 FROM bootcamp.northern_star.matches_flat;

SELECT 
    season, -- da nemamo GROUP BY ovo ne bi radilo, zato sto ove ispod kolone imaju po jednu vrednost season ima puno vise vrednosti i onda bi ove druge bile prazne. A sa GROUP BY deli podatke iz season prema zajednickom i onda odradi ove druge funkcije.
    SUM(home_goals + away_goals) AS total_goals,
    COUNT(*) as matches,
    AVG(home_goals + away_goals) AS goals_per_match
FROM bootcamp.northern_star.matches_flat
GROUP BY season;

SELECT 
    weather,
    SUM(home_goals + away_goals) AS total_goals,
    COUNT(*) as matches,
    AVG(home_goals + away_goals) AS goals_per_match
FROM bootcamp.northern_star.matches_flat
GROUP BY weather;   -- GROUP BY nece izabciti vrednosti NULL iz prikaza

-- Po vaznosti
-- FROM -> WHERE > GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT

SELECT
    season,
    DATE_TRUNC('MONTH',kickoff_ts) AS month,
    COUNT(*) AS matches,
    SUM(home_goals + away_goals) AS total_goals,
    ROUND(AVG(home_goals + away_goals), 2) AS goals_per_match   -- da zaokruzimo na dve decimale
FROM bootcamp.northern_star.matches_flat
GROUP BY season, DATE_TRUNC('MONTH',kickoff_ts)  -- databricks dozvoljava da koristimo ovo month ali u sql-u mora biti ovako GROUP BY season, DATE_TRUNC('MONTH',kickoff_ts) - mora da bude definisano
ORDER BY season, month;

SELECT
   DISTINCT DATE_TRUNC('MONTH',kickoff_ts)
FROM bootcamp.northern_star.matches_flat;

SELECT
    home_team,
   round(avg(attendance)) AS avg_attendance
FROM bootcamp.northern_star.matches_flat
GROUP BY home_team
-- HAVING izbacuje grupu koja ima manje ili 30 000 a ostale ce grupe da pokaze
HAVING avg_attendance > 30000   -- voditi racuna ovde ce databricks koristiti za avg_attendance sve round(avg(attendance)) i zaokruzivanje a to name nece trebati mozda uvek ili ce kvariti rezultat
ORDER BY avg_attendance;

SELECT
    referee_name,
    sum(home_yellow_cards + away_yellow_cards) as yellow_count,
    avg(home_yellow_cards + away_yellow_cards) AS yellow_per_match,
    COUNT(*) -- ovo sad daje sad ukupan broj podataka po svakom sudiji
FROM bootcamp.northern_star.matches_flat
GROUP BY referee_name
ORDER BY yellow_count DESC;