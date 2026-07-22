# 1 Create the Flask application and database.
import os
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, UserMixin, login_user, logout_user, current_user, login_required)

from models import db, User, Book, ReadingStatus

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

with app.app_context():
    db.create_all()

# load user
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# Registeration Validation
def validate_password(password):

    if len(password) < 8:
        return("Password must contain at least 8 characters.")
    if len(password) > 20:
        return("Password must contain at most 20 characters.") 
    if not any(character.isupper() for character in password):
        return("Password must contain at least one uppercase letter.")
    if not any(character.isdigit() for character in password):
        return("Password must contain a digit.")
    
    return None

# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        errors = []

        if not username:
            errors.append("Username is required")
        if len(username) > 50:
            errors.append("Username may contain at most 50 characters.") 
        if any(character.isspace() for character in username):
            errors.append("Username may not contain whitespace")

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            errors.append("This username is already in use!")

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            errors.append("This email is already registered.")

        password_error = validate_password(password)
        if password_error:
            errors.append(password_error)

        if errors:
            for error in errors:
                flash(error, "error")

            return render_template("register.html", username=username, email=email)
        
        # no errors
        user = User(username=username, email=email)

        # hash the password
        user.set_password(password)

        # add it to the table
        db.session.add(user)
        db.session.commit()

        flash("Your account has been created!", "success")

        return redirect(url_for("login"))
        # return redirect(url_for("home")) #to check if /registration works
    
    return render_template("register.html")

# implement login
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("books")) # return to books if already logged in
    
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        # username or passwrod error
        if user is None or not user.check_password(password):
            flash("Invalid username or password", "error")

            return render_template("login.html", username=username)
        
        # when no errors
        login_user(user)

        flash("You are now logged in.", "success")

        return redirect(url_for("books"))
    
    return render_template("login.html")

# implement logout
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    flash("You have been logged out.", "success")
    return redirect(url_for("home"))

# Books route
@app.route("/books", methods=["GET"])
@login_required
def books():
    user = User.query.get_or_404(current_user.id)
    books = user.reading_list
    return render_template("books.html", books=books)

# adding a book
@app.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():
    errors = []

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form["note"].strip()
        status_value = request.form["status"].strip()

        if not Book.valid_string(title):
            errors.append("Title is required and should be at most 100 characters long.")

        if not Book.valid_string(author):
            errors.append("Author is required and should be at most 100 characters long.")

        if len(note) > 1000:
            errors.append("The note length shouldn't exceed 1000 characters.")

        try:
            status = ReadingStatus(status_value)
        except ValueError:
            errors.append("Reading status is invalid.")

        if errors:
                for error in errors:
                    flash(error, "error")

                return render_template("book_form.html", title=title, author=author, note=note, selected_status=status_value)
    
        # create book if no errors
        book = Book(
            book_title = title,
            book_author = author,
            note = note,
            reading_status = status,
            user_id = current_user.id
        )

        # add it to the table
        db.session.add(book)
        db.session.commit()

        flash("Your book has successfully been added to the reading list", "success")

        return redirect(url_for("books"))
    
    return render_template("book_form.html")
        
# editing a book
@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.id).first_or_404() #to get only this user book

    errors = []

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form["note"].strip()
        status_value = request.form["status"].strip()

        if not Book.valid_string(title):
            errors.append("Title is required and should be at most 100 characters long.")

        if not Book.valid_string(author):
            errors.append("Author is required and should be at most 100 characters long.")

        if len(note) > 1000:
            errors.append("The note length shouldn't exceed 1000 characters.")

        try:
            status = ReadingStatus(status_value)
        except ValueError:
            errors.append("Reading status is invalid.")

        if errors:
                for error in errors:
                    flash(error, "error")

                return render_template("book_edit.html", book=book)
    
        # update book if no errors
        
        book.book_title = title
        book.book_author = author
        book.note = note
        book.reading_status = status   

        # add changes to the db
        db.session.commit()

        flash("Your book was successfully updated", "success")

        return redirect(url_for("books"))
    
    return render_template("book_edit.html", book=book)