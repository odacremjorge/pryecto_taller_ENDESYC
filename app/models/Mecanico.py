from flask_sqlalchemy import SQLAlchemy
from app import db

class Mecanico(db.Model):
    __tablename__ = 'mecanicos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    # Referencia de relacion con modelos externos
    #ots = db.relationship('Ots', backref='mecanico', lazy=True, cascade="all, delete")
    #clientes = db.relationship('Clientes', backref='cliente', lazy=True, cascade="all, delete")
