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
SELECT customer.customer_id,customer.first_name,customer.last_name,COUNT(*)
FROM payment
INNER JOIN customer ON customer.customer_id=payment.customer_id
GROUP BY customer.customer_id,customer.first_name,customer.last_name
HAVING CUSTOMER.CUSTOMER_ID = ANY
		(SELECT CUSTOMER_ID
			FROM PAYMENT
			GROUP BY CUSTOMER_ID
			HAVING COUNT(*) = ANY
				(SELECT COUNT(*)
					FROM PAYMENT
					GROUP BY CUSTOMER_ID
					ORDER BY COUNT(*) DESC
					LIMIT 1))
;

