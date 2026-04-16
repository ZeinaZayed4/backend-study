-- Inserting multiple rows at once has advantages over inserting one row at a time:
	-- Performance: it's more efficient than multiple individual inserts because it reduces the number of round-trips between the application and the PostgreSQL server.
	-- Atomicity: the entire insert statement is atomic, meaning that either all rows are inserted or none are. This ensures data consistency.

CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(384) NOT NULL UNIQUE
);


INSERT INTO contacts (first_name, last_name, email)
VALUES
	('John', 'Doe', 'john.doe@example.com'),
	('Jane', 'Smith', 'jane.smith@example.com'),
	('Bob', 'Johnson', 'bob.jhonson@example.com');


SELECT * FROM contacts;


INSERT INTO contacts (first_name, last_name, email)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Charlie', 'Brown', 'charlie.brown@example.com')
RETURNING *;

