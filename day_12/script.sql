CREATE DATABASE giraffe;

CREATE TABLE students(
    id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);

DESCRIBE students;

DROP TABLE students;

ALTER TABLE students
ADD gpa DECIMAL(3, 2);

ALTER TABLE students
DROP COLUMN gpa;
