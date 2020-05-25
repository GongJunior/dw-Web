from dw import create_app, db
from dw.models import Name, Word
from dw.database import init_db

init_db()
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Name':Name, 'Word':Word}