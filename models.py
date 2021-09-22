import marshmallow.schema
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

import datetime

db = SQLAlchemy()
ma = Marshmallow()


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

# ------------------------------------------------------- #


# Product class/model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # autoinc by default
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    price = fields.Float()
    qty = fields.Integer()


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class UserOfProduct(db.Model):
    __tablename__ = 'user_of_product'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.Text())

    def __init__(self, username, password):
        self.username = username
        self.password = password
