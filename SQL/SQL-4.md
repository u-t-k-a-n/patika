https://app.patika.dev/egitimler/veri-bilimi-patikasi/sql/Odev4

Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.

1.film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.

2.film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?

3.film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?

4.country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?

5.city tablosundaki şehir isimlerinin kaçtanesi 'R' veya r karakteri ile biter?

1.
SELECT 
DISTINCT replacement_cost
FROM film;

2.
--21

SELECT 
COUNT(DISTINCT replacement_cost)
FROM film;

3.
--9

SELECT 
COUNT(*)
FROM filmP
WHERE title LIKE 'T%' AND rating='G';

4.
--13

SELECT 
COUNT(*)
FROM country
WHERE LENGTH(country)=5;

5.
--33

SELECT COUNT(*)
FROM city
WHERE city ILIKE '%r';


