from flask import Blueprint, redirect, render_template, request, url_for
from dw.models import Name

bp = Blueprint('generate', __name__, url_prefix='/generate')

@bp.route('/diceware', methods=('GET','POST'))
def diceware():
    names = Name.query.all()
    return render_template('generate/diceware.html', names=names)