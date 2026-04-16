CREATE TABLE courses(
	course_id serial PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
  	price DECIMAL(10,2) NOT NULL,
  	description VARCHAR(500),
  	published_date date
);


INSERT INTO courses( course_name, price, description, published_date)
VALUES
	('PostgreSQL for Developers', 299.99, 'A complete PostgreSQL for Developers', '2020-07-13'),
	('PostgreSQL Administration', 349.99, 'A PostgreSQL Guide for DBA', NULL),
	('PostgreSQL High Performance', 549.99, NULL, NULL),
	('PostgreSQL Bootcamp', 777.99, 'Learn PostgreSQL via Bootcamp', '2013-07-11'),
	('Mastering PostgreSQL', 999.98, 'Mastering PostgreSQL in 21 Days', '2012-06-30');


UPDATE courses
SET published_date = '2020-08-01'
WHERE course_id = 3;


UPDATE courses
SET published_date = '2020-07-01'
WHERE course_id = 2
RETURNING *;


UPDATE courses
SET price = price * 1.05;


SELECT * FROM courses;
