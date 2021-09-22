from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Station(db.Model):
    """Model for the stations table"""
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    comments = db.Column(db.Text())

    def __init__(self, customer, comments):
        self.customer = customer
        self.comments = comments


# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), unique=True)
#     password = db.Column(db.Text())
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
