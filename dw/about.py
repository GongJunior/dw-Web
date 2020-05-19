from flask import Blueprint, render_template, url_for

bp = Blueprint('about', __name__, url_prefix='/about')

@bp.route('/diceware')
def diceware():
    return render_template('about/diceware.html')

@bp.route('/project')
def project():
    return render_template('about/project.html')

@bp.route('/author')
def author():
    return render_template('about/author.html')