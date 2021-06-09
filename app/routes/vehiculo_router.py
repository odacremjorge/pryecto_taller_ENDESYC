from flask import Blueprint
from app.controllers.VehiculoController import vehiculocontroller
from flask_login import login_required

vehiculo_router = Blueprint('vehiculo_router', __name__)

@vehiculo_router.route('/vehiculos',methods=['GET'])
@login_required
def principal():
    return vehiculocontroller.index()

@vehiculo_router.route('/vehiculos/crear',methods=['GET'])
@login_required
def crear():
    return vehiculocontroller.crearVehiculo()

@vehiculo_router.route('/vehiculos/guardar',methods=['POST'])
@login_required
def guardar():
    return vehiculocontroller.guardarVehiculo()

@vehiculo_router.route('/vehiculos/eliminarvehiculo/<string:id>')
@login_required
def eliminar(id):
    return vehiculocontroller.eliminarVehiculo(id)

@vehiculo_router.route('/vehiculos/editar/<string:id>')
@login_required
def editar(id):
    return vehiculocontroller.editarVehiculo(id)

@vehiculo_router.route('/vehiculos/actualizarvehiculo/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return vehiculocontroller.actualizarVehiculo(id)
