#ffrom app floder import app application __init__
from flask import render_template
from app import app
from app.form import LoginForm
@app.route("/")
@app.route("/index")
def index():
    data  = {'username' : "Mohamad Radwan"}
    return render_template('index.html', user  = data ,title = "Home Page")
@app.route("/user")
def user():
    return render_template("user.html", title = "User page Title", user = "Radwan")
@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form = form)
