from flask import Blueprint, render_template

h = Blueprint('home', __name__, url_prefix='/home')


@h.route('/')
def home():
    print("In Home")
    return render_template('home.html')
