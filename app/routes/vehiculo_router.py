from flask import Blueprint
from app.controllers.VehiculoController import vehiculocontroller

vehiculo_router = Blueprint('vehiculo_router', __name__)

@vehiculo_router.route('/vehiculos',methods=['GET'])
def vehiculos():
    return vehiculocontroller.index()


@vehiculo_router.route('/crear_vehiculo',methods=['POST'])
def crear():
    return vehiculocontroller.crearVehiculo()

@vehiculo_router.route('/eliminar/<string:id>')
def eliminar(id):
    return vehiculocontroller.eliminarVehiculo(id)

@vehiculo_router.route('/editar/<string:id>')
def editar(id):
    return vehiculocontroller.editarVehiculo(id)
#Modificar registro
@vehiculo_router.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    return vehiculocontroller.actualizarVehiculo(id)