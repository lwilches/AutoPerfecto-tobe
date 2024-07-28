from flask import jsonify
from jsonschema import ValidationError
from  src.models import vehiculo 
from  src.utils.validate_inputs import  validator
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from src.repositories.client_vehiculo_repository import ClientVehiculoRepository  
from src.repositories.vehiculo_repository import VehiculoRepository 

class VehiculoService:
    def __init__(self):
        self.vehiculo_repo = VehiculoRepository()
        self.client_vehiculo_repo = ClientVehiculoRepository()
                

    def dar_auto(self ,  id_user,  id_vehiculo ):
        vehiculo = self.client_vehiculo_repo.get_vehiculo_by_client_and_vehiculo_id (  client_id=  id_user , vehiculo_id= id_vehiculo  )
        if vehiculo is None:
            return jsonify({ "success" : False ,  "message": "No existe el vehiculo"}), 404 
        return jsonify( {"success" : True ,  "message": "" ,  "data" : vehiculo  } , 200)  ; 
        
    def dar_autos(self,id_user   ):
        vehiculos = self.client_vehiculo_repo.get_vehiculos_by_client_id (  client_id=  id_user )
        if vehiculo is None  or len(vehiculos) == 0   :
            return jsonify({ "success" : False ,  "message": "No existe el vehiculos asociados al cliente"}), 404 
        return jsonify( {"success" : True ,  "message": "" ,  "data" : vehiculos  } , 200)  ; 
    

    def crear_auto(self, id_user ,   dic_data_vehiculo  ):
        
        if not all(key in dic_data_vehiculo for key in ("marca", "placa", "modelo", "kilometraje", "color", "cilindraje", "tipoDeCombustible")):
            return  jsonify({ "success" : False ,  "message":  "datos incompletos"}), 400

        if self.vehiculo_repo.get_vehiculo_by_placa( dic_data_vehiculo["placa"] ) :
            return jsonify({"success" : False , "message": "Vehiculo con la misma placa o marca ya existe"}), 409 
    
        if self.client_vehiculo_repo.get_vehiculo_by_client_and_placa( id_user, dic_data_vehiculo["placa"] ) :
            return jsonify({"success" : False , "message": "Vehiculo ya registrado a este cliente"}), 409 
        
        result = self.vehiculo_repo.add_vehiculo(**dic_data_vehiculo)       
        self.client_vehiculo_repo.add_client_vehiculo(
            id_vehiculo=result["id_vehiculo"],
            id_client=id_user,
            state='Activo'
        )            
        return jsonify({"success" : True , "message": "" ,  "data": { "id_client" :id_user , "id_vehiculo" :  result["id_vehiculo"]  } }), 201 
    
        
        
    
    def editar_auto(self, id_user , id_vehiculo ,  dic_data_vehiculo  ):
        
        if not all(key in dic_data_vehiculo for key in ("marca", "placa", "modelo", "kilometraje", "color", "cilindraje", "tipoDeCombustible")):
            return  jsonify({ "success" : False ,  "message":  "datos incompletos"}), 400

        if not self.client_vehiculo_repo.get_vehiculo_by_client_and_vehiculo_id  ( client_id=id_user , vehiculo_id= id_vehiculo  ) :
            return jsonify({"success" : False , "message": "Vehiculo no existe "}), 404 
    
        result = self.vehiculo_repo.edit_vehiculo( id_vehiculo, **dic_data_vehiculo)       

        return jsonify({"success" : True , "message": "" ,  "data": { "id_client" :id_user , "id_vehiculo" :  result["id_vehiculo"]  } }), 200 
    
            

vehiculo_service = VehiculoService()