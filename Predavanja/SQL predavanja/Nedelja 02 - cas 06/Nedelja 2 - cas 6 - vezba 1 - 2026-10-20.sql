USE bootcamp.northern_star;

-- 1 zadatak: За утакмице сезоне 2024/25 прикажите датум, име судије и његову националност. Колико редова очекујете? Која националност судија се најчешће појављује?
SELECT
    date(m.kickoff_ts) AS datum,
    r.referee_name AS ime_sudije,
    r.nationality AS nacionalnost
FROM matches m
INNER JOIN referees r ON m.referee_id = r.referee_id
WHERE m.season = '2024/25';
-- Ukupno 380 rezultata

SELECT
    r.nationality AS nacionalnost,
    COUNT(r.nationality) AS broj_zemalja
FROM matches m
INNER JOIN referees r ON m.referee_id = r.referee_id
WHERE m.season = '2024/25'
GROUP BY nacionalnost
ORDER BY broj_zemalja DESC;
-- Najcesce se javlja England - 140 puta

-- 2 zadatak: Прикажите клубове и њихове стадионе са капацитетом. Колико редова враћа INNER JOIN, а колико LEFT JOIN? Који клуб има највећи стадион (order by)?
SELECT
    t.team_name,
    s.stadium_name,
    s.capacity
FROM teams AS t
INNER JOIN stadiums s ON s.stadium_id = t.stadium_id
ORDER BY s.capacity DESC;
-- INNER JOIN vraca 23 stadiona
-- Najveci stadion ima klub Northport United - stadion: Harbourside Park - kapacitet: 52 000
SELECT
    t.team_name,
    s.stadium_name,
    s.capacity
FROM teams AS t
LEFT JOIN stadiums s ON s.stadium_id = t.stadium_id
ORDER BY s.capacity DESC;
-- LEFT JOIN vraca 24 stadiona, Harbor City FC nema stadion

-- 3 zadatak: Колико голова је постигнуто главом (body_part = 'head') у свакој сезони (group by season)? Рачунајте и аутоголове.
SELECT
 m.season,
 SUM(CASE WHEN me.body_part = 'head' THEN 1 END) AS golovi_glavom
FROM match_events me
JOIN matches m ON m.match_id = me.match_id
GROUP BY m.season;
-- Rezultat u sezoni 2023/24 = 194 gola, u sezoni 2024/25 = 194 gola glavom.

-- 4 zadatak: Који играчи су добили највише жутих картона у сезони 2024/25 (рачунајте и други жути) (match_events)?
-- yellow_card ; second_yellow
SELECT
    p.first_name, p.last_name,
    SUM(
        CASE WHEN me.event_type = 'yellow_card' THEN 1 
             WHEN me.event_type = 'second_yellow' THEN 1 
             ELSE 0 END
        ) AS tot_yellow_cards
FROM match_events me
JOIN players p ON p.player_id = me.player_id
JOIN matches m ON m.match_id = me.match_id
WHERE m.season = '2024/25'
GROUP BY p.first_name, p.last_name
ORDER BY tot_yellow_cards DESC;
-- Najvise zutih kartona po 10 Lars Visser,  Callum Lawson i Javier Martínez.

-- 5 zadatak: Колико играча нема ни један ред у player_match_stats, односно никад нису били у саставу за утакмицу?
SELECT
    COUNT(*)
FROM players p
LEFT JOIN player_match_stats pms ON p.player_id = pms.player_id
WHERE pms.player_id IS NULL;
-- Rezultat 31, resio profa

SELECT COUNT(*) FROM players;   -- ovde vidimo da imamo 681 igrac
SELECT COUNT(DISTINCT player_id) FROM player_match_stats;  -- ovde vidimo da je upisano samo 650 igraca

--6 zadatak: Који судија је судио највише утакмица у којима је досуђен пенал (дат или промашен)?
-- penalty_goal ; penalty_miss
SELECT
    r.referee_name,
    SUM(
        CASE WHEN me.event_type = 'penalty_goal' THEN 1 
             WHEN me.event_type = 'penalty_miss' THEN 1 
             END
    ) AS tot_penalty
FROM referees AS r
LEFT JOIN matches m ON r.referee_id = m.referee_id
JOIN match_events me ON m.match_id = me.match_id
GROUP BY r.referee_name
ORDER BY tot_penalty DESC;
-- Rezultat Peter Lindgren ukupno 23 penala.