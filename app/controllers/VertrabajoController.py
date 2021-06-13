from flask import render_template, request, flash, redirect, url_for
from app import db
from app.models.Trabajo import Trabajo

class VertrabajoController():
    def __init__(self):
        pass

    def index(self):
        vertrabajos = Trabajo.query.all()
        return render_template('vertrabajos/vertrabajos.html', trabajos=vertrabajos)
    
    def ingresarTrabajo(self):
        
        vertrabajos = Trabajo(titulo = titulo, descripcion = descripcion, urlimage = urlimage)
        db.session.add(vertrabajo)
        db.session.commit()
        return redirect(url_for('vertrabajo_router.vertrabajos'))
    def verTrabajo(self, _id):
        trabajo = Trabajo.query.get(_id)
        return render_template('vertrabajos/trabajo.html', trabajo=trabajo)

    def eliminarVertrabajo(self, _id):
        from app.models.Trabajo import Trabajo
        trabajo = Trabajo.query.get(_id)
        db.session.delete(trabajo)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('vertrabajo_router.vertrabajos'))


    
vertrabajocontroller = VertrabajoController()