USE bootcamp.northern_star;

SELECT
    home_goals, away_goals,
    CASE WHEN home_goals > away_goals THEN 'Pobeda domacina'
         WHEN home_goals = away_goals THEN 'Nereseno'
         WHEN home_goals < away_goals THEN 'Pobeda gosta'
         ELSE 'Greska' END AS `Rezultat`    -- ovo greska treba da se aktivira kada je vrednost NULL, posto gore imamo tri moguca slucaja a kad je NULL ide u ELSE
FROM matches_flat;
-- WHERE home_goals IS NULL;

--3 poena pobeda, 1 poen nereseno, 0 poena izgubljena
SELECT
    home_team, home_goals, away_goals,
    CASE WHEN home_goals > away_goals THEN 3    -- ovo CASE WHEN SE zove u praksi prosirenje
         WHEN home_goals = away_goals THEN 1
         WHEN home_goals < away_goals THEN 0
         ELSE NULL END AS `Bodovi domacina`
FROM matches_flat;

SELECT
    home_team, season,
    SUM(
        CASE WHEN home_goals > away_goals THEN 3
        WHEN home_goals = away_goals THEN 1
        WHEN home_goals < away_goals THEN 0
        ELSE NULL END
        ) AS `Bodovi domacina`
FROM matches_flat 
GROUP BY home_team, season
ORDER BY season, `Bodovi domacina` DESC;