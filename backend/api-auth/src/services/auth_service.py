from flask import jsonify
from jsonschema import ValidationError
from src.repositories.user_repository import UserRepository 
from  src.utils.validate_inputs import  validator
from  src.models.user import UserDTO , User 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register(self, dic_user ):
        
        result_validation  = validator.validate_json_add_user(dic_user)    
        if result_validation.success  ==  False : return jsonify({ "success": False ,  "message": result_validation.error }), 400
        
        try:
            user_dto = UserDTO().load(dic_user)
        except ValidationError as err:
            return jsonify({  "success": False   , "message": "Validation error", "errors": err.messages}), 400

        if self.user_repo.valide_user_name(user_dto["user_name"] ) == False : return jsonify({ "success": False ,  "message": "Nombre de usario no es valido"}), 409
        if self.user_repo.valide_doc(user_dto["tipo_doc"], user_dto["nro_doc"]  ) == False : return jsonify({ "success": False ,  "message": "Ya existe un usario"}), 409
        result , client_id  = self.user_repo.add_user(**user_dto)
        if result :
            return jsonify({  "success": True , "user_id" :client_id ,  "message": "Usuario registrado correctamente"}), 201
        else:
            return jsonify({  "success": False  , "message": "No fue posible registrar el usario "}), 500
        


    def login(self,dic_user):
        if not dic_user["user_name"] or not dic_user["pwd"]:
            return jsonify({"message": "Usuario y password son requeridos"}), 400
        state, id_client  = self.user_repo.verify_user(dic_user["user_name"], dic_user["pwd"])
        if state:
            access_token = create_access_token(identity={'user_name': dic_user["user_name"], 'id_client': id_client})
            return jsonify({ "success": True   ,  "user_id" :id_client  , "access_token" : access_token }), 200
        else:
            return jsonify({  "success": False ,   "message": "Credenciales inválidas"}), 401
    
        

    def change_password(self, id_client, new_password):
        if not id_client or not new_password:
            return jsonify({"message": "ID client and new password required"}), 400
        
        if self.user_repo.change_password(id_client, new_password):
            return jsonify({"message": "Password changed successfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
        
    
    def get_user_info(self, user_name):
        user = self.user_repo.find_user_by_name(user_name)
        if user:
            user_info = {
                'id_client': user.id_client,
                'user_name': user.user_name,
                'tipo_doc': user.tipo_doc,
                'nro_doc': user.nro_doc,
                'fecha_creacion': user.fecha_creacion,
                'fecha_modificacion': user.fecha_modificacion
            }
            return jsonify(user_info), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404    

auth_service = AuthService()