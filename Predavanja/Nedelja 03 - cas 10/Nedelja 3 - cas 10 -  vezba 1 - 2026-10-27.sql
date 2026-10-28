USE bootcamp.northern_star;

-- 1 zadatak: За сваки клуб у сезони 2024/25 израчунајте колико је голова дао више или мање него на претходној утакмици. Где је највећи скок?
SELECT
    tm.match_id, t.team_name, 
    tm.goals_for AS dati_golovi,
    tm.goals_for - LAG(goals_for, 1, 0) OVER(PARTITION BY tm.match_id ORDER BY goals_for) AS razlika_u_odnosu_na_prethodni_mec
FROM team_matches tm
JOIN teams t ON t.team_id = tm.team_id
WHERE season = '2024/25'
ORDER BY razlika_u_odnosu_na_prethodni_mec DESC;
-- Rezultat: 
-- match_id	    team_name	        dati_golovi	    razlika_u_odnosu_na_prethodni_mec
-- 2063	        Kingsbridge City	6	            6

-- 2 zadatak: Колико пута је клуб после победе победио и у следећој утакмици? Од колико победа после којих постоји следећа утакмица?
WITH pobede AS(
SELECT
    tm.team_id, t.team_name, DATE(tm.kickoff_ts) AS datum, tm.result,
    LEAD(tm.result) OVER(PARTITION BY tm.team_id, tm.season ORDER BY tm.kickoff_ts, tm.match_id) AS sledeci_mec
FROM team_matches tm
JOIN teams t ON t.team_id = tm.team_id
)
SELECT
    COUNT_IF(result = 'W' AND sledeci_mec IS NOT NULL) AS broj_meceva,
    COUNT_IF(result ='W' AND sledeci_mec = 'W') AS pobeda_posle_pobede
FROM pobede;
-- Resenje:
-- broj_meceva	    pobeda_posle_pobede
-- 553	            221