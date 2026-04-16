-- OFFSET row_to_skip { ROW | ROWS }
-- FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY


-- get the first film sorted by titles ascending
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title
FETCH FIRST ROW ONLY;
	

-- get the first 5 films sorted by titles
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title
FETCH FIRST 5 ROW ONLY;


-- get the next 5 films after the first 5 films sorted by titles
SELECT
	film_id,
	title
FROM
	film
ORDER BY
	title
OFFSET 5 ROWS
FETCH FIRST 5 ROW ONLY;

