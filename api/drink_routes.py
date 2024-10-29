from flask import Flask, jsonify, request, Blueprint
from repositories.drink_repository import (
    db_get_drinks,
    db_get_drink_by_id
)

drink_routes = Blueprint('drink_routes', __name__)

# GET all drinks
@drink_routes.route('', methods=['GET'])
def get_drinks():
    try:
        drinks = db_get_drinks()
        return jsonify(drinks), 200 if drinks else 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET a drink by its ID
@drink_routes.route('/<int:drink_id>', methods=['GET'])
def get_drink_by_id(drink_id):
    try:
        drink = db_get_drink_by_id(drink_id)
        return jsonify(drink), 200 if drink else 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
