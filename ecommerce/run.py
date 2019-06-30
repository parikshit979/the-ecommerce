import os
from flask import Flask
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == "__main__":
    config_name = os.environ.get('APP_SETTINGS', '')
    app = create_app(config_name)
    app.run(debug=True)
