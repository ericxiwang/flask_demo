from flask import Flask, flash, redirect, url_for, request
from app.config import Config
from app.extensions import db
from model.models import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from flask_login import LoginManager, login_user,login_required, logout_user
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'flask_demo'
    db.init_app(app)

    CORS(app)
    ################### init flask login #################
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return USER_INFO.query.filter_by(id=user_id).first()

    @login_manager.unauthorized_handler
    def handle_needs_login():
        flash("You have to be logged in to access this page.")
        return redirect(url_for('main.login', next=request.endpoint))

    #################### init API JWT #################

    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "toke_expired"})

    ################# push app config to each sub module ################
    app.app_context().push()




    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import main
    app.register_blueprint(main)

    from app.api import flask_api
    app.register_blueprint(flask_api, url_prefix='/api/v1')

    from app.oauth import oauth
    app.register_blueprint(oauth, url_prefix='/oauth')

    return app

if __name__ == "__main__":
    create_app(config_class=Config).run(host="0.0.0.0", debug=False, port=8080,threaded=True,ssl_context=('static/ssl_key/cert.pem', 'static/ssl_key/key.pem'))
