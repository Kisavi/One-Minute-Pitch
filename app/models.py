from . import db
from flask_login import UserMixin  # this will check for four authentication properties in a user
from sqlalchemy.sql import func


# Model Class for User
# Model Class for Categories
# Model Class for Pitch
# Model Class for Votes
# Model Class for Comments

class User(db.model, UserMixin):
    """
    this User class helps us create new users
    args: db.model which helps us connect our class to the db
    """
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    pitches = db.relationship('Pitch')


class Pitch(db.model):
    """
    this Pitch class helps us create new Pitch from a user
    args: db.model which helps us connect our class to the db
    """

    __table_name__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
