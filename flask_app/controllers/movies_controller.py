from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import movie, user

@app.route('/new/movie')
def new():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('new_movie.html')

@app.route('/create/movie', methods=['POST'])
def create():
    if 'uuid' not in session:
        return redirect('/')
    is_valid = movie.Movie.validate(request.form)
    if not is_valid:
        return redirect('/new/movie')
    data = {
        **request.form,
        'userid' : session['uuid']
    }
    id = movie.Movie.save(data)
    return redirect('/dashboard')

@app.route('/edit/movie/<int:id>')
def edit(id):
    if 'uuid' not in session:
        return redirect('/')
    data = movie.Movie.get_one({'id' : id})
    if data.user_id != session['uuid']:
        return redirect('/dashboard')
    return render_template('update_movie.html', movie = data)

@app.route('/update/movie/<int:id>', methods=["POST"])
def update(id):
    if 'uuid' not in session:
        return redirect('/')
    is_valid = movie.Movie.validate(request.form)
    if not is_valid:
        return redirect('/edit/movie/' + str(id))
    data = {
        **request.form,
        'id' : id
    }
    movie.Movie.update(data)
    return redirect('/dashboard')

@app.route('/delete/movie/<int:id>')
def delete(id):
    if 'uuid' not in session:
        return redirect('/')
    movie.Movie.delete({ 'id' : id})
    return redirect('/dashboard')


@app.route('/show/movie/<int:id>')
def show(id):
    if 'uuid' not in session:
        return redirect('/')
    show_movie = movie.Movie.get_one({'id' : id})
    reporter = user.User.get_one_by_id({ 'id' : show_movie.user_id})
    show_movie.full_name = reporter.first_name + " " + reporter.last_name
    return render_template('show_movie.html', movie = show_movie)