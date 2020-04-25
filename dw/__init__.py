from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{Path(app.instance_path) / "dw.db"}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        Path(app.instance_path).mkdir(parents=True)
    except FileExistsError:
        pass
    @app.route('/')
    def hello_world():
        return 'Hi mom!!!'
    
    db.init_app(app)
    with app.app_context():
        from . import model
        from . import db_setup
        app.cli.add_command(db_setup.init_db_command)
        return app