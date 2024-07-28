from src.models.user import User
from sqlalchemy.orm.exc import NoResultFound
from src.models.base import db
from src.models.user   import User , UserSchema  


class UserRepository:
    def add_user(self, user_name, pwd  , tipo_doc  , nro_doc, nombres , apellidos  )  :
        user = User(user_name = user_name ,  pwd = pwd , tipo_doc = tipo_doc  ,nro_doc = nro_doc , nombres = nombres ,apellidos = apellidos )
        user.set_password(pwd)
        db.session.add(user)
        db.session.commit()
        return True , user.id_client 

    def valide_user_name(self, user_name):
        if User.query.filter_by( user_name  = user_name  ).first():
            return False  
        
    def valide_doc(self ,tipo_doc, nro_doc ):
        if User.query.filter_by( tipo_doc  = tipo_doc ,  nro_doc = nro_doc ).first():
            return False   

    def verify_user(self, user_name, password):
        user = User.query.filter_by(user_name=user_name).first()
        if user and user.check_password(password):
            return True , user.id_client 
        return False 

    def change_password(self, user_name, new_password):
        user = User.query.filter_by(user_name=user_name).first()
        if user:
            user.set_password(new_password)
            db.session.commit()
            return True
        return False

    def find_user_by_name(self, user_name) :
        return User.query.filter_by(user_name=user_name).first()