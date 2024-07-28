

from src.models.base import db
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields 
from sqlalchemy.orm import relationship
from  sqlalchemy import ForeignKey
from  src.models.client_vehiculo import ClientVehiculoSchema

from datetime import datetime
import os

class User(db.Model):
    __tablename__ = 'tbl_cliente'
    id_client = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Autonumérico
    user_name = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario
    pwd = db.Column(db.String(128), nullable=False)  # Hash de la contraseña
    salt = db.Column(db.String(32), nullable=False)  
    tipo_doc = db.Column(db.String(32), nullable=False)  # Tipo de documento
    nro_doc = db.Column(db.String(30), nullable=False)  # Número de documento
    nombres =  db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Fecha de creación
    fecha_modificacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Fecha de modificación

    def set_password(self, password):
        """Genera un hash de la contraseña con un salt y lo almacena."""
        self.salt = os.urandom(16).hex()  # Genera un salt de 16 bytes y lo almacena en hexadecimal
        self.pwd = generate_password_hash(password + self.salt)

    def check_password(self, password):
        return check_password_hash(self.pwd, password + self.salt)



class UserSchema(Schema):
    id_client = fields.Int(dump_only=True)  # Campo solo de lectura
    user_name = fields.Str(required=True)
    pwd = fields.Str(load_only=True)  # Campo solo de escritura
    tipo_doc = fields.Str(required=True)
    nro_doc = fields.Str(required=True)
    nombres = fields.Str(required=True)
    apellidos = fields.Str(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)  # Campo solo de lectura
    fecha_modificacion = fields.DateTime(dump_only=True)  # Campo solo de lectura
    
    
class UserDTO(Schema):
    user_name = fields.Str(required=True)
    tipo_doc = fields.Str(required=True)
    nro_doc = fields.Str(required=True)
    nombres = fields.Str(required=True)
    apellidos = fields.Str(required=True)
    pwd  = fields.Str(required=True, load_only=True)    
    
    