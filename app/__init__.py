import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.owner.views import own as owner
from app.traveller.views import traveller as traveller_rides
from app.home.views import h as home
from app.FinalBooking.bookings import final_book as finalbookings

db.create_all()

app.register_blueprint(owner)
app.register_blueprint(traveller_rides)
app.register_blueprint(home)
app.register_blueprint(finalbookings)


