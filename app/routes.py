#ffrom app floder import app application __init__
from flask import render_template
from app import app
@app.route("/")
@app.route("/index")
def index():
    data  = {'username' : "Mohamad Radwan"}
    return render_template('index.html', user  = data ,title = "Home Page")


