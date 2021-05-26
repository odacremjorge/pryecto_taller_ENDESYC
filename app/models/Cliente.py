from flask_sqlalchemy import SQLAlchemy
from app import db


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    nit = db.Column(db.String(50))
    responsable = db.Column(db.String(50))
    # Referencia de relacion con modelos externos
    clientes = db.relationship('Ot.Asignarot', backref='asignarot', lazy=True, cascade="all, delete")