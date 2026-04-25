-- Aggregate functions perform a calculation on a set of rows
-- and return a single row.

-- We often use aggregate functions with the GROUP BY clause.


-- calculate the average replacement cost of all films
SELECT ROUND(AVG(replacement_cost), 2) avg_replacement_cost
FROM film;

-- calculate the average replacement cost of the Drama films whose category id is 7
SELECT
	ROUND(AVG(replacement_cost), 2) avg_replacement_cost
FROM film
INNER JOIN film_category USING(film_id)
INNER JOIN category USING(category_id)
WHERE category_id = 7;


-- get number of films
SELECT COUNT(*)
FROM film;

-- get number of drama films
SELECT COUNT(*)
FROM film
INNER JOIN film_category USING(film_id)
INNER JOIN category USING(category_id)
WHERE category_id = 7;


-- get the max replacement cost of films
SELECT MAX(replacement_cost)
FROM film;

-- get the films with the max replacement cost
SELECT film_id, title
FROM film
WHERE
	replacement_cost = (
		SELECT MAX(replacement_cost)
		FROM film
	)
ORDER BY title;


-- get the min replacement cost of films
SELECT MIN(replacement_cost)
FROM film;

-- get the films with the min replacement cost
SELECT film_id, title
FROM film
WHERE replacement_cost = (
		SELECT MIN(replacement_cost)
		FROM film
	)
ORDER BY title;


-- calculate the total length of films grouped by film's rating
SELECT 
	rating,
	SUM(rental_duration)
FROM film
GROUP BY rating
ORDER BY rating;


-- ARRAY_AGG() accepts a set of values and returns an array.

-- get the list of film titles and a list of actors for each film
SELECT
	title,
	ARRAY_AGG(first_name || ' ' || last_name) actors
FROM film
INNER JOIN film_actor USING(film_id)
INNER JOIN actor USING(actor_id)
GROUP BY title
ORDER BY title;

-- get the list of film titles and a list of actors for each film sorted by the actor's first name
SELECT
	title,
	ARRAY_AGG(
		first_name || ' ' || last_name
		ORDER BY first_name
	) actors
FROM film
INNER JOIN film_actor USING(film_id)
INNER JOIN actor USING(actor_id)
GROUP BY title
ORDER BY title;


-- BOOL_AND() returns true if all values in the group are true, or false otherwise.

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

CREATE TABLE projects(
    project_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    active BOOL,
    team_id INT NOT NULL REFERENCES teams(team_id)
);

INSERT INTO teams (team_name)
VALUES
	('Team A'),
	('Team B'),
	('Team C')
RETURNING *;

INSERT INTO projects(name, active, team_id)
VALUES
	('Intranet', false, 1),
	('AI Chatbot', true, 1),
	('Robot', true, 2),
	('RPA', true, 2),
	('Data Analytics', true, 3),
	('BI', NULL, 3)
RETURNING *;

-- test if all projects are active in the projects table
SELECT BOOL_AND(active)
FROM projects;

-- check if there are active projects in each team
SELECT
	team_name,
	BOOL_AND(active) active_projects
FROM projects
INNER JOIN teams USING(team_id)
GROUP BY team_name;

-- get teams with active projects
SELECT
	team_name,
	BOOL_AND(active) active_projects
FROM projects
INNER JOIN teams USING(team_id)
GROUP BY team_name
HAVING BOOL_AND(active) = true;


-- BOOL_OR()

CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    active bool,
    team_id INT REFERENCES teams(team_id)
);

INSERT INTO members (member_name, team_id, active)
VALUES
	('Alice', 1, true),
	('Bob', 2, true),
	('Charlie', 1, null),
	('David', 2, false),
	('Peter', 3, false),
	('Joe', 3, null)
RETURNING *;

-- test if there are any active members in members table
SELECT BOOL_OR(active) active_member_exists
FROM members;

-- check if there are any active members in each team
SELECT 
	team_name,
	BOOL_OR(active) active_member_exists
FROM members
INNER JOIN teams USING(team_id)
GROUP BY team_name;

-- get teams that have active members
SELECT 
	team_name,
	BOOL_OR(active) active_member_exists
FROM members
INNER JOIN teams USING(team_id)
GROUP BY team_name
HAVING BOOL_OR(active) = true;


-- STRING_AGG()

-- return a list of actor’s names for each film from the film table
SELECT
	f.title,
	STRING_AGG(
		a.first_name || ' ' || a.last_name,
		','
		ORDER BY
			a.first_name,
			a.last_name
	) actors
FROM film f
INNER JOIN film_actor fa USING(film_id)
INNER JOIN actor a USING(actor_id)
GROUP BY f.title;

-- build an email list for each country, with emails separated by semicolons
SELECT
	country,
	STRING_AGG(email, ';') email_list
FROM customer
INNER JOIN address USING(address_id)
INNER JOIN city USING(city_id)
INNER JOIN country USING(country_id)
GROUP BY country
ORDER BY country;
