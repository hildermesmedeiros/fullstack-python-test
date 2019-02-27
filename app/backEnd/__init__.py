# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
import time
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#from config file chose some class configuration
#I will chose dev, I want to debug, never use it in production mode
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
#We have to import models before creating the database
from .models import tm_siteuser

