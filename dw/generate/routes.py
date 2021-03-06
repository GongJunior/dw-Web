from flask import render_template, url_for, jsonify
from dw.models import Name
from dw.generate import bp

@bp.route('/diceware')
def diceware():
    names = Name.query.all()
    return render_template('generate/diceware.html', names=names)

@bp.route('/lists')
def get_data():
    names = Name.query.all()
    dwLists = {}
    for i,name in enumerate(names):
        dwLists[name.name] = {}
        for word in names[i].words:
            dwLists[name.name][word.roll] = word.word

    return jsonify(dwLists)