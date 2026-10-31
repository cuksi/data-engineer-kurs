USE bootcamp.sandbox;

-- SELECT * FROM matches_flat;

CREATE SCHEMA IF NOT EXISTS bootcamp.sandbox;

--CTAS
-- OR REPLACE kad hocemo da izmenimo ako vec postoji a ne da opet kreiramo
CREATE OR REPLACE TABLE bootcamp.sandbox.smatches_flat_copy AS    -- voditi racuna gde se nalazom gore iznad inace ce kreirati tamo gde se nalazimo   AKO HOCEMO KOD ZA LOKACIJU onda kucamo: USE bootcamp.sandbox;
SELECT * FROM bootcamp.northern_star.matches_flat;

-- DROP TABLE matches_flat_copy;   -- brisanje tabele

-- SELECT * FROM matches_flat_copy;

DESCRIBE TABLE bootcamp.northern_star.matches_flat;  -- opis tabele

CREATE OR REPLACE TABLE bootcamp.sandbox.season_target ( -- ako nema OR REPLACE izbacice gresku ako vec postoji tabela, ali ako se razlikuju podaci u tabelama onda nece biti greske nego ce izbrisati celu tabelu TAKO DA OBAVEZNO PISATI OR REPLACE
    team_id  INT,
    season STRING,
    target_position INT,
    target_points INT  
);

SELECT * FROM season_target;

-- DROP TABLE season_target; 

INSERT INTO season_target
VALUES (1, '2024/25', 1, 85), (2, '2024/25', 6, 60);    -- ako necemo neku vrednost upisamo NULL koju nemamo

-- INSERT INTO season_target (team_id, season)     -- a moze i ovako ako navedemo samo kolone koje hocemo da ubacimo onda unosimo samo one koje smo hteli
-- VALUES (1, '2024/25'), (2, '2024/25');

INSERT INTO season_target
SELECT DISTINCT home_team_id, '2025/26', 10, 50     -- ovde smo dodali default vrednosti koje nedostaju da upise
FROM matches_flat_copy WHERE season = '2024/25';

ALTER TABLE matches_flat_copy ADD COLUMNS (total_goals INT, result STRING);     -- komanda za dodavanje novi kolona, moze jedna ili vise. Ako nema DEFAULT vrednosti bice NULL

SELECT * FROM matches_flat_copy;    -- provera dodavanja kolone II naci

DESCRIBE matches_flat_copy;    -- provera dodavanja kolone II nacin

UPDATE matches_flat_copy
SET total_goals = home_goals + away_goals;  --  ovo je setovanje vrednosti unutar cele kolone, ovde moze da se koristi WHERE uslovi ako treba neko fino gadanje

SELECT
    match_id, home_goals, away_goals, total_goals   -- provera za SET iznad
FROM matches_flat_copy;

SELECT
    match_id, home_goals, away_goals, total_goals, result
FROM matches_flat_copy;

UPDATE matches_flat_copy
SET total_goals = home_goals + away_goals,
    result = CASE WHEN home_goals > away_goals THEN '1'
                  WHEN home_goals = away_goals THEN 'X'
                  WHEN home_goals < away_goals THEN '2' END; 

SELECT
    match_id, home_goals, away_goals, total_goals, result
FROM matches_flat_copy;     -- provera UPDATE gore iznad

-- ALTER TABLE matches_flat_copy ALTER COLUMN total_goals AFTER match_id;  -- ovo je komanda ako hocemo da promenimo redosled kolona u tabeli mozae AFTER gde je levo od AFTER kolonu koju pomeramo a desno ide posle koje kolone

-- ALTER TABLE matches_flat_copy ALTER COLUMN total_goals FIRST;   -- ovo je drugi nacin gde ce zeljena kolona biti prva u tabeli

SELECT match_id, result
FROM matches_flat_copy
WHERE match_id IN (SELECT match_id FROM matches_flat_copy WHERE total_goals = 0);    -- pre UPDATE praksa prvo proveriti pa UPDATE

UPDATE matches_flat_copy
SET result = 'bezveze'
WHERE match_id IN (SELECT match_id FROM matches_flat_copy WHERE total_goals = 0);    -- ovo je UPDATE sa WHERE uslovom

SELECT match_id, result
FROM matches_flat_copy
WHERE match_id IN (SELECT match_id FROM matches_flat_copy WHERE total_goals = 0); -- Pa posle UPDATE opet provera da li je sve kako treba, to je praksa

