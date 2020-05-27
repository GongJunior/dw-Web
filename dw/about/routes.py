from flask import render_template, url_for
from dw.about import bp

@bp.route('/diceware')
def diceware():
    return render_template('about/diceware.html')

@bp.route('/project')
def project():
    return render_template('about/project.html')

@bp.route('/author')
def author():
    return render_template('about/author.html')