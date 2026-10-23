USE bootcamp.northern_star;

-- 1 zadatak : Za svaku sezonu prikažite ukupan broj utakmica, ukupan broj postignutih golova i prosečan broj golova po utakmici.
SELECT
    season,
    COUNT(*) AS `Ukupan broj utakmica`,
    SUM(home_goals + away_goals) AS `Ukupan broj golova u sezoni`,
    ROUND(`Ukupan broj golova u sezoni` / `Ukupan broj utakmica`, 2) AS `Prosecan broj golova po utakmici`
FROM matches_flat
GROUP BY season;

-- 2 zadatak: Za svaki stadion prikažite najmanju, najveću i prosečnu zabeleženu posetu, kao i broj utakmica za koje je poseta poznata.
SELECT
    stadium_name,
    MIN(attendance) AS `Najmanja posecenost`,
    MAX(attendance) AS `Najveca posecenost`,
    ROUND(AVG(attendance), 2) AS `Prosecna posecenost`,
    count(attendance) AS `Broj utakmmica za posete`
FROM matches_flat
GROUP BY stadium_name;

-- 3 zadatak: Prikažite sudije koje su sudile najmanje 10 utakmica i koje su ukupno pokazale najmanje 20 žutih kartona. Prikažite ime sudije, broj utakmica i ukupan broj žutih kartona.
SELECT
    referee_name,
    COUNT(referee_name) AS `Broj utakmica sudije`,
    SUM(home_yellow_cards) + SUM(away_yellow_cards) AS `Ukupan broj zutih kartona`
FROM matches_flat
GROUP BY referee_name
HAVING `Broj utakmica sudije` >= 10 AND `Ukupan broj zutih kartona` >= 20
ORDER BY `Ukupan broj zutih kartona` DESC;

--4 zadatak: Podelite utakmice prema ukupnom broju golova na kategorije Bez golova (0), Malo golova (1 ili 2) i Mnogo golova (3 ili više). 
-- Prikažite broj utakmica u svakoj kategoriji i najveći broj golova na utakmici u toj kategoriji.
SELECT
    CASE WHEN (home_goals + away_goals = 0) THEN 'Bez golova'
         WHEN (home_goals + away_goals IN (1,2)) THEN 'Malo golova' 
         ELSE 'Mnogo golova' END AS katergorije,
    COUNT(home_goals) AS `Ukupan broj broj utakmica`,
    MAX(home_goals + away_goals) AS `Najvise golova u utakmici`
FROM matches_flat
GROUP BY katergorije;

-- 5 zadatak: Za svaki klub prikažite broj utakmica koje je odigrao kao domaćin, broj pobeda kod kuće i broj poraza kod kuće. U rezultat uključite samo klubove koji su kod kuće odigrali najmanje 10 utakmica.
SELECT
    home_team,
    COUNT(home_team) AS `Broj utakmica kao domacin`,
    SUM(
        CASE WHEN home_goals > away_goals THEN 1 END
    ) AS `Pobeda kao domacin`,
    SUM(
        CASE WHEN home_goals < away_goals THEN 1 END
    ) AS `Izgubljenih kao domacin`
FROM matches_flat
GROUP BY home_team
HAVING `Broj utakmica kao domacin` >= 10;

-- 6 zadatak: Za svakog sudiju prikažite ukupan broj utakmica, broj utakmica u kojima je pokazao bar jedan crveni karton i procenat takvih utakmica u odnosu na sve utakmice koje je sudio.
-- TREBA ISPRAVKA ZADATKA
SELECT
    referee_name,
    COUNT(referee_name) AS `Broj utakmica sudije`,
    SUM(
        CASE WHEN home_red_cards + away_red_cards > 0 THEN 1 ELSE 0 END  -- jedno resenje sa SUM ali preko CASE WHEN
    ) AS red_card_games_reff
    ROUND((red_card_games_reff / `Broj utakmica sudije`) * 100.0, 2) AS `Procenta utakmica`
FROM matches_flat
GROUP BY referee_name;

-- 7 zadatak: Za svaku sezonu prikažite broj pobeda domaćina, broj nerešenih utakmica i broj pobeda gostiju. Takođe prikažite procenat utakmica koje su završene nerešenim rezultatom.
SELECT
    season,
    COUNT_IF(home_goals > away_goals) AS `Pobeda domacina`,
    COUNT_IF(home_goals = away_goals) AS `Nereseno`,
    COUNT_IF(home_goals < away_goals) AS `Pobeda gostiju`,
    ROUND((`Nereseno` / (`Pobeda domacina` + `Nereseno` + `Pobeda gostiju`)) * 100.0, 2) AS `Procenat neresenih`
FROM matches_flat
GROUP BY season;