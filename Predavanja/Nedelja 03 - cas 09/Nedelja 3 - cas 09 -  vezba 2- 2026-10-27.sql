----------------------------------------------------------------------------------------------------------------------------------------
-- Ovo je pokrenuto jedanpu da napravimo novi VIEW, stavljeno je u koment da se ne izvrsava svaki put kad pokrenemo neki drugi query
----------------------------------------------------------------------------------------------------------------------------------------
-- CREATE OR REPLACE VIEW bootcamp.northern_star.team_matches AS
-- WITH sides AS (
-- SELECT match_id, season, matchday, kickoff_ts,
-- home_team_id AS team_id, away_team_id AS opponent_id, 'home' AS
-- venue,
-- home_goals AS goals_for, away_goals AS goals_against
-- FROM bootcamp.northern_star.matches WHERE status = 'played'
-- UNION ALL
-- SELECT match_id, season, matchday, kickoff_ts,
-- away_team_id, home_team_id, 'away',
-- away_goals, home_goals
-- FROM bootcamp.northern_star.matches WHERE status = 'played'
-- )
-- SELECT *,
-- CASE WHEN goals_for > goals_against THEN 'W'
-- WHEN goals_for = goals_against THEN 'D' ELSE 'L' END AS result,
-- CASE WHEN goals_for > goals_against THEN 3
-- WHEN goals_for = goals_against THEN 1 ELSE 0 END AS points
-- FROM sides;
----------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------ KRAJ block-a za kreiranje novog VIEW-a ------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------

--=========================================================================================================================================================================================
--============================================================= VEZBA 2 PRVI DEO (Вежба 1 - OVER, PARTITION BY и рангирање) ===============================================================
--=========================================================================================================================================================================================

USE bootcamp.northern_star;

-- 1 zadatak: Рангирајте стадионе по просечној посети помоћу DENSE_RANK. Који су прва три?
WITH poseta_po_stadionu AS (
SELECT
    s.stadium_name AS ime_stadiona,
    ROUND(AVG(m.attendance), 2) AS prosecna_poseta
FROM stadiums s
JOIN matches m ON m.stadium_id = s.stadium_id
GROUP BY s.stadium_name
)
SELECT
    ime_stadiona, prosecna_poseta,
    DENSE_RANK() OVER(ORDER BY prosecna_poseta DESC) AS rnk
FROM poseta_po_stadionu
QUALIFY rnk <= 3;
-- Resenje:
-- ime_stadiona	            prosecna_poseta	    rnk
-- Harbourside Park	        44415.63	        1
-- Kingsbridge Stadium	    40091.05	        2
-- Northport Arena	        33409.74	        3

-- 2 zadatak: Пронађите највећу победу сваког клуба у сезони 2024/25 (највећа гол-разлика; ако их има више, најранија). Колико редова очекујете?
WITH gol_razlika_sezone AS(
SELECT
    t.team_name AS klub,
    tm.team_id id_kluba,
    goals_for AS dati_golovi,
    goals_against AS primljeni_golovi,
    DATE(tm.kickoff_ts) AS datum,
    goals_for - goals_against AS gol_razlika
FROM team_matches tm
JOIN teams t ON t.team_id = tm.team_id
WHERE season = '2024/25' AND (goals_for - goals_against) > 0
)
SELECT
    datum, klub, dati_golovi, primljeni_golovi, gol_razlika,
    ROW_NUMBER() OVER(PARTITION BY id_kluba ORDER BY gol_razlika DESC, datum) AS najveca
FROM gol_razlika_sezone
QUALIFY najveca = 1
ORDER BY datum;

-- Pomocni query
-- select team_id, goals_for from team_matches where team_id = 7 AND goals_for >= 6;

-- 3 zadatak: Ко је најбољи стрелац сваке сезоне?
WITH strelci AS(
SELECT
    me.player_id AS id_igraca,
    m.season AS sezona,
    COUNT(me.event_type) AS golova_po_igracu
FROM match_events me
JOIN matches m ON m.match_id = me.match_id
WHERE me.event_type IN ('goal', 'penalty_goal')
GROUP BY me.player_id, sezona
)
SELECT
    s.sezona, p.first_name, p.last_name, s.golova_po_igracu,
    RANK() OVER(PARTITION BY s.sezona ORDER BY s.golova_po_igracu DESC) AS rk   -- Bolje RANK() nego ROW_NUMBER() zato sto ROW_NUMBER() vraca samo prvog, dok ce RANK() vratiti ako vise njih deli prvo mesto
FROM strelci s
JOIN players p ON p.player_id = s.id_igraca
QUALIFY rk = 1
ORDER by s.sezona ASC, s.golova_po_igracu DESC;

-- 4 zadatak: Прве три судије по броју показаних жутих картона у свакој сезони. Шта се дешава ако двојица имају исти број?
WITH sudije AS(
SELECT
    r.referee_id AS id_sudije,
    m.season AS sezona,
    COUNT(me.event_type) AS kartona_po_sezoni
FROM match_events me
JOIN matches m ON m.match_id = me.match_id
JOIN referees r ON r.referee_id = m.referee_id
WHERE me.event_type IN ('yellow_card', 'second_yellow')
GROUP BY id_sudije, sezona
)
SELECT
    s.sezona, r.referee_name, s.kartona_po_sezoni,
    RANK() OVER(PARTITION BY s.sezona ORDER BY s.kartona_po_sezoni DESC) AS rk   -- Bolje RANK() nego ROW_NUMBER() zato sto ROW_NUMBER() vraca samo prvog, dok ce RANK() vratiti ako vise njih deli prvo mesto
FROM sudije s
JOIN referees r ON r.referee_id = s.id_sudije
QUALIFY rk <=3
ORDER by s.sezona ASC, s.kartona_po_sezoni DESC;

--==========================================================================================================================================================================================
--================================================================ VEZBA 2 DRUGI DEO (Вежба 2 - SUM, AVG и COUNT са OVER) ==================================================================
--==========================================================================================================================================================================================

-- 1 zadatak: За сваку утакмицу прикажите посету и колико је изнад или испод просека свог стадиона. Која утакмица је највише изнад просека?
