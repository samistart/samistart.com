from flask import Flask, render_template, redirect
import datetime
from models import Entry
from database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


@app.route('/')
@app.route('/blog/')
def blog():
    entry = Entry(title='title', slug='slug', content='content', published=True, timestamp=datetime.datetime.now())
    print(entry.title)
    entries = ["london", "paris", "berlin"]
    return render_template("blog.html", entries=entries)


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()
