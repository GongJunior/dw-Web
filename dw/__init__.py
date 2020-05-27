from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
migrate = Migrate()

def create_app(config='config.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_object(config)
    try:
        Path(app.instance_path).mkdir(parents=True)
    except FileExistsError:
        pass

    if not app.debug or not app.testing:
        if not Path('logs').exists():
            Path('logs').mkdir()
        file_handler = RotatingFileHandler('logs/dw.log',maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('dw startup')

    @app.route('/')
    def go_home():
        return redirect(url_for('generate.diceware'))
    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db_session.remove()
    
    db.init_app(app)
    migrate.init_app(app, db)

    from dw.about import bp as about_bp
    app.register_blueprint(about_bp, url_prefix='/about')

    from dw.generate import bp as gen_bp
    app.register_blueprint(gen_bp, url_prefix='/generate')

    from dw.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # from dw.commands import init_db_command
    # app.cli.add_command(init_db_command)
    
    return app

from dw import models