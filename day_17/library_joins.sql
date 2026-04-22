-- INNER JOIN: books with their authors
SELECT
	b.title,
	a.name
FROM books b
INNER JOIN authors a
ON b.author_id = a.id;


-- LEFT JOIN: all books
SELECT
	b.title,
	a.name
FROM books b
LEFT JOIN authors a
ON b.author_id = a.id;


-- Multiple JOINs: show who borrowed which books
SELECT
	m.name AS member,
	bk.title AS book,
	a.name AS author,
	b.borrowed_date
FROM borrowings b
INNER JOIN members m ON b.member_id = m.id
INNER JOIN books bk ON b.book_id = bk.id
INNER JOIN authors a ON bk.author_id = a.id;


-- LEFT JOIN: members who haven't borrowed anything
SELECT
	m.name,
	b.id
FROM members m
LEFT JOIN borrowings b
ON m.id = b.member_id
WHERE b.id IS NULL;


-- Count books per author
SELECT
	a.name,
	COUNT(b.id) AS book_count
FROM books b
LEFT JOIN authors a
ON b.author_id = a.id
GROUP BY a.name;

