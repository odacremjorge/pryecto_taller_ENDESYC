from flask_sqlalchemy import SQLAlchemy
from app import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(50))
    celular = db.Column(db.String(50))
    rol =db.Column(db.String(50))
    cuenta =db.Column(db.String(50))
    password =db.Column(db.String(50))

     # Referencia de relacion con modelos externos
    usuarios = db.relationship('Asignarot', backref='asignarots', lazy=True, cascade="all, delete")

