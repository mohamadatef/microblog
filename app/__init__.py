from flask import Flask

app = Flask(__name__)
#app here is directory name name not module name 
app.config['SECRET_KEY']= "OIunsb7??=-0982+++s"
from app import routes

