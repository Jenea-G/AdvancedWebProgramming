from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (check_password_hash, generate_password_hash)

# starting db
db = SQLAlchemy()