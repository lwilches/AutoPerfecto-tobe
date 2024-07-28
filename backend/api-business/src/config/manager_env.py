import os 
from dotenv import load_dotenv




class ManagerEnv:
    def __init__(self) -> None:

        self.dotenv_path = ".env.test"
        self.env = os.getenv("ENV") or ""
        if self.env != "":
            self.dotenv_path = ".env." + self.env 
            
        real_path = os.path.abspath(self.dotenv_path)    
        isOK = os.path.isfile(real_path)
            
        load_dotenv(self.dotenv_path)
        self.http_port= int(os.getenv('FLASK_RUN_PORT', 5000))
        self.db_name = "" 
        self.db_host = "" 
        self.db_port = "" 
        self.db_user = "" 
        self.db_password = "" 
        self.db_choice = "" 
        self.sqlalchemy_database_uri = ""
        
        self.ulr_service_post = ""  
        self.endpoint_consulta_post = ""  
        self.ulr_service_offer = ""  
        self.endpoint_consulta_offer = "" 
        self.endpoint_create_offer  = "" 
        self.endpoint_delete_offer  = "" 
        self.ulr_service_user  = ""  
        self.endpoint_consulta_user  = "" 
        self.auth_token  =  "f47fd06e-77b1-417e-8ff0-7e92fcbe97d6"
        self.url_users = "http://auto-perfecto-auth-api-qa.eba-2pznwn73.us-east-1.elasticbeanstalk.com/user_info"
        
    
    def loads_vars_auth(self):
        self.url_users = os.environ.get('URL_USERS', "http://auto-perfecto-auth-api-qa.eba-2pznwn73.us-east-1.elasticbeanstalk.com/user_info" )
        self.auth_token = os.environ.get('AUTH_TOKEN', "f47fd06e-77b1-417e-8ff0-7e92fcbe97d6" )
        
        
    def load_vars_db(self):
        
        self.db_name = os.environ.get('DB_NAME')
        self.db_host = os.environ.get('DB_HOST')
        self.db_port = os.environ.get('DB_PORT')
        self.db_user = os.environ.get('DB_USER')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_choice = os.environ.get('DB_CHOICE', 'postgres')
        
                
        if self.db_choice == 'sqlite':
            # Cadena de conexión para SQLite (en memoria)
            self.sqlalchemy_database_uri = f'sqlite:///{self.db_name}.db'
        elif self.db_choice == 'sqllite_memory':
            # Cadena de conexión para SQLite en memoria
            self.sqlalchemy_database_uri = 'sqlite:///:memory:'
        else:
            # Verifica si todas las variables necesarias para la conexión a PostgreSQL están definidas
            if self.db_host and self.db_port and self.db_user and self.db_password:
                self.sqlalchemy_database_uri = f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
            else:
                print("Faltan variables para la conexión a PostgreSQL.")
    
    
        
manager_env =  ManagerEnv()       