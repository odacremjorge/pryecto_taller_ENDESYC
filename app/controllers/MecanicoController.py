from flask import render_template, request, flash, redirect, url_for
from app import db

class MecanicoController():
    def __init__(self):
        pass

    def index(self):
        from app.models.Mecanico import Mecanico
        mecanicos = Mecanico.query.all()
        return render_template('mecanico/mecanicos.html', mecanicos=mecanicos)
    
    def crearMecanico(self):
        if request.method == 'POST':
            nombreMecanico = request.form['nombreMecanico']
            cargo = request.form['cargo']
            telefono = request.form['telefono']
           

            from app.models.Mecanico import Mecanico
            mecanico = Mecanico(nombreMecanico = nombreMecanico, cargo = cargo, telefono = telefono)
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

    def editarMecanico(self, _id):
        from app.models.Mecanico import Mecanico
        mecanico = Mecanico.query.get(_id)
        return render_template('mecanico/editar.html', title='Editar', mecanico = mecanico)

    def actualizarMecanico(self, _id):
        if request.method == 'POST':
            nombreMecanico = request.form['nombreMecanico']
            cargo = request.form['cargo']
            telefono = request.form['telefono']
            

            from app.models.Mecanico import Mecanico
            mecanico = Mecanico.query.get(_id)
            mecanico.nombreMecanico = nombreMecanico 
            mecanico.cargo = cargo
            mecanico.telefono = telefono
            
            
            db.session.commit()

            flash('Registro actualizado con exito')
            return redirect(url_for('mecanico_router.mecanicos'))


mecanicocontroller = MecanicoController()