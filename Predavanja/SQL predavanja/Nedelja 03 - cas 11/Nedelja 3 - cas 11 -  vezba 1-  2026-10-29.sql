USE bootcamp.sandbox;

-- 1 zadatak: Направите копију табеле teams помоћу CTAS. Колико редова има?
CREATE OR REPLACE TABLE teams_copy
SELECT * FROM bootcamp.northern_star.teams;

SELECT * FROM teams_copy;   -- Provera

-- 2 zadatak: Додајте колону league_status (STRING). Помоћу UPDATE упишите 'обе сезоне', 'испао' (играо само 2023/24), 'ушао' (играо само 2024/25) и 'није играо'. Колико клубова има сваку вредност?
ALTER TABLE teams_copy ADD COLUMN (league_status STRING);

UPDATE teams_copy   -- ovo je stavljeno na vrh zbog optimizacije. Objasnjenje dole na kraju zasto.
SET league_status = 'није играо';

UPDATE teams_copy
SET league_status = 'испао'
WHERE team_id IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2023/24') AND team_id NOT IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2024/25');

UPDATE teams_copy
SET league_status = 'ушао'
WHERE team_id NOT IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2023/24') AND team_id IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2024/25');

UPDATE teams_copy
SET league_status = 'обе сезоне'
WHERE team_id IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2023/24') AND team_id IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2024/25');


-- UPDATE teams_copy   -- ovo je bilo originalno resenje ali ovaj query je mogao biti prvi bez uslova WHERE pa posle pokrenemo ostale i dobicemo isto samo bolja optimizacija. Pa je prebaceno na pocetak.
-- SET league_status = 'није играо'
-- WHERE team_id NOT IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2023/24') AND team_id NOT IN (SELECT team_id FROM bootcamp.northern_star.team_matches WHERE season = '2024/25');

SELECT * FROM teams_copy;

-- 3 zadatak: Додајте измишљени клуб са team_id = 25, па га обришите помоћу DELETE. Пре DELETE покрените SELECT са истим WHERE.
DESCRIBE teams_copy;

INSERT INTO teams_copy
VALUES (25, 'MOJ KLUB', 'MK', 'BELGRADE', 1986, 2005, 'nije igrao');

SELECT * FROM teams_copy WHERE team_id = 25;

DELETE FROM teams_copy
WHERE team_id = 25;

SELECT * FROM teams_copy WHERE team_id = 25;

-- 4 zadatak: Помоћу DESCRIBE HISTORY пронађите верзију пре INSERT-а и прочитајте број редова у тој верзији.
DESCRIBE HISTORY teams_copy;

SELECT COUNT(*) FROM teams_copy VERSION AS OF 8;

-- 5 zadatak: Покушајте да преименујете колону city у home_city. Шта је потребно да би успело?
DESCRIBE teams_copy;

ALTER TABLE teams_copy RENAME COLUMN city TO home_city; -- ovde vidi city kolonu kao gresku jer smo promenili ime kolone

-- Mora da se omoguci mapiranje  Delta tabele
ALTER TABLE teams_copy SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name');

ALTER TABLE teams_copy RENAME COLUMN city TO home_city; -- ovde vidi city kolonu kao gresku jer smo promenili ime kolone

DESCRIBE teams_copy;