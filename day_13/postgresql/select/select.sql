SELECT 
	first_name || ' ' || last_name "full name",
	email
FROM customer;


SELECT NOW();


SELECT
	first_name,
	last_name
FROM 
	customer
ORDER BY
	first_name ASC,
	last_name DESC;


SELECT
	first_name,
	LENGTH(first_name) len
FROM
	customer
ORDER BY
	len DESC;


CREATE TABLE sort_demo(num INT);


INSERT INTO sort_demo 
VALUES
	(1),
	(2),
	(3),
	(null);


SELECT
	num
FROM
	sort_demo
ORDER BY 
	num DESC NULLS LAST;


CREATE TABLE colors(
	id SERIAL PRIMARY KEY,
	bcolor VARCHAR,
	fcolor VARCHAR
);


INSERT INTO
  colors (bcolor, fcolor)
VALUES
  ('red', 'red'),
  ('red', 'red'),
  ('red', NULL),
  (NULL, 'red'),
  (NULL, NULL),
  ('green', 'green'),
  ('blue', 'blue'),
  ('blue', 'blue');


SELECT
	DISTINCT bcolor, fcolor
FROM 
	colors
ORDER BY
	bcolor,
	fcolor;


SELECT
	DISTINCT rental_rate
FROM
	film
ORDER BY
	rental_rate;


CREATE TABLE student_scores (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  subject VARCHAR(50) NOT NULL,
  score INTEGER NOT NULL
);


INSERT INTO student_scores (name, subject, score)
VALUES
  ('Alice', 'Math', 90),
  ('Bob', 'Math', 85),
  ('Alice', 'Physics', 92),
  ('Bob', 'Physics', 88),
  ('Charlie', 'Math', 95),
  ('Charlie', 'Physics', 90);


SELECT
	DISTINCT ON (name) name,
	subject,
	score
FROM
	student_scores
ORDER BY
	name,
	score DESC;
