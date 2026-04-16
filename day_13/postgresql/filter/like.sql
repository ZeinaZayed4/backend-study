-- ~~ 		LIKE
-- ~~* 		ILIKE
-- !~~  	NOT LIKE
-- !~~* 	NOT ILIKE

SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name LIKE 'Jen%';


SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name LIKE '%er%'
ORDER BY
	first_name;


SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name LIKE '_her%'
ORDER BY
	first_name;


SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name NOT LIKE 'Jen%'
ORDER BY
	first_name;


SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name ILIKE 'BAR%';


SELECT
	first_name,
	last_name
FROM
	customer
WHERE
	first_name ~~ 'Dar%';


CREATE TABLE t(
	message TEXT
);


INSERT INTO t(message)
VALUES('The rents are now 10% higher than last month'),
      ('The new film will have _ in the title');

SELECT * FROM t
WHERE message LIKE '%10$%%' ESCAPE '$';

