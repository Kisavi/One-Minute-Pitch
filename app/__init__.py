from flask import Flask  # import the Flask class from flask module
from config import config_options


def create_app(config_name):  # a method to instantiate our App
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    return app
