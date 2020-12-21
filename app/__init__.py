from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
admin = Admin(app)

#set up a login manager 
login = LoginManager()
login.init_app(app)

from app import routes, models, errors