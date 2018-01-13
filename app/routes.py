#from app floder import app application __init__
from flask import render_template, flash , redirect, url_for

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
@app.route("/login", methods = ["POST", "GET"])

#----------------------------------#
#Start Login Route Here
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash("Login requestd")
    
        return redirect(url_for("index"))

    return render_template("login.html", form = form)
