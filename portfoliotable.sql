CREATE TABLE users (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE fines (
    id SERIAL,
    total_amount INT,
    amount_paid INT,
    amount_due INT,
    user_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE books_checked_out (
    id SERIAL,
    due_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    book_id INT,
    user_id INT,
    PRIMARY KEY(id)
);

CREATE TABLE books (
    id SERIAL,
    ISBN INT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    status_id INT NOT NULL,
    genre_id INT NOT NULL,
    employee_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE employees (
    id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE status (
    id INT,
    current_status TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE genres (
    id INT,
    genre_type TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE publishers (
    id SERIAL,
    publisher_name TEXT NOT NULL,
    published_date DATE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE books_publisher (
    book_id INT NOT NULL,
    publisher_id INT NOT NULL,
    PRIMARY KEY (book_id, publisher_id)
);

--- ALTER TABLES ---

--- one to many ---
ALTER TABLE fines
ADD CONSTRAINT fk_users_fines
FOREIGN KEY (user_id)
REFERENCES users (id);

--- one to many ---
ALTER TABLE books_checked_out
ADD CONSTRAINT fk_users_books_checked_out
FOREIGN KEY (user_id)
REFERENCES users (id);

--- one to many ---
ALTER TABLE books_checked_out
ADD CONSTRAINT fk_books_checked_out_books
FOREIGN KEY (book_id)
REFERENCES books (id);

--- one to one ---
ALTER TABLE books
ADD CONSTRAINT fk_books_status
FOREIGN KEY (status_id)
REFERENCES status (id);

--- one to one ---
ALTER TABLE books
ADD CONSTRAINT fk_books_genre
FOREIGN KEY (genre_id)
REFERENCES genre (id);

--- many to many ---
ALTER TABLE books_publisher
ADD CONSTRAINT fk_books_publishers_books
FOREIGN KEY (book_id)
REFERENCES books (id);

--- many to many ---
ALTER TABLE books_publisher
ADD CONSTRAINT fk_books_publishers_publishers
FOREIGN KEY (publisher_id)
REFERENCES publishers (id);

--- one to many ---
ALTER TABLE books
ADD CONSTRAINT fk_books_employees
FOREIGN KEY (employee_id)
REFERENCES employees (id);

-- additions to books --
ALTER TABLE books
ADD COLUMN authors TEXT,
UPDATE books
SET authors = 'James Patterson'
WHERE title = 'Fang'








