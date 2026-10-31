USE bootcamp.northern_star;

-- Utakmice sa stadionom
SELECT
*
FROM matches 
JOIN stadiums ON matches.stadium_id = stadiums.stadium_id;  -- AKO NAPISEMO SAMO JOIN ON JE PO DEFAULT-u INNER JOIN
-- LEVO JOIN DESNO - stao je levo od JOIN-a to je LEFT JOIN, AKO IMA VISE JOIN-a onda gledamo od trenutne sta je prethodno levo a sta je posle desno

SELECT
*
FROM matches AS m   -- ovo je primer kako se krace mogu nazivati tabele da ne kucam pun naziv za query
JOIN stadiums AS s ON m.stadium_id = s.stadium_id;

SELECT
m.match_id, m.kickoff_ts,
stadium_name, capacity, m.stadium_id    -- voditi racuna nekad mogu biti isti nazivi kolona u dve tabele a da znace nesto drugo. AKo su kolone jedinstvene onda ne treba da se definise. ALi bolja praksa da se tacno definise
FROM matches AS m
JOIN stadiums AS s ON m.stadium_id = s.stadium_id;

-- Timovi sa mecevim
SELECT
    h.team_name, a.team_name, m.home_goals, m.away_goals
FROM matches AS m 
JOIN teams AS h ON m.home_team_id = h.team_id   -- ovde je dva put join sa istom tabelom ali mora posto su u tabeli teams nema duplih podataka i onda stalno koristi isti id
JOIN teams AS a ON m.away_team_id = a.team_id;

SELECT DISTINCT
    event_type
FROM match_events;

-- Naci golove i asistencije (player_id je ko je dao gol, a related_player_id je onaj ko je napravio asistenciju)
SELECT
    p.first_name, p.last_name, 
    a.first_name, a.last_name,
    e.event_type, e.player_id, e.related_player_id
FROM match_events e -- za tabele ne mora AS moze samo razmak i onda alijas, ovo je kraci zapis
JOIN players p ON p.player_id = e.player_id
JOIN players a ON a.player_id = e.related_player_id -- posto je INNER JOIN ovde ce da fali neki podatak koji nema par, zato se dole ispod koristi LEFT JOIN DA BI POKAZAO SVE
WHERE e.event_type IN ('goal', 'penalty_goal');

SELECT
    p.first_name, p.last_name, 
    a.first_name, a.last_name,
    e.event_type, e.player_id, e.related_player_id
FROM match_events e -- za tabele ne mora AS moze samo razmak i onda alijas, ovo je kraci zapis
JOIN players p ON p.player_id = e.player_id
LEFT JOIN players a ON a.player_id = e.related_player_id
WHERE e.event_type IN ('goal', 'penalty_goal');

SELECT 
    r.referee_name,
    COUNT(*)    -- zato sto je ovde zvezda sve broji i gde je NULL sto ce pokazati kao jednu utakmica
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id  -- ovde moze da nas prevari jer sudija koji ima NULL prikazace jednu utakmicu posto je LEFT JOIN voditi racuna 
GROUP BY r.referee_name;

SELECT  -- ovo je za pomoc da proverimo ovo od gore
*
FROM referees
WHERE referee_name = 'Paul Tierney-Ross';

SELECT  -- ovde vidimo da nece nista vratiti za tog sudiju
    match_id
FROM matches
WHERE referee_id = 20;

SELECT 
    r.referee_name,
    COUNT(m.match_id)   -- ovde smo dodali kolonu iz tabele matches.match_id posto ce tu biti NULL i sad ga nece brojati
FROM referees r
LEFT JOIN matches m ON m.referee_id = r.referee_id
GROUP BY r.referee_name;