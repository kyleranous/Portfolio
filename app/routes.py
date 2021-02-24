from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Kyle" }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Testy'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Testy McTesterson'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
