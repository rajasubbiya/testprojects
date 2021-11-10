from flask import Blueprint, request, Response, jsonify
from app.models import Shoes, db

shoes_bp = Blueprint('shoes', __name__, url_prefix='/api/v1/shoes')


@shoes_bp.route("/northface", methods=['GET', 'POST'])
def shoes_northface():
    if request.method == 'GET':
        query_params = request.args
        if not query_params:
            shoes = Shoes.query.all()
            result = [shoe.to_dict() for shoe in shoes]
            return jsonify(result)

        shoes = Shoes.query.filter(Shoes.gender == query_params['gender'])
        result = [shoe.to_dict() for shoe in shoes]
        return jsonify(result)

    if request.method == 'POST':
        data = request.form
        shoe_to_add = Shoes(model=data['model'], gender=data['gender'], size=data['size'])
        db.session.add(shoe_to_add)
        db.session.commit()
        response = Response(status=201)
        response.headers['location'] = f"northface/{shoe_to_add.id}"
        return response

@shoes_bp.route("/northface/<int:shoe_id>", methods=['GET', 'DELETE'])
def shoe_id_fiction(shoe_id):

    if Shoes.query.get(shoe_id) is None:
        response = Response(status=404)
        return response

    if request.method == 'GET':
        shoe = Shoes.query.get(shoe_id)
        return jsonify(shoe.to_dict())

    if request.method == 'DELETE':
        shoe = Shoes.query.get(shoe_id)
        db.session.delete(shoe)
        db.session.commit()
        response = Response(status=200)
        return response