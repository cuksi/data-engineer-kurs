USE bootcamp.northern_star;

-- 1 zadatak
SELECT
    match_id, referee_name
FROM matches_flat
WHERE referee_name IN ('Daniel Price', 'Graham Sutton', 'Jonas Berg');
-- Sudili su ukupno 120 utakmica

-- 2 zadatak
SELECT
    match_id, attendance
FROM matches_flat
WHERE attendance BETWEEN 30000 AND 40000 AND season = '2024/25';
-- Ukupno 69 utakmica

-- 3 zadatak
SELECT
    DISTINCT home_team
FROM matches_flat
WHERE home_team LIKE 'N%';
-- Ukupno 3 tima: Northport United, Northport City, Newbury Forest

-- 4 zadatak
SELECT
    match_id, match_report
FROM matches_flat
WHERE match_report LIKE '%penalty%';
-- u ovom slucaju ne kontrolise reci gde je penalty napisan svim velikim slovima ili da je pocetno slovo veliko
-- ukupno 0

SELECT
    match_id, match_report
FROM matches_flat
WHERE match_report ILIKE '%penalty%';
-- Ovaj ignorise velika slova tj. sva su slova ista bila velika ili mala i onda prikazuje svude gde se pominje rec penalty.
-- Ukupno 63

-- 5 zadatak
SELECT
    match_id, weather, attendance
FROM matches_flat
WHERE weather IS NULL AND attendance IS NULL;
-- Ukupno 2 utakmica bez podataka

-- 6 zadatak
SELECT
    kickoff_ts, original_kickoff_ts,
    coalesce(original_kickoff_ts, kickoff_ts) AS planned_kickoff
FROM matches_flat
WHERE original_kickoff_ts IS NOT NULL;
-- Ukupno 2 utamice

SELECT
    kickoff_ts, original_kickoff_ts,
    coalesce(original_kickoff_ts, kickoff_ts) AS planned_kickoff
FROM matches_flat
WHERE coalesce(original_kickoff_ts, kickoff_ts) <> kickoff_ts; -- ovo je komanda za razlicito <>

-- 7 zadatak
-- 1 nacin za 7 zadatak
SELECT
    match_id, kickoff_ts
FROM matches_flat
WHERE kickoff_ts >= '2024-12-23' AND kickoff_ts < '2024-12-30';
-- Ukupno 19 utakmica

-- 2 nacin za 7 zadatak
SELECT
    match_id, kickoff_ts
FROM matches_flat
WHERE kickoff_ts BETWEEN '2024-12-23 00:00:00' AND '2024-12-29 23:59:59'; -- moze i ovako ali je bolja praksa kao u 1 nacinu vece manje

-- 8 zadatak
SELECT
    match_id, match_report
FROM matches_flat
WHERE match_report IS NULL;
-- Ukupno 29 utakmica