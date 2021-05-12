from app.models.User import User
from app.models.Vehiculo import Vehiculo
from app.models.Mecanico import Mecanico
from app.models.Ot import Ot
from app.models.Cliente import Cliente
from app import db

db.drop_all()
db.create_all()

""" alumno = Alumno(nombres='Pedro',apellidos = 'Smith', email = 'pedro@mail.com', celular='7634566')
db.session.add(alumno)
db.session.commit()  """