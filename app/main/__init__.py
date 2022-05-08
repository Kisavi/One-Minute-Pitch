from flask import Blueprint

# instantiate the Blueprint
main = Blueprint(__name__)

from . import views
