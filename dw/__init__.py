from flask import Flask, redirect, url_for
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from dw.database import db_session

db = SQLAlchemy()

def create_app(test_config='config.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_object(test_config)
    try:
        Path(app.instance_path).mkdir(parents=True)
    except FileExistsError:
        pass

    @app.route('/')
    def go_home():
        return redirect(url_for('generate.diceware'))
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    
    db.init_app(app)

    from . import generate, about
    app.register_blueprint(generate.bp)
    app.register_blueprint(about.bp)

    from dw.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from dw.commands import init_db_command
    app.cli.add_command(init_db_command)
    
    return app