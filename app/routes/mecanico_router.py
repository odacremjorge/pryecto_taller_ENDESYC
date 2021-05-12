from flask import Blueprint
from app.controllers.MecanicoController import mecanicocontroller

mecanico_router = Blueprint('mecanico_router', __name__)

@mecanico_router.route('/mecanicos',methods=['GET'])
def mecanicos():
    return mecanicocontroller.index()


@mecanico_router.route('/crear_mecanico',methods=['POST'])
def crear():
    return mecanicocontroller.crearMecanico()

@mecanico_router.route('/eliminar/<string:id>')
def eliminar(id):
    return mecanicocontroller.eliminarMecanico(id)