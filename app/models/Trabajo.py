from flask_sqlalchemy import SQLAlchemy
from app import db

class Trabajo(db.Model):
    __tablename__ = 'trabajos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.String(255))
    urlimage = db.Column(db.String(150))