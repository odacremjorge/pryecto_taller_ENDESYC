from flask_sqlalchemy import SQLAlchemy
from app import db

class Asignarot(db.Model):
  __tablename__ = 'asignarots'
  usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
  ot_id = db.Column(db.Integer, db.ForeignKey('ots.id'), primary_key=True)
  tipotrabajo = db.Column(db.String(50))
# Atributo a las claves foraneas
  cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
  mecanico_id = db.Column(db.Integer, db.ForeignKey('mecanicos.id'), nullable=False)

  #asignarots = db.Table('asignarots', db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True), db.Column('ot_id', db.Integer, db.ForeignKey('ots.id'), primary_key=True))


class Ot(db.Model):
    __tablename__ = 'ots'
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    centroCosto = db.Column(db.Integer)
    empresa = db.Column(db.String(50))
    nit = db.Column(db.String(50))
    fechaInicio = db.Column(db.DateTime)
    fechaFinal = db.Column(db.DateTime)
    conductor = db.Column(db.String(50))
    responsable = db.Column(db.String(50))
    cia = db.Column(db.String(20))
    placa = db.Column(db.String(20))
    kilometrajeEntrada = db.Column(db.Integer)
    kilometrajeSalida = db.Column(db.Integer)
    descripcion = db.Column(db.String(200))
    estadoVehiculo = db.Column(db.String(200))
    mecanico = db.relationship("Asignarot")