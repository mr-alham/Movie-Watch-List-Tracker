"""This module provides reusable functions for app.py"""

from json import JSONDecodeError, dump, load
from os.path import exists
from re import IGNORECASE
from re import compile as recompile
from re import findall

from flask import request  # pylint: disable=import-error

DATA_FILE = "data/movies.json"

if not exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8"):
        pass


def save_movies(movies: list):
    """saves the movie dict on the json file"""

    for i, movie in enumerate(movies):
        if movie["movie"] == "-":
            movies.pop(i)

    to_save_movies = {"movies": movies}  # type: ignore

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        dump(to_save_movies, file, indent=1)


def load_movies() -> list[dict]:
    """loads saved movies on the file to the memory"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            movies = load(file)
        return movies["movies"]

    except JSONDecodeError:
        return [
            {
                "movie": "-",
                "year": "-",
                "series": False,
                "downloaded": False,
                "watched": False,
            }
        ]

    except FileNotFoundError:
        print("the JSON file not found")
        return 500  # type: ignore

    except Exception as e:  # pylint: disable=W0718
        print(e)
        return 500  # type: ignore


def load_from_form() -> dict:
    """extracts the data from the web form and send the extracted data as a dict"""

    args = request.args.to_dict()
    movie = args.get("movie_name")
    year = args.get("year")
    index_bool = "index" in args
    series = "tv_series" in args
    watched = "watched" in args
    upcoming = "upcoming" in args
    downloaded = "downloaded" in args
    upcoming_notes = args.get("upcoming_notes") if "upcoming_notes" in args else False

    if index_bool:
        index = int(args["index"])  # type: int
    else:
        index = 100  # type: ignore

    add_new_movie = {
        "index": index,
        "movie": movie,
        "year": year,
        "series": series,
        "watched": watched,
        "downloaded": downloaded,
        "upcoming": upcoming,
        "upcoming_notes": upcoming_notes,
    }

    return add_new_movie


def search(query: str) -> list:
    """handles the search"""
    movies = load_movies()
    pattern = recompile(query, IGNORECASE)
    year_query = findall(r"\b\d{4}\b", query)
    re_matches = []
    year_matches = []
    match_list = []
    movie_list = []

    for movie in movies:
        if pattern.search(movie["movie"]):
            re_matches.append(movie["index"])
        elif movie["year"] in year_query:
            year_matches.append(movie["index"])

    for i, index in enumerate(re_matches):
        if index in year_matches:
            match_list.append(index)
            re_matches.pop(i)

    match_list.extend(re_matches)

    for year in year_matches:
        if year not in match_list:
            match_list.append(year)

    for movie in movies:
        if movie["index"] in match_list:
            movie_list.append(movie)

    movie_list = movie_list[::-1]

    return movie_list
