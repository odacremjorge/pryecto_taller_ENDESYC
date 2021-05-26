from flask import Blueprint
from app.controllers.MecanicoController import mecanicocontroller

mecanico_router = Blueprint('mecanico_router', __name__)

@mecanico_router.route('/mecanicos',methods=['GET'])
def mecanicos():
    return mecanicocontroller.index()


@mecanico_router.route('/crear_mecanico',methods=['POST'])
def crear_mecanico():
    return mecanicocontroller.crearMecanico()

@mecanico_router.route('/eliminar_mecanico/<string:id>')
def eliminar_mecanico(id):
    return mecanicocontroller.eliminarMecanico(id)

@mecanico_router.route('/editar_mecanico/<string:id>')
def editar_mecanico(id):
    return mecanicocontroller.editarMecanico(id)

#Modificar registro

@mecanico_router.route('/actualizar_mecanico/<id>',methods=['POST'])
def actualizar_mecanico(id):
    return mecanicocontroller.actualizarMecanico(id)