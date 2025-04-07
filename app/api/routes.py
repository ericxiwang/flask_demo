from flask import render_template

from app.api import bp

@bp.route('/')

def index():
    return "api---1"

@bp.route('/api/')

def categories():
    return "api-2"