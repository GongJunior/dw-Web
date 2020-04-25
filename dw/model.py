from dw import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    words = db.relationship('Word', backref='name', lazy=True)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer, nullable=False) 
    word = db.Column(db.String(120), nullable=False)
    listname_id = db.Column(db.Integer, db.ForeignKey('name.id'), nullable=False)