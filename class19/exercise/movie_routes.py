from flask import Blueprint, render_template, request

movies = Blueprint("movies", __name__)

MOVIES = [
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    {"title": "Spirited Away", "genre": "Animation", "year": 2001},
    {"title": "Whiplash", "genre": "Drama", "year": 2014},
    {"title": "Parasite", "genre": "Thriller", "year": 2019}
]

@movies.route("/movies")
def movies_list():
    return render_template("movies.html", movies=MOVIES)

@movies.route("/movie")
def movie_detail():
    movie_title = request.args.get("title", "Unknown Movie")
    return render_template("movie.html", movie_title = movie_title)

@movies.route("/search")
def search():
    genre = request.args.get("genre", "")

    if genre:
        filtered = []

        for movie in MOVIES:
            if movie["genre"] == genre:
                filtered.append(movie)

    else:
        filtered = MOVIES

    return render_template("search.html", movies = filtered, genre = genre)