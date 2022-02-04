from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import movie, user
import requests, json, html


@app.route('/search/movie')
def searchMovie():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('search_movie.html')


@app.route('/new/movie')
def new():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('new_movie.html')

@app.route('/get/movie', methods=['POST'])
def getMovie():
    if 'uuid' not in session:
        return redirect('/')

    url = "https://betterimdbot.herokuapp.com/"
    data = {
        **request.form
    }
    payload = data['searchQuery']
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    json_load = json.loads(response.text)
    response_Arr = []

    for item in json_load:
        response_Arr.append(item)

    if len(response_Arr) == 2:
        return redirect('/dashboard')

    output = {
        'link' : response_Arr[1]['tt_url'],
        # 'title' : html.unescape(response_Arr[1]['jsonnnob']['name']),
        'title' : html.unescape(response_Arr[1]['title']),
        # 'synopsis' : html.unescape(response_Arr[1]['jsonnnob']['description']),
        'synopsis' : html.unescape(response_Arr[1]['short_imdb_description']),
        # 'synopsis' : html.unescape(response_Arr[1]['summary']['plot']),
        'rating' : response_Arr[1]['UserRating']['rating'],
        'image' : response_Arr[1]['small_poster']
    }

    return render_template("new_movie.html", response = output)


@app.route('/create/movie', methods=['POST'])
def create():
    if 'uuid' not in session:
        return redirect('/')
    is_valid = movie.Movie.validate(request.form)
    if not is_valid:
        return redirect('/new/movie')
    data = {
        **request.form,
        'user_id' : session['uuid']
    }
    print("*************")
    print(data)
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