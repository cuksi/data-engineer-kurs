USE bootcamp.northern_star;

-- 1 zadatak: Ко је дао највише асистенција у сезони 2024/25? Пазите: асистент је у колони related_player_id.
SELECT
    me.related_player_id, p.first_name, p.last_name,
    SUM(
        CASE WHEN me.event_type = 'goal' THEN 1 END
    ) AS ukupno_asistencija
FROM match_events me
JOIN players p ON p.player_id = me.related_player_id
JOIN matches m ON m.match_id = me.match_id
WHERE season = '2024/25' AND me.related_player_id IS NOT NULL
GROUP BY me.related_player_id, p.first_name,p.last_name
ORDER BY ukupno_asistencija DESC;
-- Rezultat Pablo Fernández ukupno 9 asistencija

-- 2 zadatak: Колико голова су по сезонама дали нападачи (FW), везни (MF) и одбрамбени (DF) играчи? (bez autogolova)
SELECT
    m.season,
    SUM(
        CASE WHEN p.position = 'DF' AND (me.event_type = 'goal' OR me.event_type = 'penalty_goal') THEN 1 END   -- jedan nacin zapisa uslova, duzi
    ) as df,
    SUM(
        CASE WHEN p.position = 'MF' AND (me.event_type IN ('goal', 'penalty_goal')) THEN 1 END  -- drugi nacin zapisa, kraci
    ) as mf,
    SUM(
        CASE WHEN p.position = 'FW' AND (me.event_type IN ('goal', 'penalty_goal')) THEN 1 END   -- najbolje resenje je da smo stavili where uslov na kraju i onda mozemo da izbacimo ovde uslove
    ) as fw
FROM players p
JOIN match_events me ON me.player_id = p.player_id
JOIN matches m ON m.match_id = me.match_id
-- WHERE me.event_type IN ('goal', 'penalty_goal')  -- ako stavimo ovde ovaj uslov onda gore mozemo da izbacimo: me.event_type IN ('goal', 'penalty_goal') (i duzi i kraci nacin)
GROUP BY m.season;
-- Resenje:
-- season		df	mf	fw
-- 2023/24		126	352	532
-- 2024/25		138	370	525

-- 3 zadatak: Колика је укупна посета по граду стадиона? Који град је имао највише гледалаца?
SELECT
    s.city,
    SUM(m.attendance) AS ukupna_poseta,
    COUNT(DISTINCT s.stadium_name) as num_stadimus
FROM stadiums s
JOIN matches m ON s.stadium_id = m.stadium_id
GROUP BY s.city
ORDER BY ukupna_poseta DESC;
-- Rezultat: Grad -> Northport = 2 957 364 gledalaca

SELECT city, COUNT(stadium_name) FROM stadiums GROUP BY city;
select * from matches where stadium_id = 1;

-- 4 zadatak: Који стадион није угостио ниједну утакмицу у сезони 2024/25? Пазите где пишете услов за сезону.
SELECT
    s.stadium_name
FROM stadiums s
LEFT JOIN matches m ON s.stadium_id = m.stadium_id AND m.season = '2024/25'
WHERE m.match_id IS NULL;
-- Rezultat 1 tim: Fairhaven Lane

-- select distinct stadium_id from matches;
-- select stadium_id from stadiums;

-- 5 zadatak: Решите питање 5 из Вежбе 1 још једном, али са RIGHT JOIN. Да ли добијате исти број? 
SELECT
    COUNT(*)
FROM player_match_stats pms
RIGHT JOIN players p ON p.player_id = pms.player_id
WHERE pms.player_id IS NULL;
-- Isto 31, samo smo zamenili mesta tabelama. U prvom slucaju player_match_stats je bio desno a sad je levo i kad promenim smer LEFT -> RIGHT JOIN dobijemo isto.

-- 6 zadatak: CROSS JOIN табела referees и stadiums: колико комбинација судија–стадион је могуће, а колико се заиста догодило у табели matches?
SELECT
    *
