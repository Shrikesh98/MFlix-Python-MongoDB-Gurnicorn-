from flask import Blueprint

movies_blueprint = Blueprint('movies', __name__, url_prefix='/movies')