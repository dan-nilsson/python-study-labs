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



