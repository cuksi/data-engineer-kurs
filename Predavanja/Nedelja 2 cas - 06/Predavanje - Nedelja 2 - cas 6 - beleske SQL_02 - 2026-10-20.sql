USE bootcamp.northern_star;

SELECT 
    t.team_name, s.stadium_name, t.stadium_id t_stadion, s.stadium_id AS s_stadion  -- ne mora AS moze krace da se pise
FROM teams t
FULL OUTER JOIN stadiums s ON s.stadium_id = t.stadium_id;  -- ovde ja moguce da postoji tim bez stadiona, i da postoji stadion bez tima jer je FULL OUTER JOIN

SELECT 
    t.team_name, s.stadium_name, t.stadium_id t_stadion, s.stadium_id AS s_stadion
FROM teams t
RIGHT JOIN stadiums s ON s.stadium_id = t.stadium_id;   -- ovde imamo stadion bez tima jer je RIGHT JOIN

SELECT 
    t.team_name, s.stadium_name, t.stadium_id t_stadion, s.stadium_id AS s_stadion  -- ne mora AS moze krace da se pise
FROM teams t
FULL OUTER JOIN stadiums s ON s.stadium_id = t.stadium_id
WHERE t.team_id IS NULL OR s.stadium_id IS NULL; -- ovde cemo dobiti tim bez stadiona, i stadion bez tima