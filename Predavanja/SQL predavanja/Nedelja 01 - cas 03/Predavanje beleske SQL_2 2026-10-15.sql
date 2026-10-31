-- WHERE, AND, OR

-- = , <> , > , >= , < , <=

SELECT * FROM bootcamp.northern_star.matches_flat
WHERE home_team = 'Northport United'; -- 'northport united' nije isto

SELECT * FROM bootcamp.northern_star.matches_flat
WHERE kickoff_ts >= '2025-01-01'; -- YYYY-MM-DD u data bricksu mora crtica izmedju godine-meseca-dana

SELECT 
    home_team, away_team, home_goals, away_goals
FROM bootcamp.northern_star.matches_flat
WHERE home_team = 'Northport United' 
OR away_team = 'Northport United'
AND home_goals > away_goals;    -- ovde ide prvo AND pa onda OR uslov, kao u matematici

SELECT 
    home_team, away_team, home_goals, away_goals
FROM bootcamp.northern_star.matches_flat
WHERE (home_team = 'Northport United' 
OR away_team = 'Northport United')
AND home_goals > away_goals;    -- ovde posto je zagrda ide prvo OR pa onda AND

-- Redosled komandi kojim ide kod tj. kako se izvrsava:
-- FROM
-- WHERE
-- SELECT
-- DISTINCT
-- ORDER BY
-- LIMIT


-- ovo nece raditi
-- SELECT 
--     home_team, away_team, home_goals, away_goals,
-- home_yellow_cards + away_yellow_cards + home_red_cards + away_red_cards AS total_cards
-- FROM bootcamp.northern_star.matches_flat
-- WHERE total_cards > 10;  -- zato sto WHERE nije svestan tj. ne vidi ovu novo napravljenu kolonu total_cards posto izvrsava po gore napisanom redosledu komandi

