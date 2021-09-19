from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# ENV = 'dev'
ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/heroku_flask_db'
elif ENV == 'prod':
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://skwmlusblqxfdx:92ab2cde87bc3198fd856ce7a543503d7be0c7411ac57c9b3029a6ccff9a5b0f@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d9q38bu4qri2s1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    comments = db.Column(db.Text())

    def __init__(self, customer, comments):
        self.customer = customer
        self.comments = comments


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.Text())

    def __init__(self, username, password):
        self.username = username
        self.password = password


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


@app.route('/')
def index_func():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
