import click
from dw.database import init_db, clear_db
from flask.cli import with_appcontext

@click.command('db-init')
@with_appcontext
def init_db_command():
    """Reads mapped files into db"""
    init_db()


@click.command('db-clear')
@with_appcontext
def clear_db_command():
    """Deletes all data from database"""
    clear_db()
