from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, id: int, first_name: str, last_name: str, email: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_type = db.Column(db.String, nullable=False)

    def __init__(self, id: int, genre_type: str):
        self.id = id
        self.genre_type = genre_type

    def serialize(self):
        return {
            'id': self.id,
            'genre_type': self.genre_type
        }


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current_status = db.Column(db.String, nullable=False)

    def __init__(self, id: int, current_status: str):
        self.id = id
        self.current_status = current_status

    def serialize(self):
        return {
            'id': self.id,
            'current_status': self.current_status
        }


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String)
    title = db.Column(db.String(128), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey(Status.id))
    status = db.relationship('Status', foreign_keys='Book.status_id')
    genre_id = db.Column(db.Integer, db.ForeignKey(Genre.id))
    genre = db.relationship('Genre', foreign_keys='Book.genre_id')
    employee_id = db.Column(db.Integer, db.ForeignKey(Employee.id))
    employee = db.relationship('Employee', foreign_keys='Book.employee_id')
    author = db.Column(db.String)

    def __init__(self, id: int, isbn: str, title: str, status_id: int, genre_id: int, employee_id: int, author: str):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.status_id = status_id
        self.genre_id = genre_id
        self.employee_id = employee_id
        self.author = author

    def serialize(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'title': self.title,
            'status_id': self.status_id,
            'genre_id': self.genre_id,
            'employee_id': self.employee_id,
            'author': self.author
        }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)

    def __init__(self, id: int, first_name: str, last_name: str, email: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }


class Fine(db.Model):
    __tablename__ = 'fines'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_amount = db.Column(db.Integer)
    amount_paid = db.Column(db.Integer)
    amount_due = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship('User', foreign_keys=('Fine.user_id'))

    def __init__(self, id: int, total_amount: int, amount_paid: int, amount_due: int, user_id: int):
        self.id = id
        self.total_amount = total_amount
        self.amount_paid = amount_paid
        self.amount_due = amount_due
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'total_amount': self.total_amount,
            'amount_paid': self.amount_paid,
            'amount_due': self.amount_due,
            'user_id': self.user_id
        }


class Books_checked_out(db.Model):
    __tablename__ = 'books_checked_out'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    due_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id))
    book = db.relationship('Book', foreign_keys='Books_checked_out.book_id')
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship('User', foreign_keys='Books_checked_out.user_id')

    def __init__(self, id: int, due_date, check_out_date, book_id: int, user_id: int):
        self.id = id
        self.due_date = due_date
        self.check_out_date = check_out_date
        self.book_id = book_id
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'due_date': self.due_date,
            'check_out_date': self.check_out_date,
            'book_id': self.book_id,
            'user_id': self.user_id
        }


class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    publisher_name = db.Column(db.String, nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int, publisher_name: str, published_year: int):
        self.id = id
        self.publisher_name = publisher_name
        self.published_year = published_year

    def serialize(self):
        return {
            'id': self.id,
            'publisher_name': self.publisher_name,
            'published_year': self.published_year
        }


books_publisher = db.Table(
    'books_publisher',
    db.Column(
        'book_id', db.Integer,
        db.ForeignKey(Book.id),
        primary_key=True
    ),

    db.Column(
        'publisher_id', db.Integer,
        db.ForeignKey(Publisher.id),
        primary_key=True
    )
)
