class NuevoAutoDTO:
    def __init__(self, cilindraje, color, kilometraje, marca, modelo, placa, tipo_de_combustible, user_id):
        self.cilindraje = cilindraje
        self.color = color
        self.kilometraje = kilometraje
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.tipo_de_combustible = tipo_de_combustible
        self.user_id = user_id

    def to_dict(self):
        return {
            "cilindraje": self.cilindraje,
            "color": self.color,
            "kilometraje": self.kilometraje,
            "marca": self.marca,
            "modelo": self.modelo,
            "placa": self.placa,
            "tipoDeCombustible": self.tipo_de_combustible,
            "userId": self.user_id
        }

# Ejemplo de uso
if __name__ == "__main__":
    nuevo_auto_dto = NuevoAutoDTO(
        cilindraje="2.0",
        color="Negro",
        kilometraje=10000,
        marca="Honda",
        modelo="Civic",
        placa="ABC123",
        tipo_de_combustible="Gasolina"
    )
    auto_dict = nuevo_auto_dto.to_dict()
    print(auto_dict)
