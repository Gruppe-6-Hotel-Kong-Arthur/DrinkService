from flask import Flask, jsonify, request, Blueprint
from repositories.drink_repository import (
    db_get_drinks,
)

drink_routes = Blueprint('drink_routes', __name__)
# GET all drinks
@drink_routes.route('/drinks', methods=['GET'])
def get_drinks():
    try:
        drinks = db_get_drinks()
        return jsonify(drinks), 200 if drinks else 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

