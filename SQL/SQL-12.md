https://app.patika.dev/egitimler/veri-bilimi-patikasi/sql/Odev12

Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.

1.film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?

2.film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?

3.film tablosunda en düşük rental_rate ve en düşük replacement_cost değerlerine sahip filmleri sıralayınız.

4.payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.

1.
SELECT COUNT(*)
FROM film
WHERE length>(
	SELECT AVG(length)
	FROM film
)
;

2.

SELECT COUNT(*)
FROM film
WHERE rental_rate=(
	SELECT MAX(rental_rate)
	FROM film
)
;

3.
SELECT *
FROM film
WHERE rental_rate=(
	SELECT MIN(rental_rate)
	FROM film
) AND replacement_cost=(
	SELECT MIN(replacement_cost)
	FROM film
)
;

4.
SELECT *
FROM customer
INNER JOIN payment ON payment.customer_id=customer.customer_id
WHERE customer.customer_id= ANY (SELECT customer_id
FROM payment
GROUP BY customer_id

HAVING COUNT(\*)=(SELECT count(\*)
FROM payment
GROUP BY customer_id
ORDER BY COUNT(\*) DESC
LIMIT 1
)
);
