from flask import Blueprint

bp = Blueprint('about', __name__)

from dw.about import routes