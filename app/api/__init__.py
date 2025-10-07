from flask import Blueprint

flask_api = Blueprint('flask_api', __name__)
from . import api_routes
from . import bug_api_routes
from . import dashboard_api_routes
from . import user_api_routes