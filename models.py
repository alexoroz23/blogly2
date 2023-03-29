"""SQLAlchemy models for blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Initialize SQLAlchemy object

# Default image URL for User instances
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """Site user."""

    __tablename__ = "users" # Table name in the database

    id = db.Column(db.Integer, primary_key=True) # Primary key column for User table
    first_name = db.Column(db.Text, nullable=False) # Column for user's first name
    last_name = db.Column(db.Text, nullable=False) # Column for user's last name
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL) # Column for user's profile image URL

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan") 
    # One-to-many relationship between User and Post models
    # backref creates a 'user' attribute on Post instances to access the related User instance
    # cascade="all, delete-orphan" specifies that when a User instance is deleted, its related Post instances should be deleted as well

    @property
    def full_name(self):
        """Return full name of user."""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "posts" # Table name in the database

    id = db.Column(db.Integer, primary_key=True) # Primary key column for Post table
    title = db.Column(db.String(50), nullable=False) # Column for post title
    content = db.Column(db.String(250), nullable=False) # Column for post content
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now) # Column for post creation time
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # Foreign key column referencing User table's primary key

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)