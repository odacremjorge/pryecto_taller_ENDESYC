from flask_sqlalchemy import SQLAlchemy
from app import db

#La clase Registromecanicos es el modelo de asociacion 
# #entre dos modelos que lleva atributos
class Registromecanicos(db.Model):
    __tablename__ = 'registromecanicos'
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), primary_key=True)
    mecanico_id = db.Column(db.Integer, db.ForeignKey('mecanicos.id'), primary_key=True)
    seccion = db.Column(db.String(20))

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