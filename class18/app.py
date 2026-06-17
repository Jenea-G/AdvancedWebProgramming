 
# the browser displays the interface
# the backend receives requests
# the backend decides what data or page to send back
# the backend may validate input, apply business rules, talk to a database, render templates, and return a response.

# Important: never name your file flask.py to avoid conflicts.

from flask import Flask

app = Flask(__name__)

# this decorator tells Flask what URL should trigger the function.
@app.route("/")
def hello():
    return "<h1>Hello, Flask!</h1>" #returns the response sent to the browser.

@app.route("/about")
def about():
    return "<h1>About</h1> <p>This is the about page for Jane</p>"

# Request-response cycle:

#   1. Browser requests a URL
#   2. Flask receives the request
#   3. Flask matches a route
#   4. Python function runs
#   5. response is returned.



# What is templating?

# Flask uses Jinga template for rendering HTML, and you should note that Jinja
# autoescapes rendered user input in HTML by default.

# Why templates?

# Templates allow:
#   1. cleaner HTML files
#   2. dynamic placeholders
#   2. loops and conditionals
#   2. separation between Python logic and page structuere.

