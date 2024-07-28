import sys
from PyQt5.QtWidgets import QApplication
from src.vista.InterfazAutoPerfecto import App_AutoPerfecto
from src.logica.Logica_mock import Logica_mock
from src.logica.propietario import Propietario

# URL de la API atutenicacion AWS
#base_url = "http://127.0.0.1:5000"  --Test Local
base_url = "http://auto-perfecto-auth-api-qa.eba-2pznwn73.us-east-1.elasticbeanstalk.com"

if __name__ == '__main__':
    
    # Punto inicial de la aplicación

    logica = Propietario(base_url)

    app = App_AutoPerfecto(sys.argv, logica)
    sys.exit(app.exec_())