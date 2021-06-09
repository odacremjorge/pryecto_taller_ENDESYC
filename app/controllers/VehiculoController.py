from app import db
from flask import render_template, request, redirect, url_for, flash
from app.models.Vehiculo import Vehiculo

class VehiculoController():
    def __init__(self):
        pass

    def index(self):
        vehiculos = Vehiculo.query.all()
        return render_template('vehiculos/index.html', tittle='Vehiculos', vehiculos=vehiculos)
    
    def crearVehiculo(self):
        return render_template('vehiculos/create.html', title='Nuevo vehiculo')
    def guardarVehiculo(self):
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

            
            vehiculo = Vehiculo(cia = cia, empresa = empresa, placa = placa, tipo = tipo, marca = marca, modelo = modelo, año = año, color = color, cilindrada = cilindrada)
            db.session.add(vehiculo)
            db.session.commit()

            flash('Registro exitoso')
            return redirect(url_for('vehiculo_router.principal'))

    def eliminarVehiculo(self, _id):
        
        vehiculo = Vehiculo.query.get(_id)
        db.session.delete(vehiculo)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('vehiculo_router.principal'))

    def editarVehiculo(self, _id):
        
        vehiculo = Vehiculo.query.get(_id)
        return render_template('vehiculos/edit.html', title='Editar', vehiculo = vehiculo)

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
            return redirect(url_for('vehiculo_router.principal'))


vehiculocontroller = VehiculoController()