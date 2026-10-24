USE bootcamp.northern_star;

-- Изаберите један клуб и анализирајте његову сезону 2024/25. Сваки упит почните истим кораком, тако да за други клуб мењате само име:

-- 1 deo zadatka: Сезона у бројевима: утакмице, победе, нерешене, порази, дати и примљени голови, бодови.
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT
    c.team_id,
    COUNT(DISTINCT m.match_id) AS ukupan_broj_utakmica,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals > m.away_goals THEN 1 
             WHEN m.away_team_id = c.team_id AND m.home_goals < m.away_goals THEN 1 END
    ) AS wins,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1
             WHEN m.away_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1 END
    ) AS draws,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals < m.away_goals THEN 1 
             WHEN m.away_team_id = c.team_id AND m.home_goals > m.away_goals THEN 1 END
    ) AS loses,
    SUM(
        CASE WHEN m.home_team_id = c.team_id THEN m.home_goals
             WHEN m.away_team_id = c.team_id THEN m.away_goals END
    ) AS dati_golovi,
    SUM(
        CASE WHEN m.home_team_id = c.team_id THEN m.away_goals
             WHEN m.away_team_id = c.team_id THEN m.home_goals END
    ) AS primljeni_golovi,
    (wins * 3) + (draws * 1) AS ukupno_bodova
FROM club c
JOIN matches m ON m.home_team_id = c.team_id OR m.away_team_id = c.team_id
WHERE m.season = '2024/25'
GROUP BY c.team_id;

-- POMOCNI QUERYS

-- select * from matches where home_team_id = 10 AND home_goals > away_goals AND season = '2024/25';  -- 8 pobeda kuci
-- select * from matches where away_team_id = 10 AND home_goals < away_goals AND season = '2024/25';  -- 6 pobeda u gostima   -- UKUPNO 14 POBEDA

-- select * from matches where home_team_id = 10 AND home_goals = away_goals AND season = '2024/25';  -- 6 neresenih
-- select * from matches where away_team_id = 10 AND home_goals = away_goals AND season = '2024/25';  -- 4 neresene UKUPNO 10 NERESENIH

-- select * from matches where home_team_id = 10 AND home_goals < away_goals AND season = '2024/25';  -- 5 izgubljenih kuci
-- select * from matches where away_team_id = 10 AND home_goals > away_goals AND season = '2024/25';  -- 9 izgubljenih u gostima   -- UKUPNO 14 IZGUBLJENE

-- select SUM(home_goals) from matches where home_team_id = 10 AND season = '2024/25';  -- 35 golova datih kuci
-- select SUM(away_goals) from matches where away_team_id = 10 AND season = '2024/25';  -- 25 golova datih u gostima UKUPNO DATIH GOLOVA 60

-- select SUM(away_goals) from matches where home_team_id = 10 AND season = '2024/25';  -- 24 golova primljenih kuci
-- select SUM(home_goals) from matches where away_team_id = 10 AND season = '2024/25';  -- 37 golova primljenih u gostima UKUPNO DATIH GOLOVA 61

-- 2 deo zadatka: Код куће и у гостима: исти бројеви, одвојено за домаће и гостујуће утакмице.
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT
    c.team_id,
    -- statistika za kuci
    COUNT(
        CASE WHEN m.home_team_id = c.team_id THEN 1 END
    ) AS played_at_home_games,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals > m.away_goals THEN 1 END
    ) AS wins_home,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1 END
    ) AS draws_home,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals < m.away_goals THEN 1 END
    ) AS lose_home,
    SUM(
        CASE WHEN m.home_team_id = c.team_id THEN m.home_goals END
    ) AS datih_golova_kuci,
    SUM(
        CASE WHEN m.home_team_id = c.team_id THEN m.away_goals END
    ) AS primljenih_golova_kuci,
    (wins_home * 3) + (draws_home * 1) AS ukupno_bodova_kuci,
    -- statistika za gostovanja
    COUNT(
        CASE WHEN m.away_team_id = c.team_id THEN 1 END
    ) AS gostovanja,
    COUNT(
        CASE WHEN m.away_team_id = c.team_id AND m.home_goals < m.away_goals THEN 1 END
    ) AS wins_away,
    COUNT(
        CASE WHEN m.away_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1 END
    ) AS draws_away,
    COUNT(
        CASE WHEN m.away_team_id = c.team_id AND m.home_goals > m.away_goals THEN 1 END
    ) AS lose_away,
    SUM(
        CASE WHEN m.away_team_id = c.team_id THEN m.away_goals END
    ) AS datih_golova_na_gostovanju,
    SUM(
        CASE WHEN m.away_team_id = c.team_id THEN m.home_goals END
    ) AS primljenih_golova_na_gostovanju,
    (wins_away * 3) + (draws_away * 1) AS ukupno_bodova_u_gostima
