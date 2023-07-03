from ..models import Book, db, User
from flask import Blueprint, jsonify, abort, request

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/search', methods=['GET'])
def search(title: str):
    b = db.session.query(Book)
    if 'title' in request.json:
        search = b.title=request.json['title']
        b.filter(Book.title.like([search]))
    return jsonify(b.serialize)


@bp.route('', methods=['GET'])
def index():
    result = []
    books = Book.query.all()
    for b in books:
        result.append(b.serialize())
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    title = request.json['title']
    ISBN = request.json['ISBN']
    status_id = request.json['status_id']
    genre_id = request.json['genre_id']
    employee_id = request.json['employee_id']
    author = request.json['author']
    engine = db.get_engine()
    with engine.connect() as conn:
        rows = conn.execute(
            f"INSERT INTO books(title, ISBN, status_id, genre_id, employee_id, author) VALUES('{title}', '{ISBN}', {status_id}, {genre_id}, {employee_id}, '{author}')")
        db.session.commit()
    return jsonify({'status': 'success', 'msg': 'book was added'})


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    b = Book.query.get_or_404(id)
    try:
        db.session.delete(b) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    b = Book.query.get_or_404(id)
    if 'title' in request.json:
        b.title=request.json['title']
    if 'ISBN' in request.json:
        b.ISBN=request.json['ISBN']
    if 'status_id' in request.json:
        b.status_id=request.json['status_id']
    if 'genre_id' in request.json:
        b.genre_id=request.json['genre_id']
    if 'employee_id' in request.json:
        b.employee_id=request.json['employee_id']
    if 'author' in request.json:
        b.author=request.json['author']
    db.session.commit()
    try:
        db.session.commit()
        return jsonify(b.serialize())
    except:
        return jsonify(False)
