--Lab 2
--Ex1
CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);
--Ex2
DROP TABLE books;

CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK(year > 1400)
);
--Ex3
ALTER TABLE books ADD COLUMN isbn TEXT;
--Ex4
DROP TABLE books;
--Ex5
CREATE TABLE reviews(
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER NOT NULL,
	rating INTEGER CHECK(rating >= 1 AND rating <= 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);
--Ex6
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES(1,5,6,'nope'); --constraint failed: rating ...
--Ex7
INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES(1,50,1,'nope'); --FOREIGN KEY constraint failed
--Ex8
--Yup