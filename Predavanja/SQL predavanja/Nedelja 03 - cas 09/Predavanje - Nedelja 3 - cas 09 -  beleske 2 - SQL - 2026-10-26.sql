SELECT * FROM parlamentarni_izbori_2026;

CREATE OR REPLACE VIEW glasovi AS       -- Ovo ne ucimo ovo je da napravimo pogleda tabele koji cemo kasnije da koristimo
-- Листе 19–30 нису биле на листићу: у CSV-у постоје само као колоне са нулама.
SELECT bm_uid, opstina, okrug_region, upisani_biraci, vreme_unosa_rezultata, lista, glasovi
FROM (
  SELECT bm_uid, opstina, okrug_region, upisani_biraci, vreme_unosa_rezultata,
         stack(18,
           'lista_1',  CAST(lista_1  AS INT), 'lista_2',  CAST(lista_2  AS INT), 'lista_3',  CAST(lista_3  AS INT),
           'lista_4',  CAST(lista_4  AS INT), 'lista_5',  CAST(lista_5  AS INT), 'lista_6',  CAST(lista_6  AS INT),
           'lista_7',  CAST(lista_7  AS INT), 'lista_8',  CAST(lista_8  AS INT), 'lista_9',  CAST(lista_9  AS INT),
           'lista_10', CAST(lista_10 AS INT), 'lista_11', CAST(lista_11 AS INT), 'lista_12', CAST(lista_12 AS INT),
           'lista_13', CAST(lista_13 AS INT), 'lista_14', CAST(lista_14 AS INT), 'lista_15', CAST(lista_15 AS INT),
           'lista_16', CAST(lista_16 AS INT), 'lista_17', CAST(lista_17 AS INT), 'lista_18', CAST(lista_18 AS INT)
         ) AS (lista, glasovi)
  FROM parlamentarni_izbori_2026
);

SELECT * FROM glasovi;