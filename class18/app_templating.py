# What is templating?

# Flask uses Jinga template for rendering HTML, and you should note that Jinja
# autoescapes rendered user input in HTML by default.

# Why templates?

# Templates allow:
#   1. cleaner HTML files
#   2. dynamic placeholders
#   2. loops and conditionals
#   2. separation between Python logic and page structuere.

from flask import Flask, render_template #import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="welcome", message="hello from flask templates!")