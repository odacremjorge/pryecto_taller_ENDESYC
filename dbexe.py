from app.models.User import User
from app.models.Vehiculo import Vehiculo
from app.models.Ot import Ot
from app.models.Mecanico import Mecanico
from app.models.Cliente import Cliente
from app.models.Historial import Historial
from app.models.Repuesto import Repuesto
from app.models.Ose import Ose
from app import db

#db.drop_all()
db.create_all()

