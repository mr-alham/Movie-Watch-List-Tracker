#!/bin/env python3
"""The "Movie Watch List Tracker" is a Python Flask based web application
 that allows users to track and manage their movie watchlists."""

from subprocess import run

from flask import Flask, jsonify, redirect, render_template, request  # import-error: false
from utils import load_from_form, load_movies, save_movies, search  # import-error: false

app = Flask(__name__)

# Future Development: add a button to delete added Movies


@app.route("/")
def index():
    """index of the web page"""
    return render_template("index.html")


@app.route("/movies")
def movies() -> dict:
    """returns the list of movies as a json object"""
    movies_movies = load_movies()
    num_of_movies = len(movies_movies)
    tmp_movies_list = []
    for num in range(num_of_movies):
        tmp_movies_list.append(movies_movies[num_of_movies - (num + 1)])

    return jsonify(tmp_movies_list)


@app.route("/update")
def update():
    """from function, we can update weather the listed movie
    is watched or downloaded from the main page"""
    args = request.args.to_dict()

    downloaded = "downloaded" in args
    watched = "watched" in args
    future_release = "future_release" in args

    update_movies = load_movies()
    for movie in update_movies:
        if movie["index"] == int(args["index"]):
            movie["downloaded"] = downloaded
            movie["watched"] = watched
            movie["future_release"] = future_release

    save_movies(update_movies)

    return redirect("/")


@app.route("/edit/<int:index>")
def edit(edit_index):
    """shows the webpage to edit the specified movie"""
    edit_movies = load_movies()

    for movie in edit_movies:
        if movie["index"] == edit_index:
            return render_template("edit.html", movies=movie)

    return render_template("index.html")  # if index dosen't exist will redirect to home page.

@app.route("/edit/data/<int:index>")
def edit_data(edit_data_index):
    """retrieve the edited movie from the web page and save it"""
    updated_movie = load_from_form()
    edit_data_movies = load_movies()

    for i, movie in enumerate(edit_data_movies):
        if movie["index"] == edit_data_index:
            edit_data_movies[i] = updated_movie
            break
    save_movies(edit_data_movies)

    return redirect("/")


@app.route("/add")
def add():
    """shows the web page to add a new movie"""
    return render_template("add.html")


@app.route("/add/data")
def add_data():
    """get new movies and save them"""

    new_movie = load_from_form()
    add_data_movies = load_movies()
    new_movie["index"] = (
        100 if len(add_data_movies) == 1 and add_data_movies[0]["movie"] == "-" else len(add_data_movies) + 100
    )

    add_data_movies.append(new_movie)
    save_movies(add_data_movies)

    return redirect("/add")


searched_movie_list = []


@app.route("/search", methods=["GET"])
def search_query():
    """shows the list of matching results on a individual web page"""
    # global searched_movie_list
    query = request.args.get("query")
    searched_movie_list = search(query)  # dict of movie

    return render_template("search.html")


@app.route("/searched")
def searched_movies():
    """handles the searching mechanism for the webpage"""
    return jsonify(searched_movie_list)


@app.route("/log_out", methods=["POST"])
def log_out():
    """shows the logged out banner on the web page"""
    return render_template("log_out.html")


@app.route("/logout", methods=["POST"])
def logout():
    """logOut in here log out means stopping the docker container via bash script"""
    run(["sh", "script.sh", "&", ">/dev/null"], check=True)

    return "", 200


@app.route("/health")
def health():
    """this route is used to check the health status of the Docker container"""

    return "Hola! My Love, I am still Alive.", 200


if __name__ == "__main__":
    app.run(debug=True, port=8000)
