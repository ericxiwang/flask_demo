from flask import Flask
from config import Config
from app.extensions import db
from flask_jwt_extended import JWTManager
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'flask_demo'

    jwt = JWTManager(app)

    app.app_context().push()

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "toke_expired"})
    db.init_app(app)


    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import flask_api
    app.register_blueprint(flask_api, url_prefix='/api/v1')

    from app.oauth import oauth
    app.register_blueprint(oauth, url_prefix='/oauth')

    return app

if __name__ == "__main__":
    create_app(config_class=Config).run(host="0.0.0.0", debug=False, port=8080,threaded=True,ssl_context=('static/ssl_key/cert.pem', 'static/ssl_key/key.pem'))