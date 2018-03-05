"""
This file initializes your application and brings together all of the various components.
"""
import logging
import os

from flask import Flask
from flask_bcrypt import Bcrypt
from login import login_manager
from flask_security import SQLAlchemyUserDatastore, Security

from app.blueprints.auth.views import auth_blueprint
from app.common import config
from app.data.relations import db
from app.data.role import Role
from app.data.user import User
from app.log.log import setup_logging
from blueprints.admin.views import admin
from blueprints.main.views import main

# Logging
setup_logging()

# app
app = Flask(__name__,
            instance_relative_config=True)  # instance_relative_config implies loading config from instance folder

# Configuration
config_name = os.getenv('FLASK_CONFIGURATION', 'default')
app.config.from_object(config[config_name])
# Load the configuration from the instance folder
app.config.from_pyfile('config.py', silent=True)

# Blueprints
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Database
db.init_app(app)

# Security
bcrypt = Bcrypt(app)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)


# Login Manager
login_manager.init_app(app)
