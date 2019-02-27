# -*- coding: utf-8 -*-
import os

# This should be default config
class BaseConfig(object):
    DEBUG = False
    # shortened for readability, try # https://randomkeygen.com/
    #or try import os, it has a function urandom(), you could try os.urandom(24)
    SECRET_KEY = 'NeverEverShareItToSomeOne'
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hildermes:1234@0.0.0.0:32000/telemedicina'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
#test config eirs base attributes change some, and add others.
class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

#Dev config eirs base attributes change some, and add others.
class DevelopmentConfig(BaseConfig):
    DEBUG = True

#Production config eirs base attributes, change some, and add others.
class ProductionConfig(BaseConfig):
    DEBUG = False

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/



