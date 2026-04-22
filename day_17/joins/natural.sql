CREATE TABLE categories (
  	category_id SERIAL PRIMARY KEY,
  	category_name VARCHAR (255) NOT NULL
);

CREATE TABLE products (
  	product_id serial PRIMARY KEY,
 	product_name VARCHAR (255) NOT NULL,
  	category_id INT NOT NULL,
 	FOREIGN KEY (category_id) REFERENCES categories (category_id)
);

INSERT INTO categories (category_name)
VALUES
  	('Smartphone'),
  	('Laptop'),
  	('Tablet'),
  	('VR')
RETURNING *;

INSERT INTO products (product_name, category_id)
VALUES
  	('iPhone', 1),
  	('Samsung Galaxy', 1),
  	('HP Elite', 2),
  	('Lenovo Thinkpad', 2),
  	('iPad', 3),
  	('Kindle Fire', 3)
RETURNING *;

SELECT * 
FROM products
NATURAL JOIN categories;

-- same as the above
SELECT * 
FROM products
INNER JOIN categories USING(category_id);


SELECT * 
FROM categories
NATURAL LEFT JOIN products;

-- returns an empty list as the both tables have another common column called "last_update"
-- 	beside the country_id
SELECT * 
FROM city
NATURAL JOIN country;
