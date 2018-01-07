from flask import Flask

app = Flask(__name__)
#app here is foldder name not module name 
from app import routes

