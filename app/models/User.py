from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True,  autoincrement=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    rol =db.Column(db.String(50))
    

     # Referencia de relacion con modelos externos
   # usuarios = db.relationship('Asignarot', backref='asignarots', lazy=True, cascade="all, delete")

