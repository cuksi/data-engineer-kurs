USE bootcamp.northern_star;

-- 1 zadatak: Prosek datih golova u poslednjih 5 utakmica, uz izričit okvir prozora. Koja je najveća vrednost? Računajte samo kada prozor zaista ima 5 utakmica.
SELECT
    tm.match_id, DATE(tm.kickoff_ts) AS zavrsetak_prozora, t.team_name,
    AVG(tm.goals_for) OVER(PARTITION BY tm.team_id ORDER BY tm.kickoff_ts ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS zadnjih_pet_utakmica,    -- uzima 4 poslednje i trenutnu utakmicu to daje zbir od 5 utakmica
    COUNT(tm.goals_for) OVER(PARTITION BY tm.team_id ORDER BY tm.kickoff_ts ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS broj_zadnjih_utakmica
FROM team_matches tm
JOIN teams t ON t.team_id = tm.team_id
QUALIFY broj_zadnjih_utakmica >= 5
ORDER BY zadnjih_pet_utakmica DESC;

-- 2 zadatak: Tekući zbir datih golova svakog kluba u sezoni 2024/25: ko je prvi stigao do 50 golova i kada?
WITH running AS (
    SELECT
    match_id,
    team_id,
    kickoff_ts,
    row_number() OVER w AS games_played,
    SUM(goals_for) OVER w AS goals_so_far
    FROM team_matches
    WHERE season = '2024/25'
    WINDOW w AS(
        PARTITION BY team_id
        ORDER BY kickoff_ts, match_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        )
)
SELECT
    p.kickoff_ts, p.match_id, p.team_id, t.team_name, p.games_played, p.goals_so_far
FROM running p
JOIN teams t ON t.team_id = p.team_id
WHERE p.goals_so_far >= 50
ORDER BY p.kickoff_ts, p.match_id;
-- Resenje
-- kickoff_ts	                        team_name	            games_played	    goals_so_far
-- 2025-01-18T15:00:00.000+00:00	    Kingsbridge City	    22	                51

-- 3 zadatak: Za svaku domaću utakmicu izračunajte promenu posećenosti u odnosu na prethodnu domaću utakmicu istog kluba u istoj sezoni. Gde je najveći pad i zašto?
WITH promena AS(
SELECT
    tm.match_id, DATE(tm.kickoff_ts) AS datum, tm.venue,
    tm.team_id, t.team_name,
    m.attendance AS posecenost,
    posecenost - LAG(attendance) OVER(PARTITION BY tm.team_id, tm.season ORDER BY tm.kickoff_ts) AS promena,
    m.match_report AS izvestaj_sa_meca
FROM team_matches tm
JOIN matches m ON m.match_id = tm.match_id
JOIN teams t ON t.team_id = tm.team_id
WHERE tm.venue = 'home'
)
SELECT
    *
FROM promena
WHERE promena IS NOT NULL
ORDER BY promena ASC;
-- Resenje:
-- match_id	    datum	        venue	    team_id	    team_name	        posecenost	    promena	    izvestaj_sa_meca
-- 1220	        2024-01-14	    home	    11	        Oakfield Town	    0	            -17864	    Oakfield Town and Fairhaven Town play behind closed doors