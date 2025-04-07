from flask import Flask

from config import Config

from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)


    # Initialize Flask extensions here

    # Register blueprints here
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/test')

    return app



if __name__ == "__main__":
    create_app(config_class=Config).run(host="0.0.0.0", debug=False, port=8080,threaded=True)