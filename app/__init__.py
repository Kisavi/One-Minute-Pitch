from flask import Flask  # import the Flask class from flask module
from config import config_options
from flask_bootstrap import Bootstrap


def create_app(config_name):  # a method to instantiate our App
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    bootstrap = Bootstrap()  # Initializing Bootstrap class
    # Initializing flask extensions
    bootstrap.init_app(app)

    return app
