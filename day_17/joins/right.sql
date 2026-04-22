SELECT
	t.id AS team_id,
	team,
	city,
	p.id AS player_id,
	player,
	role
FROM teams t
RIGHT JOIN players p 
ON t.id = p.team_id;


SELECT
	f.film_id,
	f.title,
	i.inventory_id
FROM inventory i
RIGHT JOIN film f USING(film_id)
ORDER BY f.title;


SELECT
	f.film_id,
	f.title,
	i.inventory_id
FROM inventory i
RIGHT JOIN film f USING(film_id)
WHERE i.inventory_id IS NULL
ORDER BY f.title;

