from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models import user

@app.route("/register/add", methods=["POST"])
def add_user():
    is_valid = user.User.regi_validation(request.form)
    if not is_valid:
        return redirect('/')
    
    hash_pwd = bcrypt.generate_password_hash(request.form['pwd'])
    data = {
        **request.form,
        'pwd' : hash_pwd
    }
    id = user.User.save(data)
    flash("Account Created. Please log in.", "regi_success")
    return redirect('/')

@app.route("/login", methods=["POST"])
def login():
    # print(request.form)
    is_valid = user.User.login_validation(request.form)
    if not is_valid:
        return redirect("/")
    user_inst = user.User.get_one_by_email(request.form)
    if not user_inst:
        return redirect("/")
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
