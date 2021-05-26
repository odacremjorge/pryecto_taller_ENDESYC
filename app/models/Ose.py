from flask_sqlalchemy import SQLAlchemy
from app import db

class Ose(db.Model):
    __tablename__ = 'oses'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    taller = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    fechaInicio = db.Column(db.DateTime)
    fechaFinal = db.Column(db.DateTime)

    # Atributo o la clave foranea
    ot_id = db.Column(db.Integer, db.ForeignKey('ots.id'), nullable=False)