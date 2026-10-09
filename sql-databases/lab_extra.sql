--Lab Extra
--Level1
--Ex1
SELECT * FROM products WHERE category IN ('Clothing','Accessories') AND price >= 150 AND price <= 500 ORDER BY price DESC;

--Ex2
SELECT * FROM orders WHERE order_date LIKE '2026-02%' AND status NOT IN ('cancelled');

--Ex3
SELECT oi.order_id, p.name, oi.quantity, (oi.unit_price * oi.quantity) AS line_total
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE line_total > 500
ORDER BY line_total DESC;

--Ex4
SELECT c. customer_id, c.first_name, c.last_name, COUNT(o.order_id) AS antal_order
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city IN ('Stockholm','Uppsala')
GROUP BY c.customer_id;

--Ex5
INSERT INTO customers (first_name, last_name, email, city, joined_date)
VALUES ('Leo','Falk', 'leo@falk.se', 'Uppsala', '2026-10-09');
SELECT * FROM customers;
INSERT INTO orders (customer_id, order_date, status) VALUES (
(SELECT customer_id FROM customers WHERE email = 'leo@falk.se'),
'2026-10-09',
'new');
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (
(SELECT order_id FROM orders WHERE customer_id = (SELECT customer_id FROM customers 
	WHERE email = 'leo@falk.se') AND order_date = '2026-10-09'),
(SELECT product_id FROM products WHERE name IN ('Hoodie Black')),
1,
(SELECT price FROM products WHERE name IN ('Hoodie Black')));
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (
(SELECT order_id FROM orders WHERE customer_id = 
	(SELECT customer_id FROM customers WHERE email = 'leo@falk.se') 
	AND	order_date = '2026-10-09'),
(SELECT product_id FROM products WHERE name IN ('Socks 3-pack')),
2,
(SELECT price FROM products WHERE name IN ('Socks 3-pack')));
SELECT oi.order_id, p.name, oi.quantity, (oi.quantity * oi.unit_price) AS line_total
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 16;

--Ex6
SELECT oi.order_id, oi.product_id, oi.quantity
FROM order_items oi
WHERE order_id = 12;
UPDATE orders SET status = 'cancelled' WHERE order_id = 12;
UPDATE products SET stock = stock + 1 WHERE product_id IN (4,9);
SELECT * FROM orders WHERE order_id = 12;
SELECT * FROM products WHERE product_id IN (4,9);
DELETE FROM order_items WHERE order_id = 12;
SELECT * FROM order_items;


--Ex7
DELETE FROM products WHERE product_id = 1;
--FOREIGN KEY constraint failed. used in order_items key pair.
UPDATE products SET stock = 0 WHERE product_id = 1;
--we could set stock to 0.

--Ex8
ALTER TABLE products ADD COLUMN discount_percent REAL DEFAULT 0;
ALTER TABLE products ADD CONSTRAINT discount_percent CHECK (discount_percent >= 0 AND discount_percent <= 90);
UPDATE products SET discount_percent = 20 WHERE category IN ('Shoes');
SELECT name AS product, price, (price - (price * (discount_percent / 100))) AS price_after_discount
FROM products;
--sneaky REAL

--Ex9
SELECT p.name AS product, o.order_date
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
RIGHT JOIN products p ON oi.product_id = p.product_id;

--Ex10
SELECT c.first_name, c.last_name, COUNT(o.order_id) AS dojjor
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE oi.product_id IN (SELECT product_id FROM products WHERE category IN ('Shoes'))
GROUP BY c.customer_id;

--Ex11
SELECT DISTINCT (c1.first_name || ' ' || c1.last_name) AS customer1, (c2.first_name || ' ' || c2.last_name) AS customer2
FROM customers c1
JOIN customers c2 ON c1.city = c2.city
WHERE c1.customer_id < c2.customer_id;

--Ex12
UPDATE products SET price = 649 WHERE name = 'Hoodie Black';
SELECT oi.order_id, p.name, oi.unit_price AS paid, p.price AS todays_price
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE p.name IN ('Hoodie Black') AND oi.unit_price != p.price;

--Ex13
--Tables
CREATE TABLE salons (
	salon_num INTEGER PRIMARY KEY,
	num_seats INTEGER NOT NULL,
	screen_size INTEGER NOT NULL,
	sound_system TEXT
);
CREATE TABLE movies (
	title TEXT PRIMARY KEY,
	duration INTEGER NOT NULL,
	age_limit INTEGER,
	CHECK (age_limit IN (0,7,11,15))
);
CREATE TABLE screenings (
	screen_id INTEGER PRIMARY KEY,
	movie TEXT,
	salon INTEGER,
	show_date TEXT NOT NULL,
	show_time TEXT NOT NULL,
	FOREIGN KEY (movie) REFERENCES movies (title),
	FOREIGN KEY (salon) REFERENCES salons (salon_num)
);
CREATE TABLE tickets (
	ticket_id INTEGER PRIMARY KEY,
	screen_id INTEGER,
	seat_num INTEGER,
	price REAL NOT NULL,
	FOREIGN KEY (screen_id) REFERENCES screenings (screen_id),
	UNIQUE (screen_id, seat_num)
);
CREATE TABLE customers (
	customer_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);
CREATE TABLE customer_ticket (
	customer_id INTEGER,
	ticket_id INTEGER,
	PRIMARY KEY (customer_id, ticket_id),
	FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
	FOREIGN KEY (ticket_id) REFERENCES tickets (ticket_id)
);
--Insertions
INSERT INTO movies (title, duration, age_limit) VALUES
('Heat', 170, 15),
('Leon : The Professional', 110, 15),
('Shrek 2', 100, 7);
INSERT INTO salons (salon_num, num_seats, screen_size, sound_system) VALUES
(1, 100, 600, 'THX Ultra Delux Mega'),
(2, 150, 720, 'Omega THX DTS 200.1');
INSERT INTO screenings (movie, salon, show_date, show_time) VALUES
('Heat', 1, '2026-10-09', '21:00'),
('Heat', 2, '2026-10-09', '21:00'),
('Leon : The Professional', 1, '2026-10-09', '19:00'),
('Shrek 2', 2, '2026-10-09', '19:00');
INSERT INTO customers (name) VALUES
('Bob'), ('Erica'), ('James'), ('Hank'), ('Sandra'), ('Gina');
INSERT INTO tickets (screen_id, seat_num, price) VALUES
(1, 24, 120), (1, 25, 120),
(3, 64, 120), (3, 65, 120),
(4, 78, 100), (4, 77, 100);
INSERT INTO customer_ticket (customer_id, ticket_id) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6);
--Queries
SELECT * FROM screenings
ORDER BY show_date, show_time;

SELECT t.ticket_id, c.name, s.movie, s.show_date
FROM customer_ticket ct
JOIN customers c ON ct.customer_id = c.customer_id
JOIN tickets t ON ct.ticket_id = t.ticket_id
JOIN screenings s ON t.screen_id = s.screen_id;

SELECT s.screen_id, s.movie, s.salon, s.show_date, s.show_time
FROM screenings s
LEFT JOIN tickets t ON s.screen_id = t.screen_id
WHERE t.screen_id IS NULL;