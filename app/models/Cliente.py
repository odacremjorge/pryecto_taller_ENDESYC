from flask_sqlalchemy import SQLAlchemy
from app import db

class Registroclientes(db.Model):
    __tablename__ = 'registroclientes'
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), primary_key=True)
    fecharegistro = db.Column(db.DateTime)
    seccioncliente = db.Column(db.String(50))


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    nombre = db.Column(db.String(50))
    nit = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    # Atributo o la clave foranea
    #mecanico_id = db.Column(db.Integer, db.ForeignKey('mecanicos.id'), nullable=False)
