--Lab1 Extra
--Level1
SELECT * FROM products WHERE category NOT IN ('Accessories') AND stock > 0 AND name LIKE '% %' ORDER BY category, price DESC;
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;
SELECT * FROM products ORDER BY price DESC LIMIT 1 OFFSET 1;
SELECT * FROM customers WHERE joined_date LIKE '2024%' OR joined_date LIKE '2025%' ORDER BY joined_date DESC LIMIT 3;

--Level2
SELECT (first_name || ' ' || last_name) AS full_name FROM customers ORDER BY last_name; --concat(first_name,' ',last_name)
SELECT *,
	CASE
		WHEN price < 200 THEN 'budget'
		WHEN price < 800 THEN 'mid'
		WHEN price > 800 THEN 'premium'
	END AS price_level
FROM products ORDER BY price_level;
SELECT first_name,COALESCE(city,'Unknown') FROM customers;
SELECT * FROM customers WHERE strftime('%m', joined_date) IN ('01','02','03','04','05','06');
SELECT * FROM products ORDER BY LENGTH(name) DESC LIMIT 1;
SELECT SUBSTR(email,1,instr(email,'@') -1) AS username FROM customers;

--Level3
SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);
SELECT (name || ' costs ' || SUBSTR(price,1,INSTR(price,'.')-1) || ' kr') AS price_list FROM products WHERE stock > 0 ORDER BY price ASC;
SELECT city, COUNT(customer_id) AS antal_kunder FROM customers GROUP BY city ORDER BY antal_kunder DESC;