-- 1 zadatak
SELECT 
    *,
    stadium_capacity - attendance AS empty_seats
FROM bootcamp.northern_star.matches_flat ORDER BY empty_seats DESC LIMIT 5;
-- Za prva tri rezultata zajednička su polja: 
-- season= 2024/25; home_team_id= 11; home_team= Oakfield Town; home_team_code= OKT; 
-- stadium_name= National Stadium; stadium_city= Centralia; stadium_capacity= 80000; 
-- weather= clear; home_manager= Oleg Luzhny; away_red_cards= 0; first_goal_added_time= null;

-- 2 zadatak
SELECT 
    DISTINCT referee_name,
    home_team
FROM bootcamp.northern_star.matches_flat
WHERE home_team = 'Riverton Athletic';
-- Ukupno je sudilo 15 različitih sudija.

-- 3 zadatak
SELECT 
    home_team, away_team, home_goals_ht,  away_goals_ht, home_goals, away_goals,
    home_goals - away_goals AS gols_diff
FROM bootcamp.northern_star.matches_flat
WHERE away_goals_ht > home_goals_ht AND ((home_goals - away_goals) > 0 );
-- U ukupno 15 utakmica gost je vodio na poluvremenu, a na kraju utakmice domaćin pobedio.

-- 4 zadatak
SELECT 
    home_team, away_team, home_goals_ht, away_goals_ht, home_goals, away_goals,
    (home_goals + away_goals) - (home_goals_ht + away_goals_ht) AS goals_second_half
FROM bootcamp.northern_star.matches_flat ORDER BY goals_second_half DESC LIMIT 1;
-- U utakmici Northport United vs Newbury Forest je palo najviše golova u drugom poluvremenu.
-- Rezultat na poluvremenu je bio 1 prema 0 za domaćina (Northport United).
-- Rezultat na kraju utakmice je bio 6 prema 3 za domaćina (Northport United).

-- 5 zadatak
SELECT 
    season, home_team, away_team, 
    stadium_name, stadium_city, weather
FROM bootcamp.northern_star.matches_flat
WHERE (weather = 'fog' OR weather = 'snow') AND season = '2023/24';
-- Ukupno je odigrano 25 utakmica po snegu ili kiši.

-- 6 zadatak
SELECT 
    kickoff_ts, season, home_team, away_team,
    home_goals, away_goals, stadium_name
FROM bootcamp.northern_star.matches_flat
WHERE (home_team = 'Northport United' OR away_team = 'Northport United') AND (home_team = 'Northport City' OR away_team = 'Northport City')
ORDER BY kickoff_ts;
-- Prvi derbi u sezoni 2023/24 pobedio je Northport United, u gostima.
-- Drugi derbi u sezoni 2023/24 bilo je nerešeno, bez pobednika.
-- Prvi derbi u sezoni 2024/25 pobedio je Northport City, kao domaćin.
-- Drugi derbi u sezoni 2024/25 pobedio je Northport United, kao domaćin.

-- 7 zadatak
SELECT 
    match_id,
    season, kickoff_ts,
    home_team, away_team
FROM bootcamp.northern_star.matches_flat
WHERE season = '2024/25'
ORDER BY kickoff_ts LIMIT 3;
-- Nakon provere polja kickoff_ts druga i treća utakmica imaju isto vreme početka.
-- Ali pošto je match_id jedinstven (unique) i dodeljuje se redom kako se koja utakmica unosi u bazu podataka, smatrećemo njega kao dokaz koja je utakmica druga a koja treća po redu.

-- 8 zadatak
SELECT 
    match_id, home_team, home_goals,
    away_team, away_goals, first_goal_scorer
FROM bootcamp.northern_star.matches_flat
WHERE first_goal_scorer = "Sean O'Neill";
-- U ukupno 2 utakmice prvi strelac je bio Sean O'Neill