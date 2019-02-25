import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
SECRET_KEY = 'NeverEverShareItToSomeOne'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hildermes:1234@0.0.0.0:32000/telemedicina'
