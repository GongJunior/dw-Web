from dw import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Name(db.Model):
    __tablename__ = 'names'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    words = relationship('Word', backref='name', lazy=True, cascade="all, delete-orphan")
    def __repr__(self):
        return f"<Name {self.name}>"

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Integer, nullable=False) 
    word = db.Column(db.String(120), nullable=False)
    listname_id = db.Column(db.Integer, db.ForeignKey('names.id'), nullable=False)
    def __repr__(self):
        return f"<Word {self.roll}>"