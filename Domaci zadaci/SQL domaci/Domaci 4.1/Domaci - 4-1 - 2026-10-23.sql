USE bootcamp.northern_star;

-- 1 zadatak: Koliko redova ima spoj matches i player_match_stats za sezonu 2024/25? Objasnite.
SELECT
    *
FROM matches m
JOIN player_match_stats pms ON pms.match_id = m.match_id
WHERE season = '2024/25';
-- Rezultat ima redova 15200. 
-- Objasnjenje: player_match_stats za sezonu 2024/25 ima 15200 redova bez spajanja matches. Ali kad spojimo imamo duple podatke za matches, zato sto se match_id ponavlja u player_match_stats (nije jedinstven)
-- posto imamo vise igraca po utakmici. Onda za svaki unos igraca sa iste utakmice imamo upisane podatke iz matches (koji su dupli). Posto nam je veza za tabele match_id koji se ponavlja u player_match_stats.

-- pomocni query ispod
select COUNT(match_id) from player_match_stats where;   -- vraca 30440
select COUNT(match_id) from matches where season='2024/25'; -- vraca 380

-- 2 zadatak: Koliko puta je igrač u istoj sezoni igrao za dva različita kluba?
WITH igraci_urazlicitim_klubovima AS(
    SELECT
        pms.player_id, m.season,
        COUNT(DISTINCT pms.team_id) broj_klubova
    FROM player_match_stats pms
    JOIN matches m ON m.match_id = pms.match_id
    GROUP BY pms.player_id, m.season
    HAVING broj_klubova > 1
)
SELECT COUNT(*) AS resenje FROM igraci_urazlicitim_klubovima;
-- Rezultat 35 puta.

-- 3 zadatak: Koliko utakmica ima više kartona od prosečne utakmice? Bez kartona računajte sa 0.
-- yellow_card ; second_yellow ; red_card
WITH suma AS (
    SELECT
        SUM(CASE WHEN event_type = 'yellow_card' THEN 1
                WHEN event_type = 'second_yellow' THEN 1
                WHEN event_type = 'red_card' THEN 1
                ELSE 0 END
        ) AS kartona_po_utakmici
    FROM match_events
),
po_utakmici AS(
    SELECT
        match_id,
        SUM(CASE WHEN event_type = 'yellow_card' THEN 1
                WHEN event_type = 'second_yellow' THEN 1
                WHEN event_type = 'red_card' THEN 1
                ELSE 0 END
        ) AS kartona_po_utakmici
    FROM match_events
    GROUP BY match_id
)
SELECT
    COUNT_IF(pu.kartona_po_utakmici > ((select * from suma)/ (select COUNT(*) from matches WHERE status = 'played'))) AS resenje
FROM matches m
JOIN po_utakmici pu ON pu.match_id = m.match_id;
-- Rezultat 370, verovatno moze prostije da se ne ponavlja upit. do tad ovo resenje :D

-- 4 zadatak: Koliko igrača je odigralo više od 10 utakmica u sezoni 2024/25?
WITH svi_igraci_iz_sezone AS (
    SELECT
        pms.player_id, m.season,
        COUNT(DISTINCT pms.match_id) AS broj_meceva
    FROM player_match_stats pms
    JOIN matches m ON m.match_id = pms.match_id
    WHERE m.season = '2024/25' AND pms.minutes_played > 0
    GROUP BY pms.player_id, m.season
)
SELECT
    COUNT(*) AS trazeni_igraci
FROM svi_igraci_iz_sezone i
WHERE i.broj_meceva > 10;
-- Rezultat 383 igraca je imalo vise od 10 utakmica u sezoni 2024/25.

-- 5 zadatak: Prikažite sve klubove koji su igrali u sezoni 2024/25, bilo kao domaćini ili kao gosti. Koristite UNION, a zatim izmenite upit tako da koristi UNION ALL. Objasnite razliku u broju redova koji dobijate.
WITH utakmice AS (
    SELECT
        home_team_id AS team_id
    FROM matches
    WHERE season = '2024/25'
    UNION
    SELECT
        away_team_id AS team_id
    FROM matches
    WHERE season = '2024/25'
)
SELECT
    t.team_name AS naziv_kluba
FROM utakmice u
JOIN teams t ON t.team_id = u.team_id;  -- vraca 20 rezultata

WITH utakmice AS (
    SELECT
        home_team_id AS team_id
    FROM matches
    WHERE season = '2024/25'
    UNION ALL
    SELECT
        away_team_id AS team_id
    FROM matches
    WHERE season = '2024/25'
)
SELECT
    t.team_name AS naziv_kluba
FROM utakmice u
JOIN teams t ON t.team_id = u.team_id;  -- vraca 760 rezultata
-- UNION spaja rezultate upita i uklanja duplikate, a UNION ALL spaja rezultate upita i zadrzava redova