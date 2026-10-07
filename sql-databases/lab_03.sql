--Lab3
--Ex1
SELECT * FROM customers;
INSERT INTO customers VALUES (11, 'Daniel', 'Nilsson', 'dan@nil.se', 'Göteborg','2026-10-07');

--Ex2
SELECT * FROM products;
INSERT INTO products(name, category, price, stock) VALUES
('Scarf', 'Accessories', 229, 15),
('Gloves', 'Accessories', 199, 20);

--Ex3
SELECT * FROM orders;
SELECT * FROM products;
INSERT INTO orders(order_id, customer_id, order_date, status) VALUES
(16, 7, '2026-10-07', 'new');
INSERT INTO order_items(order_id, product_id, quantity, unit_price) VALUES 
(16, 10, 2, 179);
SELECT * FROM orders;
SELECT * FROM order_items;

--Ex4
INSERT INTO order_items VALUES (16, 10, 0, 179);
--CHECK constraint failed: quantity > 0

--Ex5
SELECT * FROM orders;
UPDATE orders SET status = 'shipped' WHERE order_id = 12;

--Ex6 --woha bohle
SELECT * FROM products;
UPDATE products SET stock = 50 WHERE product_id = 5;

--Ex7
UPDATE products SET price = price * 1.10 WHERE category = 'Accessories';

--Ex8
SELECT * FROM orders;
SELECT * FROM order_items;
SELECT order_id FROM orders WHERE status = 'cancelled';
DELETE FROM order_items WHERE order_id IN (SELECT order_id FROM orders WHERE status = 'cancelled');
DELETE FROM orders WHERE status = 'cancelled';

--Ex9
SELECT * FROM orders;

--Ex10
--both phone_numbers as one column and course1-3 as multiple columns are problems
--they both violate the 1NF rule: repeating groups are not permitted
--phone_numbers for having multiple values in one column and course for having multiple columns
--these should both be saved in their separate tables with the student as key

--Ex11
--it violates 1NF repeating groups by using column products as a list of products ordered spaced by commas
--it should be in its own table order_items(order_id, product_id, quantity, unit_price) with order_id as KEY

--Ex12
--customer_email should be stored with all the customer data in customers table. so that it is stored in one unique entry
--storing it in this incorrect way results in multiple 2NF violations including deletition-, update- and insertion anomaly

--Ex13-Ex15
--see music_diagram.png

--Ex16
CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE teachers (
	teacher_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE lessons (
	lesson_id INTEGER PRIMARY KEY,
	teacher_id INTEGER,
	room TEXT NOT NULL,
	lesson_date TEXT NOT NULL,
	lesson_time TEXT NOT NULL,
	instrument TEXT,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE student_lesson (
	student_id INTEGER,
	lesson_id INTEGER,
	FOREIGN KEY (student_id) REFERENCES students(student_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
	UNIQUE (student_id, lesson_id)
);

CREATE TABLE teacher_instrument (
	teacher_id INTEGER,
	instrument TEXT,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	UNIQUE (teacher_id, instrument)
);
	
