from flask import render_template
from dw.errors import bp


@bp.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500