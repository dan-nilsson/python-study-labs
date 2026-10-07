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