from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from models import db, Feedback
import os

app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))

ENV = 'dev'
# ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/heroku_flask_db'
elif ENV == 'prod':
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://skwmlusblqxfdx:92ab2cde87bc3198fd856ce7a543503d7be0c7411ac57c9b3029a6ccff9a5b0f@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d9q38bu4qri2s1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # complaining in the console
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # stop from complaining in the console

# init db
db.init_app(app)
db.app = app

# init ma
ma = Marshmallow(app)

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


if __name__ == '__main__':
    app.run()
