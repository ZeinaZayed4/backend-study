-- Upsert is a combination of update and insert.
-- it allows us to update an existing row or insert a new one if it doesn't exist.

CREATE TABLE inventory_upsert(
   	id INT PRIMARY KEY,
   	name VARCHAR(255) NOT NULL,
   	price DECIMAL(10,2) NOT NULL,
   	quantity INT NOT NULL
);

INSERT INTO inventory_upsert(id, name, price, quantity)
VALUES
	(1, 'A', 15.99, 100),
	(2, 'B', 25.49, 50),
	(3, 'C', 19.95, 75)
RETURNING *;


INSERT INTO inventory_upsert (id, name, price, quantity)
VALUES (1, 'A', 16.99, 120)
ON CONFLICT(id)
DO UPDATE SET
	price = EXCLUDED.price,
	quantity = EXCLUDED.quantity;


INSERT INTO inventory_upsert (id, name, price, quantity)
VALUES (4, 'D', 29.99, 20)
ON CONFLICT(id)
DO UPDATE SET
	price = EXCLUDED.price,
	quantity = EXCLUDED.quantity;


SELECT * FROM inventory_upsert ORDER BY id;
