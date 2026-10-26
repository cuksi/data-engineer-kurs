USE bootcamp.northern_star;

-- ================================== A. Popravite upit ==================================
-- 1 zadatak: „Број утакмица сваког судије, укључујући судије без утакмица“:
SELECT r.referee_name, COUNT(*) AS matches
FROM referees r LEFT JOIN matches m ON r.referee_id = m.referee_id
GROUP BY r.referee_name;

-- resenje
SELECT r.referee_name, COUNT(m.match_id) AS matches
FROM referees r LEFT JOIN matches m ON r.referee_id = m.referee_id
GROUP BY r.referee_name;
-- Posto u COUNT nije bila izabrana kolona onda je brojao i NULL vrednosti

-- 2 zadatak: „Сваки тим у свакој утакмици, један ред по тиму“:
SELECT season, home_goals AS goals_for, away_goals AS goals_against FROM matches
WHERE status = 'played'
UNION
SELECT season, away_goals, home_goals FROM matches WHERE status = 'played';

-- resenje
SELECT season, home_goals AS goals_for, away_goals AS goals_against FROM matches
WHERE status = 'played'
UNION ALL
SELECT season, away_goals, home_goals FROM matches WHERE status = 'played';
-- Posto treba za svaki tim onda koristimo UNION ALL zato sto UNION brise duplikate, a UNION ALL obuhvata sve podatke

-- 3 zadatak: „Утакмице на дан када домаћи тим није имао тренера“:
SELECT m.match_id, m.kickoff_ts
FROM matches m
LEFT JOIN manager_spells ms
ON ms.team_id = m.home_team_id
AND DATE(m.kickoff_ts) BETWEEN ms.start_date AND ms.end_date
WHERE ms.spell_id IS NULL;

-- resenje
SELECT m.match_id, m.kickoff_ts
FROM matches m
LEFT JOIN manager_spells_clean msc
ON msc.team_id = m.home_team_id
AND DATE(m.kickoff_ts) BETWEEN msc.start_date AND COALESCE(msc.end_date, '9999-12-31')
WHERE msc.spell_id IS NULL;
-- BETWEEN ne radi kada ima NULL za datum

-- 4 zadatak: „Најбољи стрелци сезоне 2024/25“:
SELECT p.first_name, p.last_name, COUNT(*) AS goals
FROM match_events e
JOIN players p ON e.player_id = p.player_id
JOIN matches m ON e.match_id = m.match_id
WHERE m.season = '2024/25' AND e.event_type IN ('goal', 'penalty_goal')
GROUP BY p.first_name, p.last_name
ORDER BY goals DESC;

-- resenje
SELECT e.player_id, p.first_name, p.last_name, COUNT(*) AS goals
FROM match_events e
JOIN players p ON e.player_id = p.player_id
JOIN matches m ON e.match_id = m.match_id
WHERE m.season = '2024/25' AND e.event_type IN ('goal', 'penalty_goal')
GROUP BY e.player_id, p.first_name, p.last_name
ORDER BY goals DESC;
-- zato sto GROUP BY treba da se radi po player_id zato sto je on jedinstven, dok imena nisu

-- 5 zadatak: „Утакмице без стрелца првог гола“:
SELECT COUNT(*) FROM matches_flat WHERE first_goal_scorer = NULL;

-- resenje
SELECT COUNT(*) FROM matches_flat WHERE first_goal_scorer = NULL;