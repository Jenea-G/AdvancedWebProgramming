from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (check_password_hash, generate_password_hash)
from enum import Enum

# starting db
db = SQLAlchemy()

# create User model
class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    
    password_hash = db.Column(db.String(255), nullable=False)

    # ========
    #  creating relationship
    reading_list = db.relationship(
        "Book",
        back_populates="user" #refers to Book.user
    )
    # =========
    
    # methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def add_book(self, book):     
        self.reading_list.append(book) # relationship collection, we have to get a book object

    # log
    def __repr__(self):
        return(f"<User {self.id}: {self.username}>")
    
   
# create the Book model and relationship.
class ReadingStatus(Enum):
    WANT_TO_READ = "Want to read"
    READING = "Reading"
    FINISHED = "Finished"
class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)

    book_title = db.Column(db.String(100), nullable=False)
    book_author = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(1000), nullable=True)
    reading_status = db.Column(db.Enum(ReadingStatus), nullable=False, default=ReadingStatus.WANT_TO_READ)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"), #uses the tablename.id (not Python class name)
        nullable=False
    )

    user = db.relationship(
        "User",
        back_populates="reading_list" #refers to the attribute on User.reading_list
    )

    @staticmethod
    def valid_string(value):
        if (0 < len(value) <= 100): return True
        return False

    def __repr__(self):
        return (
            f"<Book {self.id}: {self.book_title} by {self.book_author}>"
        )