FROM club c
JOIN matches m ON m.home_team_id = c.team_id OR m.away_team_id = c.team_id
WHERE m.season = '2024/25'
GROUP BY c.team_id;

-- POMOCNI QUERYS

-- select * from matches where home_team_id = 10 AND season = '2024/25';  -- 19 utakmica kuci

-- 3 deo zadatka: Стрелци: три најбоља стрелца клуба и најбољи асистент.
-- goal ; penalty_goal

-- najbolji strelci
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT 
    c.team_id, me.player_id, p.first_name, p.last_name,
    COUNT(*) AS golovi
FROM match_events me
JOIN club c ON me.team_id = c.team_id
JOIN matches m ON m.match_id = me.match_id
JOIN players p ON p.player_id = me.player_id
WHERE m.season = '2024/25' AND me.event_type IN ('goal', 'penalty_goal')
GROUP BY me.player_id, p.first_name, p.last_name, c.team_id
ORDER BY golovi DESC LIMIT 5;

-- najvolji asistent
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT 
    c.team_id, me.related_player_id, p.first_name, p.last_name,
    COUNT(*) AS asistencije
FROM match_events me
JOIN club c ON me.team_id = c.team_id
JOIN matches m ON m.match_id = me.match_id
JOIN players p ON p.player_id = me.related_player_id
WHERE m.season = '2024/25' AND me.event_type = 'goal'
GROUP BY me.related_player_id, p.first_name, p.last_name, c.team_id
ORDER BY asistencije DESC LIMIT 3;

-- POMOCNI QUERYS

-- select 
--     me.player_id,
--     COUNT(*) AS golovi
-- from match_events me
-- JOIN matches m ON m.match_id = me.match_id 
-- where me.team_id = 10 AND m.season = '2024/25' AND event_type IN ('goal', 'penalty_goal')
-- GROUP BY me.player_id
-- order by golovi DESC;  -- 3 najbolja strelca: 293 = 10, 291 = 7, 278 = 6

-- select 
--     me.related_player_id,
--     COUNT(*) AS asistencije
-- from match_events me
-- JOIN matches m ON m.match_id = me.match_id 
-- where me.team_id = 10 AND m.season = '2024/25' AND event_type IN ('goal') AND related_player_id IS NOT NULL
-- GROUP BY me.related_player_id
-- order by asistencije DESC;  -- 3 najbolja strelca: 284 = 3, 278 = 3, 269 = 2

-- 4 deo zadatka: Дисциплина: картони клуба по утакмици у поређењу са просеком лиге по тиму по утакмици.
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT
    c.team_id,
    COUNT_IF(event_type IN ('yellow_card', 'second_yellow')) AS zutih_kartona,
    COUNT_IF(event_type = 'red_card') AS crvenih_kartona,
    (zutih_kartona + crvenih_kartona) AS ukupno_kartona_za_nas_tim,
    COUNT(DISTINCT me.match_id) AS broj_nastupa_naseg_tima,
    ROUND(ukupno_kartona_za_nas_tim / broj_nastupa_naseg_tima, 2) AS kartona_po_utakmici_naseg_kluba,
    (SELECT COUNT(match_id) FROM matches 
    WHERE status = 'played' AND season = '2024/25') AS ukupno_utakmica_u_ligi,
    (   SELECT
        COUNT(*)
        FROM match_events me
        JOIN matches m ON m.match_id = me.match_id
        WHERE m.season ='2024/25' AND me.event_type IN ('yellow_card', 'second_yellow', 'red_card')) AS ukupno_kartona_u_ligi,
    ROUND(ukupno_kartona_u_ligi / ukupno_utakmica_u_ligi, 2) AS prosek_kartona_lige
