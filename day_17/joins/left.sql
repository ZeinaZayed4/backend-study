SELECT
	t.id AS team_id,
	team,
	city,
	p.id AS player_id,
	player,
	role
FROM teams t 			-- left table
LEFT JOIN  players p	-- right table
ON t.id = p.team_id;


SELECT
	f.film_id,
	f.title,
	i.inventory_id
FROM film f
LEFT JOIN inventory i USING(film_id)
ORDER BY i.inventory_id;


SELECT
	f.film_id,
	f.title,
	i.inventory_id
FROM film f
LEFT JOIN inventory i USING(film_id)
WHERE i.film_id IS NULL
ORDER BY f.title;
