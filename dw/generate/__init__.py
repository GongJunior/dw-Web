from flask import Blueprint

bp = Blueprint('generate', __name__)

from dw.generate import routes