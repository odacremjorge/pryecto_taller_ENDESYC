from flask_sqlalchemy import SQLAlchemy
from app import db


class Mecanico(db.Model):
    __tablename__ = 'mecanicos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombreMecanico = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
# Referencia de relacion con modelos externos
    #mecanicos = db.relationship('Ot.Asignarot', backref='asignarot', lazy=True, cascade="all, delete")
 