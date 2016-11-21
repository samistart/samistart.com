from flask import Flask, render_template, Markup, redirect, url_for
import datetime
from models import Entry
from database import db
from models import DBSession

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def homepage():
    return redirect(url_for("blog"))


@app.route('/blog/')
def blog():
    session = DBSession()
    first_entry = session.query(Entry).first()
    return redirect(url_for('.article', slug=first_entry.slug))


@app.route('/blog/<path:slug>')
def article(slug):
    session = DBSession()
    raw_entries = session.query(Entry)
    entries = []
    for raw_entry in raw_entries:
        entry = {
            'title' : raw_entry.title,
            'slug' : raw_entry.slug
        }
        entries.append(entry)
    current_article = session.query(Entry).filter_by(slug=slug).first()
    current_article.timestamp = current_article.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("articles/" + current_article.slug + ".html", entries=entries, current_article=current_article)


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()
