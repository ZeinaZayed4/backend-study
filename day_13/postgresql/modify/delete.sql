CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT false
);

INSERT INTO todos (title, completed) VALUES
    ('Learn basic SQL syntax', true),
    ('Practice writing SELECT queries', false),
    ('Study PostgreSQL data types', true),
    ('Create and modify tables', false),
    ('Explore advanced SQL concepts', true),
    ('Understand indexes and optimization', false),
    ('Backup and restore databases', true),
    ('Implement transactions', false),
    ('Master PostgreSQL security features', true),
    ('Build a sample application with PostgreSQL', false);

DELETE FROM todos
WHERE id = 1;

DELETE FROM todos
WHERE id = 100;

DELETE FROM todos
WHERE id = 2
RETURNING *;

DELETE FROM todos
WHERE completed = true
RETURNING *;

DELETE FROM todos;

SELECT * FROM todos;

