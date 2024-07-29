from datetime import datetime
from setuptools import sic

from sqlalchemy import Float, Integer
from src.modelo.declarative_base import engine, Base, Session
from src.modelo.nuevo_auto_dto import NuevoAutoDTO
from src.logica.service_auth_user import ServicioAuthUser
from src.modelo.vehiculo import Vehiculo
from src.modelo.mantenimiento import Mantenimiento
from src.modelo.accion import Accion
import  requests
from types import SimpleNamespace

class Propietario():

    def __init__(self, base_url):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.token = ""
        self.success = False
        self.user_id = -1
        self.servicio_auth_user = ServicioAuthUser(base_url)
    
    # Autenticación de usuario	a modificar con API

    def autenticar_usuario(self, usuario, contrasena):

        print(f'Usuario: {usuario}, Contraseña: {contrasena}')

        # Obtencion de Token de API Autenticacion AWS
        
        self.servicio_auth_user.authenticate(usuario, contrasena)

        print(f"Token: {self.servicio_auth_user.token}")

        # Validacion de autenticacion -Respuesta a Vista-Login

        if self.servicio_auth_user.success:
            self.token = self.servicio_auth_user.token
            self.success = self.servicio_auth_user.success
            self.user_id = self.servicio_auth_user.user_id
            return True
        else:
            return False
        
       

    def dar_autos(self):
        #verificar si el usuario esta autenticado
        print(f'Usuario ID: {self.user_id}')
        # invocar api para obtener autos
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        url = f'http://auto-perfecto-business-api-qa.eba-nnmseqpw.us-east-1.elasticbeanstalk.com/propietario/{self.user_id}/vehiculos'
    
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Levanta una excepción para respuestas de error
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return False

        data = response.json()
        
        if not data.get('success'):
            print(f"Error en la respuesta: {data.get('message', 'Unknown error')}")
            return False 
        
        vehiculos_data  = data.get('data', [])
        
        vehiculos = []
        for vehiculo_entry in vehiculos_data:
            vehiculo = vehiculo_entry.get('vehiculo', {})
            vehiculo['vendido'] = False  # Añadir la columna 'vendido'
            vehiculos.append(vehiculo)
                
        
        # Aplanar el array de vehículos
        vehiculos = [vehiculo_entry.get('vehiculo', {}) for vehiculo_entry in vehiculos_data]
    
        if len(vehiculos) ==  0 :
            return False 
        return  vehiculos
        


      

    def dar_auto(self, id):
        
        
        # invocar api para obtener autos
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        url = f'http://auto-perfecto-business-api-qa.eba-nnmseqpw.us-east-1.elasticbeanstalk.com/propietario/{self.user_id}/vehiculos/{id}'
    
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Levanta una excepción para respuestas de error
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return False
        
        
        data = response.json()
        
        if not data.get('success'):
            print(f"Error en la respuesta: {data.get('message', 'Unknown error')}")
            return False 
        
        vehiculo_data  = data.get('data', {})
        if vehiculo_data  is None  or vehiculo_data == {}: 
            return  False 
        
        vehiculo  = SimpleNamespace(**vehiculo_data)
        return vehiculo


    def crear_auto(self, marca, placa, modelo, kilometraje, color, cilindraje, tipoDeCombustible):
        
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        url = f'http://auto-perfecto-business-api-qa.eba-nnmseqpw.us-east-1.elasticbeanstalk.com/propietario/{self.user_id}/vehiculos'
    
        new_vehiculo = {
            "marca" : marca ,
            "placa" : placa  ,
            "modelo" : modelo ,
            "kilometraje" : kilometraje ,
            "color" : color ,
            "cilindraje" :cilindraje  ,
            "tipo_combustible" : tipoDeCombustible
        }
        try:
            response = requests.post(url, headers=headers , json = new_vehiculo)
            response.raise_for_status()  # Levanta una excepción para respuestas de error
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return False

        

    def editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipo_combustible):
        session = Session()
        vehiculos = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
        busqueda_placa = session.query(Vehiculo).filter(Vehiculo.placa == placa).all()
        busqueda_marca = session.query(Vehiculo).filter(Vehiculo.marca == marca).all()
        if len(vehiculos) != 0 and len(busqueda_placa) <= 1 and len(busqueda_marca) <= 1 and len(placa) != 0 and len(marca) != 0 and len(modelo) != 0 and kilometraje != 0 and len(color) != 0 and len(cilindraje) != 0 and len(tipo_combustible) != 0:
            for vehiculo in vehiculos:
                vehiculo.marca = marca
                vehiculo.placa = placa
                vehiculo.modelo = modelo 
                vehiculo.kilometraje = kilometraje
                vehiculo.color = color
                vehiculo.cilindraje = cilindraje
                vehiculo.tipo_combustible = tipo_combustible
                session.commit()
                session.close()
            return True
        else:
            return False

    def vender_auto(self, id, kilometraje_venta, valor_venta):
        if valor_venta >= 0 and kilometraje_venta >= 0:
            session = Session()
            busqueda = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
            if len(busqueda) >> 0 and kilometraje_venta != 0 and valor_venta != 0:
                for vehiculo in busqueda:
                    vehiculo.vendido = True
                    vehiculo.kilometraje_venta = kilometraje_venta
                    vehiculo.valor_venta = valor_venta
                    session.commit()
                    session.close()
                return True
            else:
                return False
        else:
            return False

    def eliminar_auto(self, id):
        session = Session()
        vehiculos = session.query(Vehiculo).filter(Vehiculo.id == id+1).all()
        if len(vehiculos) != 0:
            for vehiculo in vehiculos:
                session.delete(vehiculo)
                session.commit()
                session.close()
                return True
        else:
            return False

    def validar_crear_editar_auto(self, id, marca, placa, modelo, kilometraje, color, cilindraje, tipoDeCombustible):
        if kilometraje != 0:
            return True
        else:
            return False

    def validar_vender_auto(self, id, kilometraje_venta, valor_venta):
        validacion = False
        try:
            float(kilometraje_venta)
            float(valor_venta)
            validacion = True
        except ValueError:
            validacion = False
        return validacion

    def dar_mantenimientos(self):
            session = Session()
            mantenimientos = session.query(Mantenimiento).all()
            session.close()
            if len(mantenimientos) != 0 :
                return mantenimientos
            else:
                return False
    


    def aniadir_mantenimiento(self, nombre, descripcion):
        session = Session()
        busqueda = session.query(Mantenimiento).filter(Mantenimiento.nombre == nombre).all()
        if len(busqueda) == 0 and len(nombre) != 0 and len(descripcion) != 0:
            mantenimiento = Mantenimiento(nombre = nombre, descripcion = descripcion)
            session.add(mantenimiento)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False

    def editar_mantenimiento(self, id, nombre, descripcion):
        session = Session()
        mantenimientos = session.query(Mantenimiento).filter(Mantenimiento.id == id+1).all()
        if len(mantenimientos) != 0 and len(nombre) != 0 and len(descripcion) != 0:
            for mantenimiento in mantenimientos:
                mantenimiento.nombre = nombre
                mantenimiento.descripcion = descripcion
                session.commit()
                session.close()
            return True
        else:
            return False

    def eliminar_mantenimiento(self, id):
        session = Session()
        mantenimientos = session.query(Mantenimiento).filter(Mantenimiento.id == id+1).all()
        if len(mantenimientos) != 0:
            for mantenimiento in mantenimientos:
                session.delete(mantenimiento)
                session.commit()
                session.close()
                return True
        else:
            return False
    
    def validar_crear_editar_mantenimiento(self, nombre, descripcion):
        validacion = False
        if nombre!=None and descripcion!=None:
            validacion = True
        return validacion
    
    def dar_acciones_auto(self, id_auto):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_auto == id_auto+1).all()
        if len(acciones) == 0:
            return False
        else:
            return acciones

    def dar_accion(self, id_auto, id_accion):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_accion == id_accion+1).all()
        for accion in acciones:
            return accion

    def crear_accion(self, mantenimiento, id_auto, valor, kilometraje, fecha):
        session = Session()
        Session.expire_on_commit = False
        if type(mantenimiento) == str:
            mantenimiento = session.query(Mantenimiento).filter(Mantenimiento.nombre == mantenimiento).first()
        if  valor != 0 and kilometraje != 0:
            accion = Accion(id_auto = id_auto+1, mantenimiento = mantenimiento, valor = valor, kilometraje = kilometraje, fecha = datetime.strptime(str(fecha), "%Y-%m-%d"))
            session.add(accion)
            session.commit()
            
            return True    
        else:
            session.close()
            return False 

    def editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        session = Session()
        acciones = session.query(Accion).filter(Accion.id_accion == id_accion+1).all()
        if len(acciones) != 0  and mantenimiento != None and id_auto+1 != 0 and valor != 0 and kilometraje != 0 and len(fecha) != 0:
            for accion in acciones:
                accion.id_auto = id_auto+1
                accion.valor = valor
                accion.kilometraje = kilometraje
                accion.fecha = datetime.strptime(str(fecha), "%Y-%m-%d")
                session.commit()
                session.close()
            return True
        else:
            return False

    def eliminar_accion(self, id_auto, id_accion):
        session = Session()
        accion = session.query(Accion).filter(Accion.id_accion == id_accion+1).first()
        if accion != None:
            session.delete(accion)
            session.commit()
            session.close()
            return True
        else:
            return False

    def validar_crear_editar_accion(self, id_accion, mantenimiento, id_auto, valor, kilometraje, fecha):
        validacion = False
        try:
            float(kilometraje)
            float(valor)
            validacion = True
        except ValueError:
            validacion = False
        return validacion

    def dar_reporte_ganancias(self, id_auto):
        session = Session()
        vehiculo = session.query(Vehiculo).filter(Vehiculo.id == id_auto+1).first()
        if vehiculo != None :
            acciones = session.query(Accion).filter(Accion.id_auto == id_auto+1).all()
            if len(acciones) != 0:
                total = 0
                gastos = []
                kilometraje = 0
                for accion in acciones:
                    gastos += [accion.fecha.year, accion.valor]
                    kilometraje += accion.kilometraje
                    total += accion.valor 
                gastos += [('Total',total)]
                gastos = [x for x in zip(*[iter(gastos)]*2)]
                return gastos, kilometraje
            else:
                session.close()
                return [('Total',0)], 0 
        else:
            return False


    