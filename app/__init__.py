__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

UPLOAD_FOLDER = 'app/static/uploads/'

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbtaller"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.principal_router import principal_router
app.register_blueprint(principal_router)

from app.routes.home_router import home_router
app.register_blueprint(home_router)


from app.routes.vehiculo_router import vehiculo_router
app.register_blueprint(vehiculo_router)

from app.routes.mecanico_router import mecanico_router
app.register_blueprint(mecanico_router)

from app.routes.historial_router import historial_router
app.register_blueprint(historial_router)

from app.routes.trabajo_router import trabajo_router
app.register_blueprint(trabajo_router)

from app.routes.verhistorial_router import verhistorial_router
app.register_blueprint(verhistorial_router)

from app.routes.vertrabajo_router import vertrabajo_router
app.register_blueprint(vertrabajo_router)