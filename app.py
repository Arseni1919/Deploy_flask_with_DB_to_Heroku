from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from models import db, ma
from models import Feedback, Station, product_schema, products_schema, Product  # , User
import os

app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))

# ENV = 'dev'
ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/heroku_flask_db'
elif ENV == 'prod':
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://skwmlusblqxfdx:92ab2cde87bc3198fd856ce7a543503d7be0c7411ac57c9b3029a6ccff9a5b0f@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d9q38bu4qri2s1'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # complaining in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # stop from complaining in the console

# init db
db.init_app(app)
db.app = app
db.create_all(app=app)
# db = SQLAlchemy(app)

# init ma
ma.init_app(app)

# init migration
migrate = Migrate(app, db)

@app.route('/success')
def success_func():
    return render_template('success.html')


@app.route('/submit', methods=['POST'])
def submit_func():
    if request.method == 'POST':
        customer = request.form['customer']
        comments = request.form['comments']
        form_data = [customer, comments]
        if customer == '' or comments == '':
            return render_template('index.html', message='Please enter required fields...')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer=customer, comments=comments)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html', form_data=form_data)
        return render_template('index.html', message='You have already submitted feedback...')
    return render_template('index.html')


@app.route('/feedbacks')
def feedbacks_func():
    feedbacks = {}
    query = db.session.query(Feedback)
    for item in query:
        feedbacks[item.customer] = item.comments
    return render_template('feedbacks.html', feedbacks=feedbacks)


@app.route('/')
def index_func():
    return render_template('index.html')


# ------------------------------------------------------- #
# ----------------------CRUD API------------------------- #
# ------------------------------------------------------- #

@app.route('/product', methods=['POST', 'GET'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        qty = request.form['qty']

        new_product = Product(name=name, description=description, price=price, qty=qty)
        try:
            db.session.add(new_product)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return product_schema.dumps(new_product)
    if request.method == 'GET':
        all_products = Product.query.all()
        result = products_schema.dumps(all_products)
        return result

@app.route('/product/<id>')
def get_product(id):
    product = Product.query.get(id)
    result = product_schema.dumps(product)
    return result


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    qty = request.form['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    try:
        db.session.commit()
        return product_schema.dumps(product)
    except:
        db.session.rollback()
        raise


@app.route('/delete_product', methods=['POST'])
def delete_product_redirection():
    id = request.form['id']
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    result = product_schema.dumps(product)
    return result


@app.route('/product/<id>', methods=['POST'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    result = product_schema.dumps(product)
    return result
# ------------------------------------------------------- #


if __name__ == '__main__':
    app.run()
