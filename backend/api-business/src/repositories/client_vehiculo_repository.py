
from sqlalchemy.orm.exc import NoResultFound
from src.models.base import db
from src.models.client_vehiculo   import ClientVehiculo ,  ClientVehiculoSchema
from src.models.vehiculo import Vehiculo



class ClientVehiculoRepository:
    
    
    
    def add_client_vehiculo(self, id_vehiculo, id_client, state):
        new_client_vehiculo = ClientVehiculo(
            id_vehiculo=id_vehiculo,
            id_client=id_client,
            state=state
        )
        db.session.add(new_client_vehiculo)
        db.session.commit()
        return new_client_vehiculo

    def get_vehiculos_by_client_id(self, client_id):
        results = db.session.query(ClientVehiculo).join(Vehiculo).filter(ClientVehiculo.id_client == client_id).all()
        client_vehiculo_schema = ClientVehiculoSchema()
        return client_vehiculo_schema.dump(results, many=True)

    def get_vehiculo_by_client_and_vehiculo_id(self, client_id, vehiculo_id):
        result = db.session.query(ClientVehiculo).join(Vehiculo).filter(ClientVehiculo.id_client == client_id, ClientVehiculo.id_vehiculo == vehiculo_id).first()
        client_vehiculo_schema = ClientVehiculoSchema()
        return client_vehiculo_schema.dump(result)
    

    def get_vehiculo_by_client_and_placa(self, client_id, placa):
        result = self.session.query(ClientVehiculo).join(Vehiculo).filter(ClientVehiculo.id_client == client_id, Vehiculo.placa == placa).first()
        client_vehiculo_schema = ClientVehiculoSchema()
        return  client_vehiculo_schema.dump(result)
        
    
    