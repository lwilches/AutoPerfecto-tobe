import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazAutoPerfecto import App_AutoPerfecto
from src.logica.Logica_mock import Logica_mock
from src.logica.propietario import Propietario


base_url = "http://127.0.0.1:5000" # URL de la API atutenicacion AWS

if __name__ == '__main__':
    
    # Punto inicial de la aplicación

    logica = Propietario(base_url)

    app = App_AutoPerfecto(sys.argv, logica)
    sys.exit(app.exec_())