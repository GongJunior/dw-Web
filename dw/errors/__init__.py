from flask import Blueprint

bp = Blueprint('errors',__name__)

from dw.errors import handlers