from flask import Blueprint
from app.controllers.HistorialController import historialcontroller
from flask_login import login_required

historial_router = Blueprint('historial_router', __name__)

@historial_router.route('/historiales',methods=['GET'])
@login_required
def main():
    return historialcontroller.index()
@historial_router.route('/historiales/crear',methods=['GET'])
@login_required
def crear():
    return historialcontroller.crearHistorial()
@historial_router.route('/guardar_historial',methods=['POST'])
@login_required
def create():
    return historialcontroller.guardarHistorial()

@historial_router.route('/eliminar/<string:id>')
@login_required
def eliminar(id):
    return historialcontroller.eliminarHistorial(id)

@historial_router.route('/editar/<string:id>')
@login_required
def editar(id):
    return historialcontroller.editarHistorial(id)

@historial_router.route('/actualizar/<id>',methods=['POST'])
@login_required
def actualizar(id):
    return historialcontroller.actualizarHistorial(id)
