--- users ---
INSERT INTO users (first_name, last_name, email)
VALUES ('Chloe', 'Caddell', 'chloecaddell@nucamp.edu'), ('Josh', 'Tietz', 'joshuatietz@gmail.com'), ('Sarah', 'Smith', 'sarahhhsmith12@yahoo.com'), ('Jon', 'Doe', 'jondoe123@yahoo.com');

--- employees ---
INSERT INTO employees (first_name, last_name, email)
VALUES ('Charlotte', 'Cash'), ('Margot', 'Sterling', 'msterling@unomaha.edu'), ('Jon', 'Smith', 'jsmith@smithindustries.com');

--- fines ---
INSERT INTO fines (total_amount, amount_paid, amount_due, user_id)
VALUES (20, 0, 20, 3), (20, 5, 15, 4);

--- status ---
INSERT INTO status (id, current_status)
VALUES (1, 'checked in'), (2, 'checked out'), (3, 'in maintenance');

--- genre ---
INSERT INTO genres (id, genre_type)
VALUES (1, 'young adult'), (2, 'childrens'), (3, 'non fiction'), (4, 'thriller'), (5, 'self help');

--- books ---
INSERT INTO books (ISBN, title, status_id, genre_id, employee_id)
VALUES (978-0-316-03619-1, 'FANG', 2, 1, null), (978-1-4549-2788-4, 'The Psychology Book', 1, 3, null), (978-1-913419-65-3, 'The Perfect Marriage', 3, 4, 1);
INSERT INTO books (ISBN, title, status_id, genre_id, employee_id)
VALUES (978-1-59184-513-3, 'The Chemistry Between Us', 2, 3, null), (978-1-63557-612-2, 'Dancing with the Octopus', 1, 5, null), (978-1-4767-2908-4, 'The Rosie Project', 2, 1, null), (978-0-439-02702-1, 'The Sea of Monsters', 3, 2, 2), (0-439-86130-6, 'The Lightening Thief', 2, 2, 2);
--- books checked out ---

INSERT INTO books_checked_out (due_date, check_out_date, book_id, user_id)
VALUES ('2023-6-30', '2023-5-29', 1, 2);
INSERT INTO books_checked_out (due_date, check_out_date, book_id, user_id)
VALUES ('2023-7-15', '2023-6-4', 4, 4), ('2023-7-10', '2023-6-4', 6, 2), ('2023-6-5', '2023-7-5', 8, 2);

--- books publisher id ---
INSERT INTO books_publisher (book_id, publisher_id)
VALUES (1, 1), (2, 2), (3, 3);
INSERT INTO books_publisher (book_id, publisher_id)
VALUES (4,4), (5,5), (6,6), (7,7), (8,8);
--- publishers ---
INSERT INTO publishers (publisher_name, published_date)
VALUES ('Little, Brown and Company', 2010), ('Sterling Publishing Co.', 2014), ('Bloodhound Books', 2020);
INSERT INTO publishers (publisher_name, published_date)
VALUES ('Penguin Group', 2012), ('Bloomsbury Publishing', 2020), ('Simon & Schuster Paperbacks', 2013), ('Scholastic Inc.', 2006), ('Scholastic Inc.', 2006);