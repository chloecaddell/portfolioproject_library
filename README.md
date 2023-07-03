# My Library
My Library was designed to upload information about books, users, and employees.
The user is able to change information about the books. There is a table to keep track of books that users have checked out and fines users have for books that are overdue.
## API Reference Table of endpoint paths, methods, and parameters
'''
PUT http://localhost:5000/books/book_id
{
    "title": "Through the Looking Glass",
   "ISBN": "938-1234-56",
   "status_id": 1,
   "genre_id": 2,
   "employee_id": 1,
   "author": "Lewis B. Carroll"
}
'''
'''
POST http://localhost:5000/books
{
    "title": "Through the Looking Glass",
   "ISBN": "938-1234-56",
   "status_id": 1,
   "genre_id": 2,
   "employee_id": 1,
   "author": "Lewis B. Carroll"
}
'''
'''
GET http://localhost:5000/books
'''
'''
DELETE http://localhost:5000/books/book_id
'''
## Evolution of My Library
When building the ERD a lot of changes were made during that process.
Originally it was just basic book information and the users. When I started thinking about information a real library would need I added genres to organize where books would go in a Library. Then I added on fines for users with late books. 
### Future Improvements
Later I would like to add a function that assigns a due date based on the check out date as well as one that can assign a fine for each day late.
Later I would like to add a function to allow users to check out books and one to allow employees to update the status of books.
### ORM or raw SQL?
Originally My Library was going to use raw SQL, but I was confused on how to use it and had started writing it using an ORM. So in order to save time I ended up sticking with using an ORM.# portfolio_project
# portfolio_project
