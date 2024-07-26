from flask import Flask


def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.config.Config')

    #app.register_blueprint(auth_bp, url_prefix='/auth')

    return app