-- INSERT returns a command tag:
	-- INSERT oid count
	-- oid is an object identifier, the INSERT statement returns oid with value 0.
	-- The count is the no. rows inserted successfully.
-- RETURNING clause returns the information of the inserted row. 


CREATE TABLE links (
	id SERIAL PRIMARY KEY,
	url VARCHAR(255) NOT NULL,
	name VARCHAR(255) NOT NULL,
	description VARCHAR(255),
	last_update DATE
);


INSERT INTO links (url, name)
VALUES('https://google.com', 'Google');


SELECT * FROM links;


INSERT INTO links (url, name)
VALUES('https://oreilly.com', 'O''Reilly Media');


INSERT INTO links (url, name, last_update)
VALUES('https://neon.com/postgresql', 'PostgreSQL Tutorial', '2026-04-15');


INSERT INTO links (url, name)
VALUES('https://postgresql.org', 'PostgreSQL')
RETURNING id;
