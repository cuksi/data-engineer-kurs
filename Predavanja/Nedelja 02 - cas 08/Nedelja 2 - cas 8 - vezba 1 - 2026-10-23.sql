USE bootcamp.northern_star;

---------------------------------- ZAGREVANJE ----------------------------------

-- 1 zadatak: „Све утакмице у којима је први гол дао Mattéo O'Brien“:
-- ima greska ime igraca je naspisano iz dva stringa, zato sto koristi u imenu apostrof
SELECT * FROM matches_flat WHERE first_goal_scorer = 'Mattéo O''Brien';
-- Ispravka
SELECT * FROM matches_flat WHERE first_goal_scorer = "Mattéo O'Brien";

-- 2 zadatak: „Број утакмица од 1. до 26. децембра 2024“:
-- Ovde je problem kada koristimo BETWEEN racuna samo kad je sati 00:00 pa ce ostala vremena za te datume da preskoci
SELECT COUNT(*) FROM matches_flat
WHERE kickoff_ts BETWEEN '2024-12-01' AND '2024-12-26'; -- vraca 32

-- Ispravka
SELECT COUNT(*) FROM matches_flat
WHERE kickoff_ts > '2024-12-01' AND kickoff_ts < '2024-12-27'; -- vraca 42

-- 3 zadatak: „Колико утакмица је била голеада (5 или више голова)?“:
-- redosled uslova za golove, ako stavimo prvo >= 2 onda ce svi golovi biti ovde cak i ako ih je vise od 5
SELECT 
    CASE WHEN home_goals + away_goals >= 2 THEN 'Има голова'
         WHEN home_goals + away_goals >= 5 THEN 'Голеада'
         ELSE 'Тесно' END AS bucket,
    COUNT(*) AS matches
FROM matches_flat GROUP BY bucket;
--bucket	    matches
--Има голова	580
--Тесно	        181

-- Ispravka
SELECT 
    CASE WHEN home_goals + away_goals >= 5 THEN 'Голеада'
         WHEN home_goals + away_goals >= 2 THEN 'Има голова'
         ELSE 'Тесно' END AS bucket,
    COUNT(*) AS matches
FROM matches_flat GROUP BY bucket;

-- 4 zadatak: „Број домаћих утакмица сваког клуба у сезони 2024/25, укључујући клубове са 0 утакмица“:
-- Problem je WHERE uslov treba da se pomeri u ON uslov
SELECT 
    t.team_name,
    COUNT(m.match_id) AS home_matches
FROM teams t
LEFT JOIN matches m ON t.team_id = m.home_team_id
WHERE m.season = '2024/25'
GROUP BY t.team_name;

-- Ispravljeno
SELECT 
    t.team_name,
    COUNT(m.match_id) AS home_matches
FROM teams t
LEFT JOIN matches m ON t.team_id = m.home_team_id AND m.season = '2024/25'
GROUP BY t.team_name;

-- 5 zadatak: „Колико играча никад није дало асистенцију?“:
-- treba NULL da iskljucimo iz rezultata
SELECT 
    COUNT(*) 
FROM players
WHERE player_id NOT IN (SELECT related_player_id FROM match_events WHERE event_type IN ('goal', 'penalty_goal')); -- daje rezultat 0

-- Ispravljeno
SELECT 
    COUNT(*) 
FROM players
WHERE player_id NOT IN (SELECT related_player_id FROM match_events WHERE event_type IN ('goal', 'penalty_goal') AND related_player_id IS NOT NULL); -- daje rezultat 225

-- 6 zadatak:  „Укупна посета у сезони 2024/25“:
--Ne treba JOIN posto su svi podaci u matches
SELECT 
    SUM(m.attendance)
FROM matches m
JOIN player_match_stats s ON m.match_id = s.match_id
WHERE m.season = '2024/25'; -- 359120480

-- Ispravljeno
SELECT 
    SUM(m.attendance)
FROM matches m
WHERE m.season = '2024/25'; -- 8978012

--===========================================================================================================================================
--================================================================= VEZBA 1 =================================================================
--===========================================================================================================================================

---------------------------------------------------------------- Sesija 1 i 2 ----------------------------------------------------------------

-- 1 zadatak: Прикажите утакмице са више од 40.000 гледалаца у марту 2025. Колико их је?
SELECT
    *
FROM matches_flat
WHERE attendance > 40000 AND MONTH(kickoff_ts) = 3;
-- Rezultat 5

-- 2 zadatak: Прикажите све различите комбинације резултата (home_goals, away_goals) за одигране утакмице, сортиране по укупном броју голова. Колико различитих резултата постоји?
SELECT
    DISTINCT home_goals, away_goals
FROM matches_flat
WHERE home_goals IS NOT NULL AND away_goals IS NOT NULL
ORDER BY home_goals + away_goals;

-- 3 zadatak: Који стадиони у имену имају реч „Park“?
SELECT
    DISTINCT stadium_name
FROM matches_flat
WHERE stadium_name ILIKE '%Park%';
-- stadium_name
-- Harbourside Park
-- Stonebridge Park
-- Westmere Park
-- Pemberton Park
-- Valemont Park
-- Dunmore Park

-- 4 zadatak: Прикажите утакмице без податка о посети или о времену: датум, тимове, посету и време, а уместо NULL нека пише 'непознато'. Колико их је?
SELECT
    home_team, away_team, 
    COALESCE(CAST(attendance AS STRING), 'непознато'), 
    COALESCE(weather, 'непознато')
FROM matches_flat
WHERE attendance IS NULL AND weather IS NULL;
-- Rezultat 2

---------------------------------------------------------------- Sesija 3 i 4 ----------------------------------------------------------------

-- 1 zadatak: За сваког судију прикажите националност (из referees), број утакмица, просечан број голова и проценат победа домаћина. Код ког судије домаћини најчешће побеђују?
SELECT
    r.referee_name, r.nationality,
    COUNT(m.match_id) AS ukupno_utakmica,
    ROUND(SUM(m.home_goals + m.away_goals) / ukupno_utakmica, 2) AS prosecan_broj_golova,
    CASE WHEN ukupno_utakmica = 0 THEN 0 
         ELSE ROUND((COUNT_IF(m.home_goals > m.away_goals) / ukupno_utakmica )*100.0, 2) END AS procenat_pobeda_domacina
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id AND m.status = 'played'
GROUP BY r.referee_name, r.nationality
ORDER BY procenat_pobeda_domacina DESC;
-- Resenje: Samuel Achebe	Nigeria	39	2.87	53.85

-- 2 zadatak: Који клубови су у сезони 2024/25 имали више победа у гостима него код куће?
WITH home_away AS (
    SELECT
        home_team_id AS team,
        match_id, season,
        COUNT_IF(home_goals > away_goals) AS pobede
    FROM matches 
    WHERE status = 'played'
    GROUP BY team, match_id, season
    UNION ALL
    SELECT
        away_team_id AS team,
        match_id, season,
        COUNT_IF(home_goals < away_goals) AS pobede
    FROM matches 
    WHERE status = 'played'
    GROUP BY team, match_id, season
)
SELECT
    t.team_name,
    COUNT(*)
FROM teams t
JOIN home_away ha ON ha.team = t.team_id AND ha.season = '2024/25'
GROUP BY t.team_name;


-- 3 zadatak: Колико играча је давало голове у обе сезоне?
SELECT
    DISTINCT player_id
FROM match_events me
WHERE event_type IN ('goal', 'penalty_goal');