from flask import render_template, request, flash, redirect, url_for
from app import db

class MecanicoController():
    def __init__(self):
        pass

    def index(self):
        from app.models.Mecanico import Mecanico
        mecanicos = Mecanico.query.all()
        return render_template('mecanicos.html', mecanicos=mecanicos)
    
    def crearMecanico(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            cargo = request.form['cargo']
           

            from app.models.Mecanico import Mecanico
            mecanico = Mecanico(nombre = nombre, cargo = cargo)
            db.session.add(mecanico)
            db.session.commit()

            flash('Registro exitoso')
            return redirect(url_for('mecanico_router.mecanicos'))

    def eliminarMecanico(self, _id):
        from app.models.Mecanico import Mecanico
        mecanico = Mecanico.query.get(_id)
        db.session.delete(mecanico)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('mecanico_router.mecanicos'))


mecanicocontroller = MecanicoController()