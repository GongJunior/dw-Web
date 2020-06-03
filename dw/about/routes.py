from flask import render_template, url_for
from dw.about import bp
from dw.models import Name

@bp.route('/diceware')
def diceware():
    curr_lists = Name.query.all()
    return render_template('about/diceware.html', names=curr_lists)

@bp.route('/project')
def project():
    return render_template('about/project.html')

@bp.route('/author')
def author():
    return render_template('about/author.html')

@bp.route('lists/<listname>')
def get_list(listname):
    curr_lists = Name.query.filter(Name.name==listname).first()
    return render_template('about/lists.html', name=curr_lists.name, rolls=curr_lists.words)