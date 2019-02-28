# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
#api to bind mysql, python and flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
import time
#User password encryption
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import logging
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
#instanciating Bcrypt as bcrypt
bcrypt = Bcrypt(app)
#instanciating Login_manager as login_manager
login_manager = LoginManager()
login_manager.init_app(app)
#from config file chose some class configuration
#I will chose dev, I want to debug, never use it in production mode
app.config.from_object(os.environ['APP_SETTINGS'])
app.logger.setLevel(logging.NOTSET)
db = SQLAlchemy(app)
#We have to import models before creating the database
#this points to url_for(login)
login_manager.login_view = 'login'

from .models import tm_siteuser

@login_manager.user_loader
def load_user(user_id):
    return tm_siteuser.query.filter(tm_siteuser.id == int(user_id)).first()
