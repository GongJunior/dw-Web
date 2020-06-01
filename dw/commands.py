import click
from dw.database import init_db
from flask.cli import with_appcontext

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
