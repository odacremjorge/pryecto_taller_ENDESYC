from flask_sqlalchemy import SQLAlchemy
from app import db

#Relacion de muchos a muchos
ingresartrabajos = db.Table('ingresartrabajos', db.Column('ot_id', db.Integer, db.ForeignKey('ots.id'), primary_key=True), db.Column('historial_id', db.Integer, db.ForeignKey('historiales.id'), primary_key=True))



class Historial(db.Model):
    __tablename__ = 'historiales'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    fecha = db.Column(db.DateTime)
    kilometraje = db.Column(db.Integer)
    conductor = db.Column(db.String(50))
    tipoMantenimiento = db.Column(db.String(50))
    cambioFiltro = db.Column(db.String(20))
    mecanico = db.Column(db.String(20))
    ot = db.Column(db.Integer, unique=True)
    repuestoCambiado = db.Column(db.String(200))
    servicioExterno = db.Column(db.String(200))

# Atributo o la clave foranea
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)