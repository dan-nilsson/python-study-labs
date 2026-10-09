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


