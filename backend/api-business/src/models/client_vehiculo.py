

from src.models.base import db
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from marshmallow import Schema, fields 
from sqlalchemy.orm import relationship
from  sqlalchemy import ForeignKey

from datetime import datetime
import os
from  src.models.vehiculo import Vehiculo


class ClientVehiculo(db.Model):
    __tablename__ = 'tbl_Client_Vehiculo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_vehiculo = db.Column(db.Integer, ForeignKey('tbl_Vehiculo.id_vehiculo'), nullable=False)
    id_client = db.Column(db.Integer,  nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    state = db.Column(db.String(50), nullable=False)

    vehiculo = relationship("Vehiculo", back_populates="clients")

    

class VehiculoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vehiculo
        load_instance = True
        include_relationships = False     
    
    
class ClientVehiculoSchema(Schema):
    vehiculo = fields.Nested(VehiculoSchema)
    class Meta:
        model = ClientVehiculo
        load_instance = True
        include_relationships = True
    
    