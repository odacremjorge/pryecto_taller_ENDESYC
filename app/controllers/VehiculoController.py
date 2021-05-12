from flask import render_template, request, flash, redirect, url_for
from app import db

class VehiculoController():
    def __init__(self):
        pass

    def index(self):
        from app.models.Vehiculo import Vehiculo
        vehiculos = Vehiculo.query.all()
        return render_template('vehiculos.html', vehiculos=vehiculos)
    
    def crearVehiculo(self):
        if request.method == 'POST':
            cia = request.form['cia']
            empresa = request.form['empresa']
            placa = request.form['placa']
            tipo = request.form['tipo']
            marca = request.form['marca']
            modelo = request.form['modelo']
            año = request.form['año']
            color = request.form['color']
            cilindrada = request.form['cilindrada']

            from app.models.Vehiculo import Vehiculo
            vehiculo = Vehiculo(cia = cia, empresa = empresa, placa = placa, tipo = tipo, marca = marca, modelo = modelo, año = año, color = color, cilindrada = cilindrada)
            db.session.add(vehiculo)
            db.session.commit()

            flash('Registro exitoso')
            return redirect(url_for('vehiculo_router.vehiculos'))

    def eliminarVehiculo(self, _id):
        from app.models.Vehiculo import Vehiculo
        vehiculo = Vehiculo.query.get(_id)
        db.session.delete(vehiculo)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('vehiculo_router.vehiculos'))

    def editarVehiculo(self, _id):
        from app.models.Vehiculo import Vehiculo
        vehiculo = Vehiculo.query.get(_id)
        return render_template('editar.html', title='Editar', vehiculo = vehiculo)

    def actualizarVehiculo(self, _id):
        if request.method == 'POST':
            cia = request.form['cia']
            empresa = request.form['empresa']
            placa = request.form['placa']
            tipo = request.form['tipo']
            marca = request.form['marca']
            modelo = request.form['modelo']
            año = request.form['año']
            color = request.form['color']
            cilindrada = request.form['cilindrada']

            from app.models.Vehiculo import Vehiculo
            vehiculo = Vehiculo.query.get(_id)
            vehiculo.cia = cia 
            vehiculo.empresa = empresa
            vehiculo.placa = placa
            vehiculo.tipo = tipo
            vehiculo.marca = marca
            vehiculo.modelo = modelo
            vehiculo.año = año
            vehiculo.color = color
            vehiculo.cilindrada = cilindrada
            
            db.session.commit()

            flash('Registro actualizado con exito')
            return redirect(url_for('vehiculo_router.vehiculos'))


vehiculocontroller = VehiculoController()