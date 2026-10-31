SELECT * FROM glasovi;

SELECT * FROM parlamentarni_izbori_2026 WHERE upisani_biraci < 100 ORDER BY upisani_biraci;

SELECT * FROM parlamentarni_izbori_2026;

-- Udeo liste na svakom birackom mestu
SELECT 
    bm_uid, opstina, lista, glasovi,
    try_divide(100 * glasovi, SUM(glasovi) OVER (PARTITION BY bm_uid)) AS udeo_pct
FROM glasovi
WHERE bm_uid IS NOT NULL
ORDER BY bm_uid, glasovi DESC;


------------------------------------------ ovo ispod su pomocni query-jevi za ovo gore---------------------------------------
SELECT bm_uid, opstina, lista, glasovi FROM glasovi WHERE bm_uid IS NULL;

SELECT 
    bm_uid, lista,
    SUM(glasovi)
FROM glasovi
GROUP BY bm_uid, lista;

SELECT bm_uid, opstina, lista, glasovi 
FROM glasovi
WHERE bm_uid = 210849;
--------------------------------------- ovde je kraj pomocnog query-ia--------------------------------------------

-- Ko je prvi na svakom mestu
SELECT
    bm_uid, lista, glasovi,
    RANK() OVER(PARTITION BY bm_uid ORDER BY glasovi DESC) AS rnk
FROM glasovi
WHERE bm_uid IS NOT NULL
QUALIFY rnk = 1;

-- drugi nacin za ovaj gore zadatak
WITH rang AS (
    SELECT
    bm_uid, lista, glasovi,
    RANK() OVER(PARTITION BY bm_uid ORDER BY glasovi DESC) AS rnk
FROM glasovi
WHERE bm_uid IS NOT NULL
)
SELECT lista, bm_uid
FROM rang
WHERE rnk = 1;

-- Ko je prvi na koliko razlicitih mesta
WITH rang AS (
    SELECT
    bm_uid, lista, glasovi,
    RANK() OVER(PARTITION BY bm_uid ORDER BY glasovi DESC) AS rnk
FROM glasovi
WHERE bm_uid IS NOT NULL
)
SELECT lista, COUNT(*) AS prvo_mesto
FROM rang
WHERE rnk = 1
GROUP BY lista;
----------------------------kraj zadatka----------------------------------

-- Poredak tj. ovaj tekst zadatka ispod
-- Kolika je prednost prve lista nad drugom (prema rangiranju)
WITH poredak AS(
SELECT
    bm_uid, lista, glasovi,
    ROW_NUMBER() OVER(PARTITION BY bm_uid ORDER BY glasovi DESC) AS rn,     -- ROW_NUMBER zagrade su prazne ne upisujemo nista
    LEAD(glasovi, 2) OVER(PARTITION BY bm_uid ORDER BY glasovi DESC) AS naredna_lista_glasovi,     -- PROZORSKE FUNKCIJE ( OVER(PARTITION BY) ) GRUPISU NESTO ALI ZADRZAVAJU REDOVE, NE MENJA REDOVE SAMO CE DODATI KOLONU SA VREDNOSCU KOJU VRACA
    -- ovo u zagradi od LEAD ,2 je korak. Da uzima svaku drugu vrednost, mozemo koju god vrednost hocemo za korak
    SUM(glasovi)  OVER(PARTITION BY bm_uid) AS vazeci_glasovi
FROM glasovi
WHERE bm_uid IS NOT NULL
)
SELECT 
    bm_uid, lista, glasovi,
    glasovi - naredna_lista_glasovi AS razlika
    -- da treba procenat ovde bi se racunao
FROM poredak
WHERE rn = 1;   -- ovde je 1 zato sto dobijamo razliku koliko je u odnosu na sledeceg
----------------------------------kraj zadatka----------------------------------

-- Izlaznost: u odnosu na opstinu
SELECT
    bm_uid, opstina, upisani_biraci, glasali_biraci,
    ROUND(100 * try_divide(glasali_biraci, upisani_biraci), 2) AS izlaznost_pct,   -- ovo u zagradi try_divide je kao da je podeljeno samo ne izbacuje gresku kad deli NULL
    ROUND(100 * SUM(glasali_biraci) OVER(PARTITION BY opstina)
              / SUM(upisani_biraci) OVER(PARTITION BY opstina)
                , 2) AS izlaznost_opstina,  -- ovo je prvi nacin za izlaznost po opstinama i pravilnije je

    ROUND( 100 * 
            AVG(try_divide(glasali_biraci, upisani_biraci)) OVER(PARTITION BY opstina)
            , 2) AS prosek  -- ovo je drugi nacin za izlaznost po opstinama ali prvi nacin je pravilniji
FROM parlamentarni_izbori_2026;

-- dodat qualify
SELECT
    bm_uid, opstina, upisani_biraci, glasali_biraci,
    ROUND(100 * try_divide(glasali_biraci, upisani_biraci), 2) AS izlaznost_pct,   -- ovo u zagradi try_divide je kao da je podeljeno samo ne izbacuje gresku kad deli NULL
    ROUND(100 * SUM(glasali_biraci) OVER(PARTITION BY opstina)
              / SUM(upisani_biraci) OVER(PARTITION BY opstina)
                , 2) AS izlaznost_opstina,  -- ovo je prvi nacin za izlaznost po opstinama i pravilnije je

    ROUND( 100 * 
            AVG(try_divide(glasali_biraci, upisani_biraci)) OVER(PARTITION BY opstina)
            , 2) AS prosek  -- ovo je drugi nacin za izlaznost po opstinama ali prvi nacin je pravilniji
FROM parlamentarni_izbori_2026
QUALIFY izlaznost_pct IS NOT NULL AND izlaznost_opstina IS NOT NULL
ORDER BY izlaznost_pct - izlaznost_opstina DESC;