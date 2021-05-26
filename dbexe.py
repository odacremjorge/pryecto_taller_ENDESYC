from app.models.Vehiculo import Vehiculo
from app.models.Usuario import Usuario
from app.models.Ot import Ot
from app.models.Mecanico import Mecanico
from app.models.Cliente import Cliente
from app.models.Historial import Historial
from app.models.Repuesto import Repuesto
from app.models.Ose import Ose
from app import db

#db.drop_all()
db.create_all()

""" alumno = Alumno(nombres='Pedro',apellidos = 'Smith', email = 'pedro@mail.com', celular='7634566')
db.session.add(alumno)
db.session.commit()  """