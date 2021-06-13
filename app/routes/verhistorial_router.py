from flask import Blueprint
from app.controllers.VerhistorialController import verhistorialcontroller
from flask_login import login_required

verhistorial_router = Blueprint('verhistorial_router', __name__)

@verhistorial_router.route('/verhistoriales',methods=['GET'])
@login_required
def verhistoriales():
    return verhistorialcontroller.index()

@verhistorial_router.route('/ingresar_detalle',methods=['POST'])
@login_required
def ingresar():
    return verhistorialcontroller.ingresarVerhistorial()


@verhistorial_router.route('/verhistoriales/verhistorial/<string:id>')
@login_required
def verhistorial(id):
    return verhistorialcontroller.verHistorial(id)

@verhistorial_router.route('/eliminar_verhistorial/<string:id>')
@login_required
def eliminarVerhistorial(id):
    return verhistorialcontroller.eliminarVerhistorial(id)