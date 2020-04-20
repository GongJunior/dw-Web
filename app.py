from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__),'diceware.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)),"dw.db")}'
db = SQLAlchemy(app)

class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    words = db.relationship('Words', backref='names', lazy=True)

class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer, nullable=False) 
    word = db.Column(db.String(120), nullable=False)
    listname_id = db.Column(db.Integer, db.ForeignKey('names.id'), nullable=False)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#if __name__ == "__main__":
#    app.run(debug=True)