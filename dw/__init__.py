from flask import Flask, redirect, url_for
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from dw.database import db_session, db, init_db

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
    def go_home():
        return redirect('/generate/diceware')
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    
    db.init_app(app)
    with app.app_context():
        from . import generate
        app.register_blueprint(generate.bp)
        from dw.commands import init_db_command
        app.cli.add_command(init_db_command)
        return app
    return app