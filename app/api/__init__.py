from flask import Blueprint

flask_api = Blueprint('flask_api', __name__)
from . import api_routes