from flask_sqlalchemy import SQLAlchemy
from app import db

# Relacion de uno a Muchos
detalleots = db.Table('detalleots',
    db.Column('vehiculo_id', db.Integer, db.ForeignKey('vehiculos.id'), primary_key=True),
    db.Column('ot_id', db.Integer, db.ForeignKey('ots.id'), primary_key=True)
)

class Ot(db.Model):
    __tablename__ = 'ots'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    centroCosto = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    fecha = db.Column(db.DateTime)
    # Atributo o la clave foranea
   # mecanico_id = db.Column(db.Integer, db.ForeignKey('mecanicos.id'), nullable=False)