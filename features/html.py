from flask import Blueprint, render_template

html = Blueprint('html', __name__)


@html.route('/')
def login():
    return render_template('login.html')


@html.route('/register')
def register():
    return render_template('register.html')
