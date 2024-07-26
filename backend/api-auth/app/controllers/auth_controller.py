from flask import Blueprint, request, jsonify
#from app.services.auth_service import AuthService

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