from flask_sqlalchemy import SQLAlchemy
from app import db

class Repuesto(db.Model):
    __tablename__ = 'repuestos'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    fechaPedido = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)
    unidad = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    solicitante = db.Column(db.String(50))

    # Atributo o la clave foranea
    ot_id = db.Column(db.Integer, db.ForeignKey('ots.id'), nullable=False)