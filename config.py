from os import environ
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(__file__).parent.absolute()
load_dotenv(dotenv_path=Path(basedir / '.env', verbose=True))

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URI') or f"sqlite:///{Path(basedir / 'intance/dw.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY')

class DevConfig(Config):
    SECRET_KEY='dev'
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True