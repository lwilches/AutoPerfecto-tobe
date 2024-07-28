from flask import Flask
from datetime  import datetime
from src.controllers.auth_controller  import auth_bp
from src.config.manager_env import manager_env 
from  src.models.base import db
from flask_jwt_extended import JWTManager

app =  Flask(__name__) 
app.register_blueprint(auth_bp)
manager_env.load_vars_db()
manager_env.loads_vars_auth()

app.config['JWT_SECRET_KEY'] = manager_env.auth_token
app.config['SQLALCHEMY_DATABASE_URI'] = manager_env.sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db.init_app(app)
jwt = JWTManager(app)


class ManagerApp ():
    
    def __init__(self , app ) -> None:
        self.app = app
        
    def init_manager_app(self ) :
        with self.create_context():
            db.create_all()    ;
    
    def create_context(self ):
        return self.app.app_context()


manager_app = ManagerApp(app)

