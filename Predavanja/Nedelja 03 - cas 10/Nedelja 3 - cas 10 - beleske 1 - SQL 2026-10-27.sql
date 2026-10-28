USE bootcamp.northern_star;

SELECT
    kickoff_ts,
    LEAD(kickoff_ts) OVER(PARTITION BY team_id ORDER BY kickoff_ts) AS a
FROM team_matches;

SELECT
    kickoff_ts,
    LAG(kickoff_ts, 2) OVER(PARTITION BY team_id ORDER BY kickoff_ts) AS a  -- ovo je sa korakom
FROM team_matches;

SELECT
    goals_against,
    LAG(goals_against, 2, 5) OVER(PARTITION BY team_id ORDER BY kickoff_ts) AS a  -- ovo je sa korakom i sa DEFAULT (to je broj 5 iz naseg primera) vrednoscu koja ce biti umesto NULL
FROM team_matches;

SELECT
    goals_against,
    LAG(goals_against, 8) OVER(PARTITION BY team_id ORDER BY kickoff_ts) AS a  -- kada nam je korak 8 onda imamo 8 NULL vrednosti tek deveti kupi vrednost od prvog
FROM team_matches;

SELECT
    points,
    SUM(points) OVER(PARTITION BY team_id ORDER BY kickoff_ts
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS a   -- ovo sabira od pocetka (ovo znaci od pocetka UNBOUNDED PRECEDING) do trenutnog reda (ovo znaci do trenutnog red CURRENT ROW)
FROM team_matches;

SELECT
    points,
    SUM(points) OVER(PARTITION BY team_id ORDER BY kickoff_ts
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS a   -- ovo UNBOUNDED PRECEDING i CURRENT ROW moze da se menja, ima da biramo korak napred i nazad, znaci SVE levo i desno od AND moze da se bira i menja po zelji
FROM team_matches;

-- Zadatak: koliko je dana proslo izmedju dve uzastopne utakmice u sezoni 2024/25
SELECT
    season,
    team_id,
    kickoff_ts,
    LAG(kickoff_ts) OVER(PARTITION BY season, team_id ORDER BY kickoff_ts) AS prev_kickoff_ts,  -- ako nestavimo ORDER BY kickoff_ts onda bi svuda bila ista vrednost
    DATEDIFF(kickoff_ts, LAG(kickoff_ts) OVER(PARTITION BY season, team_id ORDER BY kickoff_ts)) AS rest_days -- daje razliku izmedju dva datuma
FROM team_matches
WHERE season = '2024/25'
ORDER BY rest_days;

-- Zadatak: za svaku utakmicu u sezoni 2024/25 racunamo ukupoan broj golova a onda kumulativni broj golova
SELECT
    match_id,
    kickoff_ts,
    home_goals + away_goals AS goals,

    SUM(home_goals + away_goals) OVER(ORDER BY kickoff_ts) AS running_default,

    SUM(home_goals + away_goals) OVER(ORDER BY kickoff_ts, match_id RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_rows  -- Ovde je koristen RANGE umesto ROW potraziti objasnjenje na netu
    -- Objasnjenje profe:  RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW" - ово је default ако не ставимо ништа (а не ROWS) 
                        -- RANGE ће вредности где имамо исти број (goals = 4) у исто време "комбиновати" (сабрати све вредности), уместо један по један као што ради ROWS
    
FROM matches
WHERE season = '2024/25'
ORDER BY kickoff_ts, match_id;

--Zadatak: kako se menja pozicija tima nakon svake odigrane utakmice
WITH running AS (
    SELECT
        season,
    team_id,
    kickoff_ts,
    row_number() OVER w AS games_played,
    SUM(points) OVER w AS pts_so_far
    FROM team_matches
    WINDOW w AS(
        PARTITION BY season, team_id
        ORDER BY kickoff_ts, match_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        )
),
positions AS(
    SELECT *,
        RANK() OVER(
            PARTITION BY season, games_played
            ORDER BY pts_so_far DESC
        ) AS position
    FROM running
)

SELECT
    season, team_id, games_played, pts_so_far, position,
    LAG(position) OVER (PARTITION BY season, team_id ORDER BY games_played) - position AS places_moved
FROM positions;