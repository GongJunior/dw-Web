from dw.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Name(Base):
    __tablename__ = 'names'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    words = relationship('Word', backref='name', lazy=True)

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    roll = Column(Integer, nullable=False) 
    word = Column(String(120), nullable=False)
    listname_id = Column(Integer, ForeignKey('names.id'), nullable=False)