--Lab4 Joining Tables
--Ex1
SELECT * FROM orders;
SELECT c.first_name, c.last_name, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

--Ex2
SELECT c.first_name, o.order_id
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Erik';

--Ex3
SELECT c.city, o.order_id, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;

--Ex4
SELECT p.name, p.category
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

--Ex5
SELECT oi.order_id, p.name
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.product_id IN (SELECT product_id FROM products WHERE category = 'Shoes');

--Ex6
SELECT p.name, oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS line_total
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 10;

--Ex7
SELECT c.first_name, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_id IN (SELECT order_id FROM order_items WHERE product_id IN (SELECT product_id FROM products WHERE name = 'Hoodie Black'));
--spent 15min trying to look up 'Black Hoodie' smileyface

--Ex8
SELECT c.first_name, c.last_name, o.order_id
FROM orders o
RIGHT JOIN customers c ON o.customer_id = c.customer_id;

--Ex9
SELECT p.name, oi.order_id
FROM order_items oi
RIGHT JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id IS NULL;

--Ex10
SELECT c.first_name AS dude, p.name AS product, oi.quantity AS antal
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id
WHERE c.city = 'Uppsala';
