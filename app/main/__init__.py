from flask import Blueprint

# instantiate the Blueprint
main = Blueprint(__name__, 'main')

from . import views
