from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:ah44220206@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pawfyrwyfozdaf:162db5f7717a8734e6746dd9863d426d22a3b9f303962e759346586f007d79e9@ec2-52-72-125-94.compute-1.amazonaws.com:5432/dclb7p9ngjoab5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#connexion = psycopg2.connect(dbname = "quotes", user = "postgres", password = "ah@@4422", host = "127.0.0.1")

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result = result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form["author"]
    quote = request.form["quote"]
    quotedata = Favquotes(author = author, quote = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
