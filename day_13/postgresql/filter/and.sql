-- true -> true, 't', 'true', 'y', 'yes', '1'
-- false -> false, 'f', 'false', 'n', 'no', '0'

SELECT true AND true AS result;		-- true

SELECT false AND true AS result;	-- false

SELECT true AND null AS result;		-- null

SELECT false AND null AS result;	-- false

SELECT null AND null AS result;		-- null

SELECT
	title,
	length,
	rental_rate
FROM
	film
WHERE
	length > 180
	AND rental_rate < 1;
