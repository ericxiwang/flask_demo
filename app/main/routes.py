from app.main import bp
from flask import render_template

@bp.route('/')

def login():
    return render_template('login.html')

@bp.route('/index')
def index():
    return render_template('index.html')