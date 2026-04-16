SELECT
	film_id,
	title
FROM
	film
WHERE 
	film_id IN (1, 2, 3);


SELECT
	first_name,
	last_name
FROM
	actor
WHERE
	last_name IN ('Allen', 'Chase', 'Davis')
ORDER BY
	last_name;


SELECT
	payment_id,
	amount,
	payment_date
FROM
	payment
WHERE
	payment_date::date IN ('2007-02-15', '2007-02-16');


SELECT
	film_id,
	title
FROM
	film
WHERE 
	film_id NOT IN (1, 2, 3)
ORDER BY
	film_id;


