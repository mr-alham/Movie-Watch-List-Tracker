#!/bin/env python3

from flask import Flask, jsonify, redirect, render_template,  request
from utils import load_from_form,load_movies, save_movies,  search
from subprocess import run

app = Flask(__name__)

# TODO add a filtering tag to filter movies by upcoming releases


@app.route("/")
def index():
    """index of the web page"""
    return render_template("index.html")


@app.route("/movies")
def movies() -> dict:
    """returns the list of movies as a json object"""
    movies = load_movies()
    return jsonify(movies)


@app.route("/update")
def update():
    """from function, we can update weather the listed movie is watched or downloaded from the main page"""
    args = request.args.to_dict()

    downloaded = True if "downloaded" in args else False
    watched = True if "watched" in args else False
    upcoming = True if "upcoming" in args else False

    movies = load_movies()
    for movie in movies:
        if movie["index"] == int(args["index"]):
            movie["downloaded"] = downloaded
            movie["watched"] = watched
            movie["upcoming"] = upcoming

    save_movies(movies)

    return redirect("/")


@app.route("/edit/<int:index>")
def edit(index):
    """shows the webpage to edit the specified movie"""
    movies = load_movies()

    for movie in movies:
        if movie["index"] == index:
            return render_template("edit.html", movies=movie)


@app.route("/edit/data/<int:index>")
def edit_data(index):
    """retrieve the edited movie from the web page and save it """
    updated_movie = load_from_form()
    movies = load_movies()

    for i, movie in enumerate(movies):
        if movie["index"] == index:
            movies[i] = updated_movie
            break
    save_movies(movies)

    return redirect("/")


@app.route("/add")
def add():
    """shows the web page to add a new movie"""
    return render_template("add.html")


@app.route("/add/data")
def add_data():
    """get new movies and save them"""

    new_movie = load_from_form()
    movies = load_movies()
    new_movie["index"] = 100 if len(
        movies) == 1 and movies[0]["movie"] == "-" else len(movies)+100

    movies.append(new_movie)
    save_movies(movies)

    return redirect("/add")


@app.route("/search", methods=["GET"])
def search_query():
    """shows the list of matching results on a individual web page"""
    global searched_movie_list
    query = request.args.get("query")
    searched_movie_list = search(query)  # dict of movie

    return render_template("search.html")


@app.route("/searched")
def searched_movies():
    return jsonify(searched_movie_list)


@app.route("/log_out", methods=["POST"])
def log_out():
    return render_template("log_out.html")


@app.route("/logout", methods=["POST"])
def logout():
    run(["sh", "script.sh", "&", ">/dev/null"])

    return "", 200


if __name__ == "__main__":
    app.run(debug=False, port=8000)
