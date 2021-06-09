from flask import Blueprint
from app.controllers.MecanicoController import mecanicocontroller
from flask_login import login_required

mecanico_router = Blueprint('mecanico_router', __name__)

@mecanico_router.route('/mecanicos',methods=['GET'])
@login_required
def mecanicos():
    return mecanicocontroller.index()


@mecanico_router.route('/crear_mecanico',methods=['POST'])
@login_required
def crear_mecanico():
    return mecanicocontroller.crearMecanico()

@mecanico_router.route('/eliminar_mecanico/<string:id>')
@login_required
def eliminar_mecanico(id):
    return mecanicocontroller.eliminarMecanico(id)

@mecanico_router.route('/editar_mecanico/<string:id>')
@login_required
def editar_mecanico(id):
    return mecanicocontroller.editarMecanico(id)

#Modificar registro

@mecanico_router.route('/actualizar_mecanico/<id>',methods=['POST'])
@login_required
def actualizar_mecanico(id):
    return mecanicocontroller.actualizarMecanico(id)