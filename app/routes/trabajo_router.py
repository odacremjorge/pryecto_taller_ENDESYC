from flask import Blueprint
from app.controllers.TrabajoController import trabajocontroller
from flask_login import login_required

trabajo_router = Blueprint('trabajo_router', __name__)

@trabajo_router.route('/trabajos',methods=['GET'])
@login_required
def main():
    return trabajocontroller.index()
@trabajo_router.route('/trabajos/crear',methods=['GET'])
@login_required
def crear():
    return trabajocontroller.crearTrabajo()
@trabajo_router.route('/guardar_trabajo',methods=['POST'])
@login_required
def create():
    return trabajocontroller.guardarTrabajo()

@trabajo_router.route('/eliminar/<string:id>')
@login_required
def eliminar(id):
    return trabajocontroller.eliminarTrabajo(id)

@trabajo_router.route('/editar/<string:id>')
@login_required
def editar(id):
    return trabajocontroller.editarTrabajo(id)

@trabajo_router.route('/actualizar/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return trabajocontroller.actualizarTrabajo(id)
