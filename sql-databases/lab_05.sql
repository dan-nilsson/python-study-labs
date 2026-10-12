--Lab5
--Ex09
SELECT p.name, SUM(oi.quantity) AS antal
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Anna'
GROUP BY p.name;

--Ex10
SELECT first_name, email FROM customers WHERE first_name = 'Erik';
UPDATE customers SET email = 'erik.johansson@example.com' WHERE first_name = 'Erik';

--Ex11
--Not sure name would be necessary for this view. customer_id is good enough
--for the purpose.
CREATE VIEW customer_overview AS
SELECT c.customer_id, c.first_name, c.city, COUNT(o.order_id) AS antal_order
FROM orders o
RIGHT JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id;

SELECT * FROM customer_overview;

--Ex12
-- Birth date is highly identifying data combined with name and city.
-- It should not be collected and stored unless absolutely necessary.
-- However both Sales and Marketting would demand this data point for their work.