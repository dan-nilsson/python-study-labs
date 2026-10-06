--Lab2 Extra
--Level1
--Ex1
CREATE TABLE suppliers(
	supplier_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	country TEXT DEFAULT 'Sweden',
	email TEXT,
	UNIQUE(name)
);
--Ex2
INSERT INTO suppliers(supplier_id, name, email)
VALUES(1,'Leverans AB','info@leverans.se');
SELECT * FROM suppliers; --Sweden

--Ex3
INSERT INTO suppliers(supplier_id, name, email)
VALUES(2,'Nordisc Textiles','info@nordictex.se');
INSERT INTO suppliers(supplier_id, name, email)
VALUES(3,'Nordisc Textiles','info@nordictex.se');
--UNIQUE constraint failed: suppliers.name

--Ex4
CREATE TABLE coupons(
	code TEXT PRIMARY KEY,
	discount_percent INTEGER 
		CHECK(discount_percent > 0 AND discount_percent <= 90),
	valid_until TEXT NOT NULL
);
INSERT INTO coupons(code,discount_percent,valid_until)
VALUES('SUMMER20',95,'2026-10-31');
--CHECK constraint failed: discount_percent ...

--Level2
--Ex5
INSERT INTO suppliers(name, email)
VALUES('Bosses Verkstad AB','bosse@hotmail.com');
SELECT * FROM suppliers;
--supplier_id=3. since PRIMARY KEY is needed auto-incremented insert is added.

--Ex6
ALTER TABLE suppliers RENAME COLUMN email TO contact_email;

--Ex7
PRAGMA table_info(products);

--Ex8
CREATE TABLE product_suppliers(
	purchase_price REAL CHECK(purchase_price > 0)
);

--Ex9
CREATE TABLE campaign(
	name TEXT NOT NULL,
	start_date TEXT NOT NULL,
	end_date TEXT,
	CHECK(start_date < end_date)
);
INSERT INTO campaign(name, start_date, end_date)
VALUES('HöstREA','2026-10-10','2026-10-01');
--CHECK constraint failed: start_date < end_date

--Ex10
