import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
class DatabaseConfs:
   SECRET_KEY = SECRET_KEY
   DEBUG = DEBUG
   SQLALCHEMY_DATABASE_URI = 'postgresql://cerberus:Autodesk123!@localhost:5432/fyyur'
   # SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
   SQLALCHEMY_TRACK_MODIFICATIONS = False