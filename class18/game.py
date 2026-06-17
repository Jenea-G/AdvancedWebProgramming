from flask import Flask

app = Flask(__name__)

# we want an app with 3 routes
#       /
#       /games
#           return unordered list with 3 game names.
#       /students
# each route should return different HTML content.

@app.route("/")
def home():
    return "<h1>Home page for Game App</h1>"

@app.route("/games")
def games():
    return "<h1>Games List</h1>" \
    "<ul>" \
    "<li>Ticket to ride</li>" \
    "<li>Catan</li>" \
    "<li>Cacao</li>" \
    "</ul"

@app.route("/students")
def students():
    return "<h1>Students List</h1>" \
    "<ul>" \
    "<li>Ann</li>" \
    "<li>Bob</li>" \
    "<li>Cathy</li>" \
    "</ul"