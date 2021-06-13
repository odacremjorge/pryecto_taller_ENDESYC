from flask import render_template, request, flash, redirect, url_for
from app import db
from app.models.Historial import Historial

class VerhistorialController():
    def __init__(self):
        pass

    def index(self):
        verhistoriales = Historial.query.all()
        return render_template('verhistoriales/verhistoriales.html', historiales=verhistoriales)
    
    def ingresarDetalle(self):
        
        verhistoriales = Historial(titulo = titulo, descripcion = descripcion, urlimage = urlimage)
        db.session.add(verhistorial)
        db.session.commit()
        return redirect(url_for('verhistorial_router.verhistoriales'))
    def verHistorial(self, _id):
        detalle = Historial.query.get(_id)
        return render_template('verhistoriales/detalle.html', detalle=detalle)

    def eliminarVerhistorial(self, _id):
        from app.models.Historial import Historial
        historial = Historial.query.get(_id)
        db.session.delete(historial)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('verhistorial_router.verhistoriales'))

    
verhistorialcontroller = VerhistorialController()