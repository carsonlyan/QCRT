from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from qcrt.main import main as main_blueprint
    from qcrt.author import author as author_blueprint
    from qcrt.ajax import ajax as ajax_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(author_blueprint)
    app.register_blueprint(ajax_blueprint)
    return app