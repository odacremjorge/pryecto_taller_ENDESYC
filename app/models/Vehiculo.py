from flask_sqlalchemy import SQLAlchemy
from app import db

#Relacion de muchos a muchos
generarots = db.Table('generarots', db.Column('ot_id', db.Integer, db.ForeignKey('ots.id'), primary_key=True), db.Column('vehiculo_id', db.Integer, db.ForeignKey('vehiculos.id'), primary_key=True))


class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    cia = db.Column(db.String(50))
    empresa = db.Column(db.String(50))
    placa = db.Column(db.String(50), unique=True)
    tipo = db.Column(db.String(20))
    marca = db.Column(db.String(20))
    modelo = db.Column(db.String(20))
    año = db.Column(db.Integer)
    color = db.Column(db.String(20))
    cilindrada = db.Column(db.String(20))