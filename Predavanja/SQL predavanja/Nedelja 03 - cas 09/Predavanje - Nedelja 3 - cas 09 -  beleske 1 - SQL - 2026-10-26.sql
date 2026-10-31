USE bootcamp.northern_star;

SELECT opstina, bm, glasali
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali);

SELECT
    SUM(glasali)
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali);

SELECT
    opstina,
    SUM(glasali)
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali)
GROUP BY opstina;

-- ovde je primer kako se koristi OVER a ovo iznad su stari nacini kako smo radili nesto slicno
SELECT 
    opstina, bm, glasali,
    SUM(glasali) OVER (PARTITION BY opstina) AS ukupno_opstina
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali);

-- CTE nacin a dole je QUALIFY nacin ispod primer
WITH glasovi_prosireno AS(
SELECT 
    opstina, bm, glasali,
    SUM(glasali) OVER (PARTITION BY opstina) AS ukupno_opstina
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali)
)
SELECT * FROM glasovi_prosireno
WHERE ukupno_opstina > 250;

SELECT 
    opstina, bm, glasali,
    SUM(glasali) OVER (PARTITION BY opstina) AS ukupno_opstina
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali)
QUALIFY ukupno_opstina > 250;   -- Ovo je primena QUALIFY-a da izbegnom gornji nacin gde smo pravili CTE

-- SUM, AVG, COUNT, MIN, MAX, COUNT_IF
-- ROW_NUMBER, RANK, DENSE_RANK     -- ovo moze da se koristi samo kad se stavi ORDER BY U zagradu za OVER
-- LAG, LEAD, FIRST_VALUE, LAST_VALUE   -- ovo moze da se koristi samo kad se stavi ORDER BY U zagradu za OVER

SELECT 
    opstina,
    AVG(glasali)
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali)
GROUP BY opstina;   -- ovako smo pre radili

SELECT 
    opstina, bm, glasali,
    100 * glasali / SUM(glasali) OVER(PARTITION BY opstina) AS udeo_u_procentima,
    ROW_NUMBER() OVER (PARTITION BY opstina ORDER BY glasali DESC, bm DESC) AS rn,    -- ovo rn je skraceno ROW NUMBER -- ovde smo dodali jos jednu vrednost unutar ORDER BY dodali smo bm
    RANK() OVER (PARTITION BY opstina ORDER BY glasali DESC) AS rnk,    -- ovo rn je skraceno RANK
    DENSE_RANK() OVER (PARTITION BY opstina ORDER BY glasali DESC) AS dense,     -- ovo rn je skraceno DENSE RANK
    LAG(glasali) OVER (PARTITION BY opstina ORDER BY glasali DESC) AS prethodni,    -- prepisuje prethodnu vrednost, red iznad, u zagradi LAG-a pise koji kolonu gledamo
    LEAD(glasali) OVER (PARTITION BY opstina ORDER BY glasali DESC) AS naredni      -- prepisuje sledecu vrednost, red ispod, u zagradi LAG-a pise koji kolonu gledamo
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali);
-- ORDER BY glasali;   -- ovaj ORDER BY Nema veze sa onim ORDER BY-om iz OVER zagrade, ovaj ce da slaze kao pre


SELECT 
    opstina, bm, glasali,
    100 * glasali / SUM(glasali) OVER() AS udeo_u_procentima,   -- kad nemamo PARTITION BY u OVER zagradi onda gleda celu tabelu, a kad ima PARTITION BY onda se ponasa kao GROUP BY
    ROW_NUMBER() OVER (ORDER BY glasali DESC, bm DESC) AS rn,
    RANK() OVER (ORDER BY glasali DESC) AS rnk_all,
    RANK() OVER (ORDER BY glasali DESC) AS rnk_opstina,
    DENSE_RANK() OVER (ORDER BY glasali DESC) AS dense,
    LAG(glasali) OVER (ORDER BY glasali DESC) AS prethodni, -- ovaj kasni za celom tabelom posto nema PARTIION BY, da ima PARTITION BY onda bi kasnio uunutar grupe
    LAG(opstina) OVER (ORDER BY opstina DESC) AS prethodni_opstine,
    LEAD(glasali) OVER (ORDER BY glasali DESC) AS naredni
FROM VALUES ('A', 'bm1', 120), 
            ('A', 'bm2', 80), 
            ('A', 'bm3', 80), 
            ('B', 'bm4', 200), 
            ('B', 'bm5', 50)
     AS t(opstina, bm, glasali)
ORDER BY glasali DESC;