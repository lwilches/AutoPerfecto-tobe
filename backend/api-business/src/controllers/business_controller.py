from flask import Blueprint, request, jsonify
from src.controllers import token_required
from src.services.vehiculo_service import vehiculo_service 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
vehiculos_bp = Blueprint('business', __name__)



@vehiculos_bp.route('/propietario/<int:id_user>/vehiculos/<int:id>', methods=['GET'])
@token_required
def dar_auto(id_user,  id_vehiculo ):
    return vehiculo_service.dar_auto(id_user,  id_vehiculo )


@vehiculos_bp.route('/propietario/<int:id_user>/vehiculos', methods=['POST'])
def crear_auto(id_user):
    data = request.get_json()
    return  vehiculo_service.crear_auto(id_user,  data )


@vehiculos_bp.route('/propietario/<int:id_user>/vehiculos', methods=['GET'])
def dar_autos(id_user):
    data = request.get_json()
    return vehiculo_service.dar_autos(id_user)



@vehiculos_bp.route('/propietario/<int:id_user>/vehiculos/<int:id>', methods=['PUT'])
def editar(id_user  , id):
    data = request.get_json()
    return vehiculo_service.editar_auto(id_user ,id  , data )




