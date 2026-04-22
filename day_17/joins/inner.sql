SELECT 
	t.id AS team_id,
	team,
	city,
	p.id AS player_id,
	player,
	role
FROM teams t
INNER JOIN players p
ON t.id = p.team_id;


SELECT
	customer_id,
	first_name,
	last_name,
	amount,
	payment_date
FROM customer
INNER JOIN payment USING(customer_id)
ORDER BY payment_date;


-- Three tables
SELECT
	c.customer_id,
	c.first_name || ' ' || c.last_name customer_name,
	s.first_name || ' ' || s.last_name staff_name,
	p.amount,
	p.payment_date
FROM customer c 
INNER JOIN payment p USING(customer_id)
INNER JOIN staff s USING(staff_id)
ORDER BY payment_date;

