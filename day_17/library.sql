CREATE DATABASE library;

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	country VARCHAR(50)
);

CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	title VARCHAR(200) NOT NULL,
	author_id INT REFERENCES authors(id),
	published_year INT,
	genre VARCHAR(50)
);


CREATE TABLE members (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE,
	joined_date DATE DEFAULT CURRENT_DATE
);


CREATE TABLE borrowings (
	id SERIAL PRIMARY KEY,
	book_id INT REFERENCES books(id),
	member_id INT REFERENCES members(id),
	borrowed_date DATE DEFAULT CURRENT_DATE,
	returned_date DATE
);


INSERT INTO authors (name, country)
VALUES 
	('J.K Rowling', 'UK'),
	('George Orwell', 'UK'),
	('Haruki Murakmi', 'Japan');

INSERT INTO books (title, author_id, published_year, genre)
VALUES 
	('Harry Potter', 1, 1997, 'Fantasy'),
	('1984', 2, 1949, 'Dystopian'),
	('Animal Farm', 2, 1945, 'Political Fiction'),
	('Norwegian Wood', 3, 1987, 'Romance');

INSERT INTO members (name, email)
VALUES 
	('Zeina Zayed', 'zeina@email.com'),
	('Hana Atef', 'hana@email.com');

INSERT INTO borrowings (book_id, member_id, borrowed_date)
VALUES 
	(1, 1, '2026-04-01'),
	(2, 1, '2026-04-04'),
	(3, 2, '2026-04-20');


