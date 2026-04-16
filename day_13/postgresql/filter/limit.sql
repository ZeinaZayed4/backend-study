-- LIMIT: constrains the no. of rows returned.
-- OFFSET: skip number of rows before returning.

-- if row_count = 0, query returns an empty set
-- if row_count = NULL, query returns the same result as it doesn't have the LIMIT clause.

-- To use LIMIT, you should always use ORDER BY.


-- get the first 5 films sorted by film_id
SELECT
	film_id,
	title,
	release_year
FROM
	film
ORDER BY
	film_id
LIMIT 5;


-- get 4 films starting from 4th one ordered by film_id
SELECT
	film_id,
	title,
	release_year
FROM
	film
ORDER BY
	film_id
LIMIT 4 OFFSET 3;


-- get the top 10 most expensive films by rental_rate
SELECT
	film_id,
	title,
	rental_rate 
FROM
	film
ORDER BY
	rental_rate DESC
LIMIT 10;

