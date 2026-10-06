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
--DROP TABLE product_suppliers;
CREATE TABLE product_suppliers(
	product_id INTEGER,
	supplier_id INTEGER,
	purchase_price REAL CHECK(purchase_price > 0),
	PRIMARY KEY(product_id, supplier_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
INSERT INTO product_suppliers(product_id,supplier_id)
VALUES	(1,99);
--FOREIGN KEY constraint failed
--there is no supplier_id 99

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
--DROP TABLE product_sizes;
CREATE TABLE product_sizes(
	size_id INTEGER PRIMARY KEY,
	product_id INTEGER,
	size TEXT,
	stock INTEGER DEFAULT 0,
	UNIQUE (product_id, size),
	CHECK (size IN ('S','M','L','XL')),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);
INSERT INTO product_sizes(size_id, product_id, size, stock)
VALUES	(1, 2,'M',5),
		(2, 2,'M',5);
--UNIQUE constraint failed: product_sizes.product_id, product_sizes.size

--Ex11
DROP TABLE employees;
CREATE TABLE employees(
	employee_id INTEGER PRIMARY KEY,
	manager INTEGER,
	FOREIGN KEY (manager) REFERENCES employees(employee_id)
);
INSERT INTO employees(employee_id, manager)
VALUES	(1,NULL), --bossman
		(2,1),
		(3,1);

--Ex12
CREATE TABLE teams(
	name TEXT PRIMARY KEY
);
CREATE TABLE players(
	name TEXT PRIMARY KEY,
	team TEXT,
	FOREIGN KEY (team) REFERENCES teams(name) 
		ON DELETE CASCADE
);
INSERT INTO teams(name)
VALUES('Goa Gubbar');
INSERT INTO players(name, team)
VALUES	('Bengt','Goa Gubbar'),
		('Börje','Goa Gubbar');
SELECT * FROM teams;
SELECT * FROM players;
DELETE FROM teams WHERE name = 'Goa Gubbar';
SELECT * FROM players; 
--poof