from flask import Blueprint, request, jsonify
from src.services.auth_service import auth_service 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('business', __name__)

@auth_bp.route('/propietario/{id_user}/vehiculos', methods=['POST'])
def register(id_user):
    data = request.get_json()
    return auth_service.register(data)


@auth_bp.route('/propietario/{id_user}/vehiculos', methods=['GET'])
def consultar_todos():
    data = request.get_json()
    return auth_service.register(data)



@auth_bp.route('/propietario/{id_user}/vehiculos/{id}', methods=['GET'])
def consultar(id):
    data = request.get_json()
    return auth_service.register(data)




@auth_bp.route('/propietario/{id_user}/vehiculos/{id}', methods=['PUT'])
def register(id_user):
    data = request.get_json()
    return auth_service.register(data)


