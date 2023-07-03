from ..models import User, db, Book
from flask import Blueprint, jsonify, abort, request

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])
def index():
    result = []
    users = User.query.all()
    for u in users:
        result.append(u.serialize())
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    u = User.query.all()
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    engine = db.get_engine()
    with engine.connect() as conn:
        rows = conn.execute(f"INSERT INTO users(first_name, last_name, email) VALUES('{first_name}', '{last_name}', '{email}')")
        db.session.commit()
    return jsonify({'status': 'success', 'msg': 'user was added'})

@bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'first_name' in request.json:
        u.first_name=request.json['first_name']
    if 'last_name' in request.json:
        u.last_name=request.json['last_name']
    if 'email' in request.json:
        u.email=request.json['email']
    db.session.commit()
    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
    
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
