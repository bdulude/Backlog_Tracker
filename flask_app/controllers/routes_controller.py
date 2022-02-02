from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models import sighting

@app.route("/")
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route("/register")
def show_register():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template("register.html")

@app.route("/dashboard")
def success():
    if 'uuid' not in session:
        return redirect('/')
    # data = sighting.Sighting.get_all_with_users()
    # return render_template("dashboard.html", data = data)
    return render_template("dashboard.html")