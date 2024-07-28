import requests
from src.modelo.nuevo_auto_dto import NuevoAutoDTO

class ServicioAutos:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.autos = []

    def obtener_autos(self):
        url = f"{self.base_url}/propietario/2/vehiculos"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if response_data[0]["success"]:
                self.autos = [NuevoAutoDTO.from_dict(item) for item in response_data[0]["data"]]
                print(self.autos)
            else:
                print(f"Failed to retrieve autos: {response_data[0]['message']}")

        else:
            print(f"Failed to retrieve autos: {response.status_code} - {response.text}")

    def obtener_auto_por_id(self, id):
        url = f"{self.base_url}/vehiculos/{id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if response_data[0]["success"]:
                auto = NuevoAutoDTO.from_dict(response_data[0]["data"][0])
                self.mostrar_auto(auto)
            else:
                print(f"Failed to retrieve auto: {response_data[0]['message']}")
        else:
            print(f"Failed to retrieve auto: {response.status_code} - {response.text}")

    def crear_auto(self, auto_dto):
        url = f"{self.base_url}/vehiculos"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.post(url, json={"vehiculo": auto_dto.to_dict()}, headers=headers)

        if response.status_code == 201:
            print("Auto creado exitosamente.")
        else:
            print(f"Failed to create auto: {response.status_code} - {response.text}")

    def borrar_auto(self, id):
        url = f"{self.base_url}/vehiculos/{id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print("Auto borrado exitosamente.")
        else:
            print(f"Failed to delete auto: {response.status_code} - {response.text}")

    def modificar_auto(self, id, auto_dto):
        url = f"{self.base_url}/vehiculos/{id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.put(url, json={"vehiculo": auto_dto.to_dict()}, headers=headers)

        if response.status_code == 200:
            print("Auto modificado exitosamente.")
        else:
            print(f"Failed to update auto: {response.status_code} - {response.text}")

    def mostrar_autos(self):
        for auto in self.autos:
            self.mostrar_auto(auto)

    def mostrar_auto(self, auto):
        print(f"ID: {auto.id_vehiculo}, Marca: {auto.marca}, Modelo: {auto.modelo}, Color: {auto.color}, Kilometraje: {auto.kilometraje}, Placa: {auto.placa}, Tipo de Combustible: {auto.tipo_combustible}")

# Ejemplo de uso
if __name__ == "__main__":
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjIwODc0NCwianRpIjoiZWM0OGFmZjItMWZkNi00ODBhLTgzNWItMzYwMGNkNmQzYjhiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX25hbWUiOiJsd2lsY2hlcyIsImlkX2NsaWVudCI6Mn0sIm5iZiI6MTcyMjIwODc0NCwiY3NyZiI6IjNiNzgxZDU4LTcyYzktNGZkYy1iYTY3LTkzZmNmNWQzM2FmYiIsImV4cCI6MTcyMjIwOTY0NH0.QxtGSQnszqUJOg6pVyVj-LNSXc-SNxwrwpktYRtXx3s"  # Reemplaza con tu token real
    autos_service = ServicioAutos("http://auto-perfecto-business-api-qa.eba-nnmseqpw.us-east-1.elasticbeanstalk.com", token)
    
    # Obtener y mostrar todos los autos
    autos_service.obtener_autos()
    #autos_service.mostrar_autos()

    # Obtener y mostrar un auto específico por ID
    auto_id = 2  # Cambia esto al ID del auto que quieras consultar
    autos_service.obtener_auto_por_id(auto_id)
    
    # Crear un nuevo auto usando el DTO
    nuevo_auto_dto = NuevoAutoDTO(
        cilindraje="2.0",
        color="Negro",
        kilometraje="10000.00",
        marca="Honda",
        modelo="Civic",
        placa="ABC123",
        tipo_combustible="Gasolina"
    )
    autos_service.crear_auto(nuevo_auto_dto)
    
    # Modificar un auto existente usando el DTO
    auto_id_a_modificar = 1  # Cambia esto al ID del auto que quieras modificar
    datos_modificados_dto = NuevoAutoDTO(
        cilindraje="2.2",
        color="Rojo",
        kilometraje="15000.00",
        marca="Honda",
        modelo="Civic",
        placa="DEF456",
        tipo_combustible="Gasolina"
    )
    autos_service.modificar_auto(auto_id_a_modificar, datos_modificados_dto)
    
    # Borrar un auto por ID
    #auto_id_a_borrar = 1  # Cambia esto al ID del auto que quieras borrar
    #autos_service.borrar_auto(auto_id_a_borrar)
