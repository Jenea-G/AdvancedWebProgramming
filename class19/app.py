from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!<h1>" #render on the browser

@app.route("/greet")
def greet():
    # get arguments from the URL
    # such as /greet/?name=Joe
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1>"

@app.route("/about")
def about():
    return render_template("about.html", title="About me")

# the routes are our backend entry points!
# templates are redered by Flask!
# query parameters let the broweser send lightweight input!