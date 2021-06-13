import os
import time
from app import db
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models.Historial import Historial

from PIL import Image #pip install pillow
import urllib.request
from werkzeug.utils import secure_filename

class HistorialController():

    def __init__(self):
        pass

    def index(self):
        historiales = Historial.query.all()
        return render_template('historiales/index.html', title='Historial', historiales=historiales)
    def crearHistorial(self):
        return render_template('historiales/create.html', title='Nuevo Historial')

    
    
    """ ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS """
    def guardarHistorial(self):
        if request.method == 'POST':
            titulo = request.form['titulo']
            descripcion = request.form['descripcion']

            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file: #and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #guardar nombre
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                fecha = time.strftime("%Y%m%d%H%M%S")
                imgPath = app.config['UPLOAD_FOLDER'] + filename
                img = Image.open(imgPath)
                img.save('app/static/uploads/'+fecha+'.png')
                os.remove('app/static/uploads/'+filename)
                newfilename = fecha+'.png'

                historial = Historial(titulo=titulo, descripcion=descripcion, urlimage=newfilename)
                db.session.add(historial)
                db.session.commit()

                flash('Historial creado exitosamente')
                return redirect(url_for('historial_router.main'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)
historialcontroller = HistorialController()
