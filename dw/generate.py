from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from dw.models import Name

bp = Blueprint('generate', __name__, url_prefix='/generate')

@bp.route('/diceware', methods=('GET','POST'))
def diceware():
    names = Name.query.all()
    return render_template('generate/diceware.html', names=names)

@bp.route('/lists')
def get_data():
    names = Name.query.all()
    dwLists = {}
    for name in names:
        dwLists[name.name] = {}
        for word in names[0].words:
            dwLists[name.name][word.roll] = word.word

    return jsonify(dwLists)