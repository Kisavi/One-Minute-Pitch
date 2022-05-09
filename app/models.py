from . import db
from flask_login import UserMixin  # this will check for four authentication properties in a user
from sqlalchemy.sql import func


# Model Class for User
# Model Class for Categories
# Model Class for Pitch
# Model Class for Votes
# Model Class for Comments

class User(db.Model, UserMixin):
    """
    this User class helps us create new users
    args: db.model which helps us connect our class to the db
    """
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')


# class Category(db.Model):
#     """
#     this Category class helps us create new Pitch from a user
#     args: db.model which helps us connect our class to the db
#     """
#     pass


class Pitch(db.Model):
    """
    this Pitch class helps us create new Pitch from a user
    args: db.model which helps us connect our class to the db
    """

    __table_name__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy='dynamic')
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


class UpVote(db.Model):
    """
    this Votes class helps us update the votes for a pitch
    args: db.model which helps us connect our class to the db
    """
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=0)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


class DownVote(db.Model):
    """
    this Votes class helps us update the votes for a pitch
    args: db.model which helps us connect our class to the db
    """
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=0)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    """
    this Comment class helps us create a new comment a user submits
    args: db.model which helps us connect our class to the db
    """

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
