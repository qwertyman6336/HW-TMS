CREATE TABLE authors (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);


CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);


CREATE TABLE sales (
    id INT PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);


INSERT INTO authors (id, first_name, last_name) VALUES
(1, 'Leo', 'Tolstoy'),
(2, 'Fyodor', 'Dostoevsky'),
(3, 'Anton', 'Chekhov');


INSERT INTO books (id, title, author_id, publication_year) VALUES
(1, 'War and Peace', 1, 1869),
(2, 'Crime and Punishment', 2, 1866),
(3, 'The Cherry Orchard', 3, 1904);


INSERT INTO sales (id, book_id, quantity) VALUES
(1, 1, 10),
(2, 2, 15),
(3, 3, 20);


SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;


SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;


SELECT books.title, authors.first_name, authors.last_name
FROM books
RIGHT JOIN authors ON books.author_id = authors.id;



SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON books.id = sales.book_id;


SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id;


SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;


SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity), 0) AS total_sales
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id
GROUP BY authors.id;



SELECT authors.first_name, authors.last_name
FROM authors
WHERE authors.id = (
    SELECT books.author_id
    FROM sales
    INNER JOIN books ON sales.book_id = books.id
    GROUP BY books.author_id
    ORDER BY SUM(sales.quantity) DESC
    LIMIT 1
);


SELECT books.title
FROM books
INNER JOIN sales ON books.id = sales.book_id
WHERE sales.quantity > (
    SELECT AVG(quantity) FROM sales
);
