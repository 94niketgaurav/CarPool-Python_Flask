from flask_wtf import Form
from wtforms import StringField
from wtforms import validators


class BookingForm(Form):
    name = StringField("Name Of Owner", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])
