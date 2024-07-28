from flask import Blueprint, request, jsonify
from src.services.auth_service import auth_service 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return auth_service.register(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return auth_service.login(data)

@auth_bp.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    return auth_service.change_password(data)

@auth_bp.route('/user_info', methods=['GET'])
@jwt_required()
def user_info():
    current_user = get_jwt_identity()
    return auth_service.get_user_info(current_user['user_name'])