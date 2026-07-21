# 1 Create the Flask application and database.
import os
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, UserMixin, login_user, logout_user, current_user, login_required)

from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///shelf.db")

# the secret key from an envrionment variable.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# db
db.init_app(app)

# login
login_manager = LoginManager()      # Create the login manager
login_manager.login_view = "login"  # Redirect unauthenticated users to /login
login_manager.init_app(app)         # Attach manager to the app