CREATE TABLE teams (
	id INT PRIMARY KEY,
	team VARCHAR(100) NOT NULL,
	city VARCHAR(100) NOT NULL
);


CREATE TABLE players (
	id INT PRIMARY KEY,
	team_id INT REFERENCES teams(id),
	player VARCHAR(100) NOT NULL,
	role VARCHAR(100) NOT NULL
);


INSERT INTO teams (id, team, city)
VALUES
    (1, 'Lions', 'Rome'),
    (2, 'Owls', 'Oslo'),
    (3, 'Bears', 'Bern'),
    (4, 'Sharks', 'Lima');


INSERT INTO players (id, team_id, player, role)
VALUES
    (1, 1, 'Ava', 'Guard'),
    (2, 1, 'Noah', 'Wing'),
    (3, 2, 'Emma', 'Back'),
    (4, NULL, 'Liam', 'Guard'),
    (5, NULL, 'Mia', 'Wing');


