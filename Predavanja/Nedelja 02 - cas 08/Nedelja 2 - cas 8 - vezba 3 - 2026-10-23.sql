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