FROM match_events me
JOIN club c ON me.team_id = c.team_id
JOIN matches m ON m.match_id = me.match_id
WHERE m.season = '2024/25' 
GROUP BY c.team_id;

--5 deo zadatka: Тренери: ко је водио клуб у сезони и са колико бодова по утакмици.
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT
    c.team_id, msc.manager_name,
    COUNT(DISTINCT m.match_id) AS ukupan_broj_utakmica,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals > m.away_goals THEN 1 
             WHEN m.away_team_id = c.team_id AND m.home_goals < m.away_goals THEN 1 END
    ) AS wins,
    COUNT(
        CASE WHEN m.home_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1
             WHEN m.away_team_id = c.team_id AND m.home_goals = m.away_goals THEN 1 END
    ) AS draws,
    ROUND(
        ((wins * 3) + (draws * 1)) / ukupan_broj_utakmica, 
    2) AS bodova_po_utakmici
FROM club c
JOIN matches m ON m.home_team_id = c.team_id OR m.away_team_id = c.team_id
JOIN manager_spells_clean msc ON msc.team_id = c.team_id AND DATE(m.kickoff_ts) BETWEEN COALESCE(msc.start_date, DATE('2024-08-01')) AND COALESCE(msc.end_date, DATE('2025-05-31'))
WHERE m.season = '2024/25'
GROUP BY c.team_id, msc.manager_name;

-- POMOCNI QUERYS
-- select kickoff_ts, season from matches WHERE season ='2024/25' order by kickoff_ts, season; -- pocetak sezone 2024-08-17-00:00:00, kraj sezone 2025-05-18

-- 6 deo zadatka: Највећа победа и најтежи пораз.
-- Najtezi poraz
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
),
utakmica AS (
    SELECT
    m.match_id, th.team_name, ta.team_name,
    concat(m.home_goals, ' : ', m.away_goals) AS rezultat,
    m.match_report,
    CASE WHEN m.home_team_id = c.team_id THEN m.home_goals - m.away_goals
         ELSE m.away_goals - m.home_goals END AS gol_razlika
FROM club c
JOIN matches m ON m.home_team_id = c.team_id OR m.away_team_id = c.team_id
JOIN teams th ON th.team_id = m.home_team_id
JOIN teams ta ON ta.team_id = m.away_team_id
WHERE m.season = '2024/25'
)
SELECT
    *
FROM utakmica
ORDER BY utakmica.gol_razlika ASC LIMIT 3;

-- Najveca pobeda
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
),
utakmica AS (
    SELECT
    m.match_id, th.team_name, ta.team_name,
    concat(m.home_goals, ' : ', m.away_goals) AS rezultat,
    m.match_report,
    CASE WHEN m.home_team_id = c.team_id THEN m.home_goals - m.away_goals
         ELSE m.away_goals - m.home_goals END AS gol_razlika
FROM club c
JOIN matches m ON m.home_team_id = c.team_id OR m.away_team_id = c.team_id
JOIN teams th ON th.team_id = m.home_team_id
JOIN teams ta ON ta.team_id = m.away_team_id
WHERE m.season = '2024/25'
)
SELECT
    *
FROM utakmica
ORDER BY utakmica.gol_razlika DESC LIMIT 3;

-- select home_team_id, away_team_id, home_goals, away_goals from matches where season ='2024/25' and (home_team_id = 10 OR away_team_id = 10) order by (home_goals-away_goals) DESC;

-- 7 deo zadatka: Публика: просечна посета и попуњеност на домаћим утакмицама, и колико утакмица нема податак о посети.
WITH club AS (
    SELECT team_id FROM teams WHERE team_name = 'Lakeside Rangers'
)
SELECT
    c.team_id, s.stadium_name,
    COUNT(m.match_id) AS broj_utakmica,
    AVG(m.attendance) AS prosecna_poseta,
    COUNT_IF(m.attendance IS NULL) AS nema_podatak_o_poseti,
    ROUND((SUM(m.attendance) / (s.capacity * (broj_utakmica - nema_podatak_o_poseti))) * 100.0, 2) AS popunjenost_na_domacim_utakmicama
FROM club c
JOIN matches m ON m.home_team_id = c.team_id
JOIN stadiums s ON m.stadium_id = s.stadium_id
WHERE season = '2024/25'
GROUP BY c.team_id, s.stadium_name, s.capacity;