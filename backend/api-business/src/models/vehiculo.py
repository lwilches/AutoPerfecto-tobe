

from src.models.base import db
from werkzeug.security import generate_password_hash, check_password_hash

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields 
from sqlalchemy.orm import relationship
from  sqlalchemy import ForeignKey

from datetime import datetime
import os

class Vehiculo(db.Model):
    __tablename__ = 'tbl_Vehiculo'
    id_vehiculo = db.Column(db.Integer,primary_key=True, autoincrement=True)
    marca = db.Column(db.String(80), nullable=False)
    placa = db.Column(db.String(80), unique=True, nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    kilometraje = db.Column(db.Numeric(18,2), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    cilindraje = db.Column(db.Numeric(18,2), nullable=False)
    tipo_combustible = db.Column(db.String(80), nullable=False)
    
    clients = relationship("ClientVehiculo", back_populates="vehiculo")


    def serialize(self):
        return {
            'id_vehiculo': self.id,
            'marca': self.marca,
            'placa': self.placa,
            'modelo': self.modelo,
            'kilometraje': self.kilometraje,
            'color': self.color,
            'cilindraje': self.cilindraje,
            'tipo_combustible': self.tipo_combustible
        }

