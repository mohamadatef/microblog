from flask import Flask

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app here is directory name name not module name 
app.config['SECRET_KEY']= "OIunsb7??=-0982+++s"
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
from app import routes

