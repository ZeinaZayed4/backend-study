SELECT
	t.id AS team_id,
	team,
	city,
	p.id AS player_id,
	player,
	role
FROM teams t
FULL OUTER JOIN players p
ON t.id = p.team_id;


CREATE TABLE departments (
	dept_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(255) NOT NULL
);

CREATE TABLE employees (
	emp_id SERIAL PRIMARY KEY,
	emp_name VARCHAR(255),
	dept_id INTEGER
);

INSERT INTO departments (dept_name)
VALUES
  ('Sales'),
  ('Marketing'),
  ('HR'),
  ('IT'),
  ('Production');
INSERT INTO employees (emp_name, dept_id)
VALUES
  ('Bette Nicholson', 1),
  ('Christian Gable', 1),
  ('Joe Swank', 2),
  ('Fred Costner', 3),
  ('Sandra Kilmer', 4),
  ('Julia Mcqueen', NULL);

SELECT
	emp_name,
	dept_name
FROM employees
FULL OUTER JOIN departments USING(dept_id);

SELECT
	emp_name,
	dept_name
FROM employees
FULL OUTER JOIN departments USING(dept_id)
WHERE emp_name IS NULL;

SELECT
	emp_name,
	dept_name
FROM employees
FULL OUTER JOIN departments USING(dept_id)
WHERE dept_name IS NULL;


