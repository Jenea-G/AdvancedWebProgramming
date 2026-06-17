# What is templating?

# Flask uses Jinga template for rendering HTML, and you should note that Jinja
# autoescapes rendered user input in HTML by default.

# Why templates?

# Templates allow:
#   1. cleaner HTML files
#   2. dynamic placeholders
#   2. loops and conditionals
#   2. separation between Python logic and page structuere.

from flask import Flask, render_template, request #import render_template

app = Flask(__name__)

@app.route("/")
def home():
    # render_template tells flask to render an HTML template
    return render_template("home.html", title="welcome", message="hello from flask templates!")
# ^^^^^^^^ title and message are passed from Python into the template
# inside the HTML file {{ variable_name }}

@app.route("/games")
def games():
    games_list = ["Street fighter", "Tetris", "Pac-Man", "Fire and Water"]
    return render_template("games.html", games=games_list)

# ===============================
# looking at request data

@app.route("/greet")
def greet():
    # flask can read name from the request (.../greet?name=Jane)
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name} </h1>"

@app.route("/welcome")
def welcome():
    # two arguments: ../welcome?name=Jane&program=Web%20Development
    name = request.args.get("name", "Guest")
    program = request.args.get("program", "Unknown")
    return f"<h1>{name} studies in the {program} program.</h1>" # Jane studies in the Web Development program.