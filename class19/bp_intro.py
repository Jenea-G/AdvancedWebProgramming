from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Test<h1>" #render on the browser


# a bigger app should be divided by responsibility!
#       to do this idea, we can use blueprints!

# A blueprint is a way to group related routes together!

#   main page in one bp
#   matches in another
#   players is another bp
#   etc..


# ==== !!! === common mistakes!

#   1. Never forget to register blueprint
#   2. dont mis @app.route and @blueprint.route
#   3. Dont forget the imports!
#   4. Blueprints are not separate applications!
#           BPs are sections of one app
#       