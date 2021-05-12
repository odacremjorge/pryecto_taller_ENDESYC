__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask('app')

app = Flask(__name__, template_folder="views")

#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbtaller"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

from app.routes.home_router import home_router
app.register_blueprint(home_router)

from app.routes.vehiculo_router import vehiculo_router
app.register_blueprint(vehiculo_router)

from app.routes.mecanico_router import mecanico_router
app.register_blueprint(mecanico_router)