SELECT DISTINCT status FROM matches_flat_copy;

SELECT
    *
FROM matches_flat_copy
WHERE status = 'abandoned'; -- provera pre DELETE

DELETE FROM matches_flat_copy
WHERE status = 'abandoned'; -- brisanje

UPDATE matches_flat_copy SET attendance = 0;    -- ovo je namerna greska da bi uradili RESTORE

SELECT SUM(attendance) FROM matches_flat_copy;

DESCRIBE HISTORY matches_flat_copy;

SELECT SUM(attendance) FROM matches_flat_copy VERSION AS OF 4;  -- da proverimo sumu u verziji iz koje hocemo RESTORE pre nego sto ga uradimo

RESTORE TABLE matches_flat_copy TO VERSION AS OF 4; -- kako vracamo tabelu is history ako zeznemo nesto

INSERT INTO matches_flat_copy (match_id)    -- ako ovako uradimo INSERT dodace match_id vrednost ali ostale ce sve biti NULL
VALUES (9999);


--------------------------------- Primer kako se pravi zvezdasta sema----------------------------------------
CREATE OR REPLACE TABLE dim_team AS
SELECT  -- moglo je ovde DISTINCT onda ne bi trebao UNION ALL ali ovde moze da se desi da je jedan tim igrao samo u gostima pa smo zato stavili UNION ALL, a DISTINCT ide da nemam isti tim vise puta, posto su upisani dani meceva cele lige
    home_team_id AS team_id,
    home_team AS team_name,
    home_team_code AS team_code
FROM matches_flat_copy
UNION
SELECT
    away_team_id AS team_id,
    away_team AS team_name,
    away_team_code AS team_code
FROM matches_flat_copy;

SELECT * FROM dim_team;

CREATE OR REPLACE TABLE dim_referee AS
SELECT DISTINCT referee_id, referee_name
FROM matches_flat_copy
UNION
SELECT -1, 'Nije odredjen';

SELECT * FROM dim_referee;

CREATE OR REPLACE TABLE dim_stadium (
    stadium_key BIGINT GENERATED ALWAYS AS IDENTITY,   -- ovo je opcija da sam databricks dodaje id kada ga nema a da ga doda automatski
    stadium_name STRING, 
    stadium_capacity INT, 
    stadium_city STRING     
);

SELECT stadium_name, stadium_capacity, stadium_city FROM matches_flat_copy;

SELECT * FROM dim_stadium;

INSERT INTO dim_stadium (stadium_name, stadium_capacity, stadium_city)  -- ovo je kako popunjavamo gore kreiranu tabelu ali bez id-a koji je automatski generisao databrick
SELECT DISTINCT stadium_name, stadium_capacity, stadium_city FROM matches_flat_copy;

SELECT * FROM dim_stadium;

CREATE OR REPLACE TABLE dim_date AS
SELECT CAST(DATE_FORMAT(d, 'yyyyMMdd') AS INT) AS date_key,
       d                                       AS full_date,
       DATE_FORMAT(d, 'EEEE')                  AS weekday_name,
       DAYOFWEEK(d) IN (1, 7)                  AS is_weekend,
       CASE WHEN MONTH(d) >= 7 THEN CONCAT(YEAR(d), '/', SUBSTRING(CAST(YEAR(d) + 1 AS STRING), 3, 2))
            ELSE CONCAT(YEAR(d) - 1, '/', SUBSTRING(CAST(YEAR(d) AS STRING), 3, 2))
       END                                     AS season
FROM (SELECT EXPLODE(SEQUENCE(DATE'2023-07-01', DATE'2025-06-30', INTERVAL 1 DAY)) AS d);   -- ovde ubacimo datume od prve i zadnje utakmice u sezoni da dobijemo timeline, ova tabela nije vezana ni sa jednom drugom tabelom, kdobijamo kalendar

SELECT * FROM dim_date;

CREATE OR REPLACE TABLE fact_match AS
SELECT f.match_id, -- дегенерисана димензија
CAST(DATE_FORMAT(f.kickoff_ts, 'yyyyMMdd') AS INT) AS date_key,
f.home_team_id, f.away_team_id, -- обе показују на dim _team
s.stadium_key,
COALESCE (f.referee_id, -1) AS referee_id,
f.home_goals, f.away_goals, f.attendance,
f.home_yellow_cards, f.away_yellow_cards,
f.home_red_cards, f.away_red_cards
FROM matches_flat_copy f
JOIN dim_stadium s ON f.stadium_name = s.stadium_name