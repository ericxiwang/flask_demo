from flask import Flask
from app.config import Config
from app.extensions import db
from model.models import *
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'flask_demo'
    db.init_app(app)

    jwt = JWTManager(app)

    app.app_context().push()

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "toke_expired"})


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