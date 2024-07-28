
from sqlalchemy.orm.exc import NoResultFound
from src.models.base import db
from src.models.vehiculo   import Vehiculo 
from src.models.client_vehiculo import  VehiculoSchema


class VehiculoRepository:

    def add_vehiculo(self, placa, modelo, marca, color ,   kilometraje, cilindraje, tipo_combustible):
        new_vehiculo = Vehiculo(
            placa=placa,
            modelo=modelo,
            marca = marca,
            color =color ,
            kilometraje=kilometraje,
            cilindraje=cilindraje,
            tipo_combustible=tipo_combustible
        )
        db.session.add(new_vehiculo)
        db.session.commit()
        vehiculo_schema = VehiculoSchema()
        data_vehiculo = vehiculo_schema.dump(new_vehiculo)
        return data_vehiculo
    
    
    def get_vehiculo_by_placa(self, placa):
        vehiculo = db.session.query(Vehiculo).filter_by(placa=placa).first()
        vehiculo_schema = VehiculoSchema()
        return vehiculo_schema.dump(vehiculo)
    
    
    def get_vehiculo_by_placa(self, placa ):
        vehiculo = db.session.query(Vehiculo).filter_by(placa = placa ).first()
        vehiculo_schema = VehiculoSchema()
        return vehiculo_schema.dump(vehiculo)
    
    def edit_vehiculo(self, id_vehiculo, placa=None, modelo=None, kilomentraje=None, cilindraje=None, tipo_combustible=None):
        vehiculo = db.session.query(Vehiculo).filter_by(id_vehiculo=id_vehiculo).first()       
        if placa:
            vehiculo.placa = placa
        if modelo:
            vehiculo.modelo = modelo
        if kilomentraje:
            vehiculo.kilomentraje = kilomentraje
        if cilindraje:
            vehiculo.cilindraje = cilindraje
        if tipo_combustible:
            vehiculo.tipo_combustible = tipo_combustible
        
        db.session.commit()
        vehiculo_schema = VehiculoSchema()
        return vehiculo_schema.dump(vehiculo)