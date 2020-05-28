from dw import create_app, db
from dw.models import Name, Word
from config import DevConfig

app = create_app(DevConfig)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Name':Name, 'Word':Word}