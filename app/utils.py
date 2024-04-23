from json import dump, load, JSONDecodeError
from re import compile, IGNORECASE, findall
from os.path import exists
from flask import request

data_file = 'data/movies.json'
if not exists(data_file):
    with open(data_file, 'w'):
        pass


def save_movies(movies: list):
    '''saves the movie dict on the json file'''

    for i, movie in enumerate(movies):
        if movie["movie"] == '-':
            movies.pop(i)

    movies = {"movies": movies}

    with open(data_file, 'w') as file:
        dump(movies, file, indent=1)


def load_movies() -> list[dict]:
    '''loads saved movies on the file to the memory'''
    try:
        with open(data_file, 'r') as file:
            movies = load(file)
        return movies["movies"]

    except JSONDecodeError:
        return [{"movie": '-',
                 "year": '-',
                 "series": False,
                 "downloaded": False,
                 "watched": False}]

    except FileNotFoundError:
        print('the JSON file not found')
        return 500

    except Exception as e:
        print(e)
        return 500


def load_from_form() -> dict:
    '''extracts the data from the web form and send the extracted data as a dict'''

    args = request.args.to_dict()
    index = True if 'index' in args else False
    movie = args.get('movie_name')
    year = args.get('year')
    series = True if 'tv_series' in args else False
    watched = True if 'watched' in args else False
    downloaded = True if 'downloaded' in args else False
    upcoming = True if 'upcoming' in args else False
    upcoming_notes = args.get(
        'upcoming_notes') if 'upcoming_notes' in args else False

    if index:
        index = int(args['index'])
    else:
        index = 100

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
    '''handles the search '''
    movies = load_movies()
    pattern = compile(query, IGNORECASE)
    year_query = findall(r'\b\d{4}\b', query)
    re_matches = []
    year_matches = []
    match_list = []
    movie_list = []

    for movie in movies:
        if pattern.search(movie['movie']):
            re_matches.append(movie['index'])
        elif movie['year'] in year_query:
            year_matches.append(movie['index'])

    for i, index in enumerate(re_matches):
        if index in year_matches:
            match_list.append(index)
            re_matches.pop(i)

    match_list.extend(re_matches)

    for year in year_matches:
        if year not in match_list:
            match_list.append(year)

    for movie in movies:
        if movie['index'] in match_list:
            movie_list.append(movie)

    movie_list = movie_list[::-1]

    return movie_list
