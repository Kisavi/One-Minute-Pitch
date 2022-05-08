from flask import Flask


def create_app(): # a method to instantiate our App
    app = Flask(__name__)

    return app
