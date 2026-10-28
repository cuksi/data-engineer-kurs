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

--===============================================================================================
-- Profino resenje:
SELECT
    stadium_name, AVG(attendance) AS avg_crowd,
    DENSE_RANK() OVER(ORDER BY AVG(attendance)) AS crowd_rank
FROM matches_flat
GROUP BY stadium_name
ORDER BY crowd_rank;
--===============================================================================================

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
--===============================================================================================
-- Profino resenje:
SELECT
    t.team_name, tm.goals_for, tm.goals_against, tm.kickoff_ts,
    tm.goals_for - tm.goals_against AS gol_razlika
    -- ROW_NUMBER() OVER(PARTITION BY tm.team_id ORDER BY tm.goals_for - tm.goals_against DESC, tm.kickoff_ts) AS rn    -- ovo smo komentirali i ovako necemo prikazati row number
FROM team_matches tm
JOIN teams t ON t.team_id = tm.team_id
WHERE tm.season = '2024/25' AND tm.result = 'W'
QUALIFY ROW_NUMBER() OVER(PARTITION BY tm.team_id ORDER BY tm.goals_for - tm.goals_against DESC, tm.kickoff_ts) = 1;
--===============================================================================================

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

--===============================================================================================
-- Profino resenje:
WITH goals AS (
SELECT
    m.season, e.player_id, COUNT(*) AS goals
FROM match_events e
JOIN matches m ON e.match_id = m.match_id
WHERE e.event_type IN ('goal', 'penalty_goal')
GROUP BY m.season, e.player_id
)
SELECT
    p.first_name, p.last_name, g.season, g.goals,
    DENSE_RANK() OVER(PARTITION BY g.season ORDER BY g.goals DESC) AS rank
FROM goals g
JOIN players p ON p.player_id = g.player_id
QUALIFY rank = 1;
--===============================================================================================

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

--===============================================================================================
-- Profino resenje:
SELECT
    season, referee_name,
    SUM(home_yellow_cards + away_yellow_cards) AS yellows,
    RANK() OVER(PARTITION BY season ORDER BY SUM(home_yellow_cards + away_yellow_cards) DESC) AS rank
FROM matches_flat
GROUP BY referee_name, season
QUALIFY rank <= 3
ORDER BY season, rank;
--===============================================================================================

--==========================================================================================================================================================================================
--================================================================ VEZBA 2 DRUGI DEO (Вежба 2 - SUM, AVG и COUNT са OVER) ==================================================================
--==========================================================================================================================================================================================

-- 1 zadatak: За сваку утакмицу прикажите посету и колико је изнад или испод просека свог стадиона. Која утакмица је највише изнад просека?
SELECT
    s.stadium_name AS stadion,
    m.attendance AS poseta,
    ROUND(
        poseta - AVG(attendance) OVER(PARTITION BY m.stadium_id ), 2) AS iznad_ispod_proseka
FROM matches m
JOIN stadiums s ON s.stadium_id = m.stadium_id
ORDER BY iznad_ispod_proseka DESC;

-- 2 zadatak: Који играч има највећи удео у минутима свог клуба у сезони 2024/25?
WITH po_igracu AS (
    SELECT
        pms.team_id, pms.player_id,
        SUM(minutes_played) AS minuti_po_igracu
    FROM player_match_stats pms
    JOIN matches m ON m.match_id = pms.match_id
    WHERE m.season = '2024/25'
    GROUP BY pms.team_id, pms.player_id
)
SELECT
    pi.team_id, t.team_name, pi.player_id, p.first_name, p.last_name, pi.minuti_po_igracu,
    SUM(pi.minuti_po_igracu) OVER(PARTITION BY pi.team_id) AS minuti_za_tim,
    ROUND((pi.minuti_po_igracu / minuti_za_tim) * 100.0 ,2) AS udeo_igraca
FROM po_igracu pi
JOIN players p ON p.player_id = pi.player_id
JOIN teams t ON t.team_id = pi.team_id
ORDER BY udeo_igraca DESC;
-- team_id	team_name	        player_id	    first_name	    last_name	    minuti_po_igracu	minuti_za_tim	    udeo_igraca
-- 3	    Ashford Rovers	    61	            Ibrahima	    Ndiaye	        3240	            37514	            8.64

--===============================================================================================
-- Profino resenje: Hint profe -> prosirujemo tabelu koja nam je najbliza resenju
WITH mins AS(
SELECT
    s.player_id, s.team_id,
    SUM(s.minutes_played) AS ukupno_minuta
FROM player_match_stats s
JOIN matches m ON m.match_id = s.match_id
WHERE season = '2024/25'    -- mogli smo i da stavimo da je match_id veci od 2000 zato sto tad pocinje nova sezona po podacima
GROUP BY player_id, team_id
)
SELECT
    m.player_id, m.ukupno_minuta ,m.team_id,
    SUM (m.ukupno_minuta) OVER(PARTITION BY m.team_id) AS ukupno_minuta_tim,
    ROUND(100 * m.ukupno_minuta / ukupno_minuta_tim, 2) AS pct
FROM mins m
ORDER BY pct DESC;
--===============================================================================================

-- 3 zadatak: Поред сваке утакмице прикажите колико утакмица је укупно судио њен судија. Колико је најмање, а колико највише?
SELECT
     m.match_id, m.referee_id, r.referee_name,
    COUNT(m.referee_id) OVER(PARTITION BY m.referee_id) AS ukupno_utakmica_sudija
FROM matches m
JOIN referees r ON r.referee_id = m.referee_id
ORDER BY ukupno_utakmica_sudija DESC;
-- Rezultat najmanje je sudjeno 40 utakmica a najvise 41 utakmica

-- 4 zadatak: Колики удео у укупном броју голова сезоне 2024/25 има сваки месец? Који месец има највећи удео?
WITH ukupno_golova AS (
    SELECT
        m.match_id, 
        m.kickoff_ts, 
        m.home_goals, m.away_goals, m.season,
        SUM(m.home_goals + m.away_goals) OVER() AS ukupno_golova
    FROM matches m
    WHERE m.season = '2024/25'
)
SELECT
    YEAR(ug.kickoff_ts) AS godina,
    MONTH(ug.kickoff_ts) AS mesec,
    SUM(ug.home_goals + ug.away_goals) AS golovi_po_mesecu,
    ROUND((golovi_po_mesecu / ukupno_golova) * 100.0, 2) AS udeo_meseca
FROM ukupno_golova ug
GROUP BY godina, mesec, ukupno_golova
ORDER BY godina, mesec;
-- Resenje decembar 13.28%