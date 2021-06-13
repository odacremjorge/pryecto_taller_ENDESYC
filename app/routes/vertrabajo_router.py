from flask import Blueprint
from app.controllers.VertrabajoController import vertrabajocontroller
from flask_login import login_required

vertrabajo_router = Blueprint('vertrabajo_router', __name__)

@vertrabajo_router.route('/vertrabajos',methods=['GET'])
@login_required
def vertrabajos():
    return vertrabajocontroller.index()

@vertrabajo_router.route('/ingresar_trabajo',methods=['POST'])
@login_required
def ingresar():
    return vertrabajocontroller.ingresarVertrabajo()


@vertrabajo_router.route('/vertrabajos/vertrabajo/<string:id>')
@login_required
def vertrabajo(id):
    return vertrabajocontroller.verTrabajo(id)

@vertrabajo_router.route('/eliminar_vertrabajo/<string:id>')
@login_required
def eliminarVertrabajo(id):
    return vertrabajocontroller.eliminarVertrabajo(id)