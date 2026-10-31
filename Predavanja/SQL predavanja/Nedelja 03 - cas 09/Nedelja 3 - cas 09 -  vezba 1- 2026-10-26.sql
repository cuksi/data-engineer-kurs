-- 1 zadatak: Колико бирачких места има у свакој општини? Која општина има највише?
SELECT 
    opstina,
    COUNT(bm_uid) as bm_po_opstini
FROM parlamentarni_izbori_2026
GROUP BY opstina
ORDER BY bm_po_opstini DESC;
-- Resenje: Град Нови Сад = 221; Град Лесковац = 186; Град Крагујевац = 174

-- 2 zadatak: Колика је укупна излазност у целој табели? Рачунајте из сабраних бројева, не као просек излазности места.
SELECT
    SUM(glasali_biraci) AS ukupno_glasalo,
    SUM(upisani_biraci) AS ub,
    ROUND (ukupno_glasalo / ub * 100.0, 2) AS ukupna_izlaznost
FROM parlamentarni_izbori_2026;
-- Resenje 68,85

-- 3 zadatak: Колико је гласова добила свака листа и колики је то удео у свим важећим гласовима? Прикажите првих пет листа. NIJE RESEN
SELECT
    lista,
    SUM(glasovi) AS glasova_po_listi,
    ROUND(glasova_po_listi / (SELECT SUM(glasovi) FROM glasovi) * 100.0, 2) AS udeo
FROM glasovi
GROUP BY lista
ORDER BY glasova_po_listi DESC LIMIT 5;
-- Resenje:
-- lista	    glasova_po_listi	udeo
-- lista_3	    2266939	            53.42
-- lista_1	    1683090	            39.66
-- lista_2	    93104	            2.19
-- lista_8	    38502	            0.91
-- lista_5	    34761	            0.82

-- 4 zadatak: Колико бирачких места има мање од 100 уписаних бирача?
SELECT
    COUNT(bm_naziv)
FROM parlamentarni_izbori_2026
WHERE upisani_biraci < 100;
-- Resenje 739

-- 5 zadatak: Која општина има највећи, а која најмањи удео неважећих листића? Рачунајте само општине са бар 1.000 листића.
SELECT
    opstina,
    ROUND ((SUM(nevazeci_listici) / SUM(listici_u_kutiji) )* 100.0, 2 )AS udeo,
    SUM(listici_u_kutiji) AS ubaceni_listici_po_opstini
FROM parlamentarni_izbori_2026
GROUP BY opstina
HAVING ubaceni_listici_po_opstini >= 1000
ORDER BY udeo DESC;
-- Штрпце= 6.43%

SELECT
    opstina,
    ROUND ((SUM(nevazeci_listici) / SUM(listici_u_kutiji) )* 100.0, 2 )AS udeo,
    SUM(listici_u_kutiji) AS ubaceni_listici_po_opstini
FROM parlamentarni_izbori_2026
GROUP BY opstina
HAVING ubaceni_listici_po_opstini >= 1000
ORDER BY udeo ASC;
-- Иностранство = 0.21%