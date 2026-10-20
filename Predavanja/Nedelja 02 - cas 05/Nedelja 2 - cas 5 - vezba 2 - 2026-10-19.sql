USE bootcamp.northern_star;

-- 1 zadatak: Направите колону kickoff_slot: 'Рано' (почетак пре 14 h), 'Поподне' (од 14 до 17 h) и 'Вече' (од 17 h). Колико утакмица има у сваком термину?
SELECT
    CASE WHEN HOUR(kickoff_ts) < 14 THEN 'Rano'
         WHEN HOUR(kickoff_ts) BETWEEN 14 AND 16 THEN 'Popodne'
         WHEN HOUR(kickoff_ts) >= 17 THEN 'Vece' END AS kickoff_slot,
    COUNT(*) AS num_matches
FROM matches_flat
GROUP BY kickoff_slot;
-- Rezultat Rano = 74, Popodne = 573, Vece = 114

-- 2 zadatak: Разврстајте посету у категорије 'Без података' (NULL), 'Без публике' (0), 'Мала' (испод 20.000) и 'Велика', па избројте утакмице по категорији. Пазите на редослед WHEN услова.
SELECT
    CASE WHEN attendance = 0 THEN 'Bez publike'
         WHEN attendance < 20000 THEN 'Mala'
         WHEN attendance >= 20000 THEN 'Velika'
         ELSE 'Bez podataka' END AS `Posecenost`,
    COUNT(*)
FROM matches_flat
GROUP BY `Posecenost`;
--Rezultati: Velika = 475; Mala = 268; Bez podataka = 17; Bez publike = 1

-- 3 zadatak: За сваког судију прикажите број утакмица, број утакмица са бар једним црвеним картоном и тај удео у процентима. Ко има највећи удео?
SELECT
referee_name,
COUNT(*) AS `Ukupan broj utakmica`,
SUM(
    CASE WHEN (home_red_cards + away_red_cards) >= 1 THEN 1
     ELSE 0 END
     ) AS total_red_cards,
(total_red_cards / `Ukupan broj utakmica`) * 100 AS  red_card_percaentages_per_game
FROM matches_flat
GROUP BY referee_name
ORDER BY total_red_cards DESC;
-- Ukupno rezultata 19, Robert Kane i Craig Pawson-Lee po 8 utakmica - udeo utakmica sa crvenim kartonom 20% 

-- 4 zadatak: За сваку сезону: у колико утакмица је домаћин водио на полувремену, а у колико од њих је и победио?
SELECT
    season,
    SUM(
        CASE WHEN home_goals_ht > away_goals_ht  THEN 1 END
    ) AS host_lead_ht,
    SUM(
        CASE WHEN home_goals_ht > away_goals_ht AND home_goals > away_goals  THEN 1 END
    ) AS host_win
FROM matches_flat
GROUP BY season;
-- Rezultat: sezeona 2023/24: na poluvremenu 107, a na kraju 88
--           sezeona 2023/24: na poluvremenu 119, a na kraju 88

-- 5 zadatak:Разврстајте наслове: 'Касна драма' ако помињу late или stoppage, 'Пенал' ако помињу penalty, 'Црвени картон' ако помињу red card,  'Без наслова' ако наслова нема, а иначе 'Остало'.
--          Колико утакмица има у свакој категорији?
SELECT
    SUM(
        CASE WHEN match_report ILIKE '%late%' THEN 1 
             WHEN match_report ILIKE '%stoppage%' THEN 1 END
    ) AS `Kasna drama`,
    SUM(
        CASE WHEN match_report ILIKE '%penalty%' THEN 1 END
    ) AS `Penal`,
    SUM(
        CASE WHEN match_report ILIKE '%red card%' THEN 1 END
    ) AS `Crveni karton`,
    SUM(
        CASE WHEN match_report IS NULL THEN 1 END
    ) AS `Bez naslova`,
    COUNT(*) - `Kasna drama` - `Penal` - `Crveni karton` - `Bez naslova` AS `Ostalo`
FROM matches_flat;
-- Rezultat: Kasna drama = 55; Penal = 63; Crveni karton = 62, Bez naslova = 29; Ostalo 552

-----------------------------------------------------
------------------- DODATNI ZADACI-------------------
-----------------------------------------------------

-- 1 zadatak: Направите учинак у гостима за сезону 2024/25: за сваки клуб бодови освојени као гост. Који клуб је најбољи гост?
SELECT
    season, away_team,
    SUM(
        CASE WHEN home_goals < away_goals THEN 3
             WHEN home_goals = away_goals THEN 1
             ELSE 0 END
    ) AS bodovi
FROM matches_flat
WHERE season = '2024/25'    -- moze da se prikaze season i sa ovom komandom ali season more biti dodat u u GROUP BY
GROUP BY away_team, season
-- HAVING season = '2024/25'    -- a moze da se prikaze season i sa ovom komandom ali season more biti dodat u u GROUP BY
ORDER BY bodovi DESC;
-- Rezultat Pemberton United sa 43 poena

-- 2 zadatak: По месецима сезоне 2024/25: у ком проценту утакмица су оба тима дала гол? Који месец има највећи проценат?
SELECT
    season, date_format(kickoff_ts,'MMMM') AS mesec,
    SUM(
        CASE WHEN  home_goals > 0 AND away_goals > 0 THEN 1 END
        ) AS games_with_hom_awy_goals,
        (games_with_hom_awy_goals / COUNT(*)) * 100 AS per_month_percentage
FROM matches_flat
GROUP BY mesec, season
HAVING season = '2024/25'
ORDER BY games_with_hom_awy_goals DESC;
-- Rezultat: February - 28 utakmica - 70 %

-- 3 zadatak: Који стадион има највећу просечну попуњеност (посета у односу на капацитет), рачунајући само стадионе са бар 10 утакмица?
SELECT
    stadium_name,
    SUM(
        CASE WHEN stadium_name IS NOT NULL THEN 1 END
    ) as games_per_stadium,
    ROUND((AVG(attendance) / stadium_capacity) * 100, 1) AS `Prosecna popunjenost` -- OVO DAJE TACAN REZULTAT

    -- ROUND((SUM(attendance) / SUM(stadium_capacity)) * 100, 1) AS `Prosecna popunjenost`  -- ZASTO OVO NE DAJE ISTO RESENJE (JER MOZDA ZATO STO SUM PRESKACE NULL PA SE MENJA VREDNOST< JER IMAMO JEDNU ODLOZENU UTAKMICU)

FROM matches_flat
GROUP BY stadium_name, stadium_capacity
HAVING games_per_stadium >= 10
ORDER BY `Prosecna popunjenost` DESC;
-- Rezultat: Castle Grounds i Elmsworth Lane sa 88,9%

-- 4 zadatak: За сваку врсту времена (NULL нека буде 'непознато') прикажите број утакмица и колико их је завршено 0:0.
SELECT
    coalesce(weather, 'Nepoznato') AS vreme,
    SUM(
        CASE WHEN weather LIKE 'clear' THEN 1 
        WHEN weather LIKE 'rain' THEN 1
        WHEN weather LIKE 'wind' THEN 1
        WHEN weather LIKE 'fog' THEN 1
        WHEN weather LIKE 'snow' THEN 1
        ELSE 1 END
    ) AS ukupan_broj_utakmica,
    COUNT_IF(home_goals = 0 AND away_goals = 0) AS result_0_0
FROM matches_flat
GROUP BY coalesce(weather, 'Nepoznato');