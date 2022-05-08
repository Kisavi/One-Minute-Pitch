from flask import Flask  # import the Flask class from flask module
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initializing SQLAlchemy claas
DB_NAME = 'watchlist.db'


def create_app(config_name):  # a method to instantiate our App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # initialise our db

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    return app