FROM referees r
CROSS JOIN stadiums s;
-- Ukupno 440 kombinacija

SELECT
    r.referee_name, s.stadium_name
FROM referees r
JOIN matches m ON r.referee_id = m.referee_id
JOIN stadiums s ON m.stadium_id = s.stadium_id
GROUP BY r.referee_name, s.stadium_name;
-- Ukupno 332 stvarna slucaja

----------------------DODATNI ZADACI-----------------------

-- 1 zadatak: Који играч је одиграо највише минута у сезони 2024/25 и за који клуб?
SELECT
    p.first_name, p.last_name, p.player_id,
    SUM(pms.minutes_played) AS minuta_igrao
FROM player_match_stats pms
JOIN players p ON pms.player_id = p.player_id
JOIN matches m ON pms.match_id = m.match_id
JOIN teams t ON pms.team_id = t.team_id
WHERE m.season = '2024/25'
GROUP BY p.first_name, p.last_name, p.player_id
ORDER BY minuta_igrao DESC;
-- Rezultat 4 igraca sa 3240 minuta: Aaron Lowe; Jonas Müller; Ibrahima Ndiaye; Morgan Nolan

select * from players where first_name = 'Leo' AND last_name = 'Marsh'; -- Imaju dva igraca sa istim imenom a razlicitim player_id

-- 2 zadatak: Играчи који никад нису ушли у игру: спојите players и player_match_stats са условом minutes_played > 0, прво у WHERE, па у ON. Колико играча добијате у сваком случају и зашто?

-- Treba pojasnjenje zasto u resenju za WHERE slucaj stoji 0
SELECT
    p.player_id, p.first_name
FROM players p
LEFT JOIN player_match_stats pms ON p.player_id = pms.player_id
WHERE pms.minutes_played > 0;

SELECT
    COUNT(DISTINCT p.player_id)
FROM players p
LEFT JOIN player_match_stats pms ON p.player_id = pms.player_id AND pms.minutes_played > 0
WHERE pms.player_id IS NULL;

-- 3 zadatak: Који клуб је имао највише искључења (red_card и second_yellow) у обе сезоне?
-- second_yellow ; red_card
SELECT
    t.team_name,
    SUM(
        CASE WHEN me.event_type = 'second_yellow' THEN 1 
             WHEN me.event_type = 'red_card' THEN 1 
             ELSE 0 END
    ) AS ukupno_iskljucenja
FROM teams t
JOIN match_events me ON t.team_id = me.team_id
GROUP BY t.team_name
ORDER BY ukupno_iskljucenja DESC;
-- Rezultat po 7 iskljucenja: Northport City i Riverton Athletic

-- 4 zadatak: За сваки аутогол прикажите играча, клуб за који је играо на тој утакмици и клуб коме је гол признат. Савет: клуб играча је у player_match_stats.
-- own_goal
SELECT
    p.first_name, p.last_name, t.team_name AS klub_za_koji_igra, t_priznat.team_name AS kome_je_priznat,
    CASE WHEN me.event_type = 'own_goal' THEN 'Autogol' END AS autgoal
FROM match_events me
JOIN players p ON me.player_id = p.player_id    -- ovde je spojeno da je dat autogol i koji je igrac dao autogol (ovde sam dobio ime)
JOIN player_match_stats pms ON me.match_id = pms.match_id AND pms.player_id = me.player_id  -- ovde je povezan koja utakmica i koji igrac (ovde je dobije id kluba za koji je igrao)
JOIN teams t ON pms.team_id = t.team_id -- ovde je dobije klub za koji je igrao igrac sto je dao autogol
JOIN teams t_priznat ON t_priznat.team_id = me.team_id
WHERE event_type = 'own_goal';

-- select * from match_events where match_id = 1002 and event_type = 'own_goal';
-- select * from players where player_id = 160;
-- select * from player_match_stats where match_id = 1002 AND player_id = 160;
-- select * from teams where team_id = 6;