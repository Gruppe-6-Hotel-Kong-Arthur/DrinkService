from flask import Flask, jsonify, request, Blueprint
from repositories.drink_repository import (
    db_get_drinks,
    db_get_drink_by_id,
    db_update_units_sold
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


# PUT to update the units sold for a drink
@drink_routes.route('/drinks/<int:drink_id>/update', methods=['PUT'])
def update_units_sold(drink_id):
    try:
        data = request.get_json()
        amount = data.get('amount')
        db_update_units_sold(drink_id, amount)
        return jsonify({'message': 'Units sold updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
