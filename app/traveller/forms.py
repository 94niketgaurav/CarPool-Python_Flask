from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, TextField, FieldList,DateTimeField
from wtforms import validators
from wtforms import widgets


class TravellerDirect(Form):
    name = StringField("Name of the Traveller", [validators.DataRequired("Please enter your name")])
    email = StringField("Email please", [validators.DataRequired("Email Required")])
    phone = StringField("Phone Number", [validators.DataRequired("Phone Required")])
    start_time = DateTimeField("Starting Time", [validators.DataRequired("Please Enter Starting Time")])
    start_location = StringField("Starting Location", [validators.DataRequired("Please Enter  Starting Location")])
    drop_location = StringField("Dropping Location", [validators.DataRequired("Please Enter Dropping Location")])


class TRSignup(Form):
    name = StringField("Name of the Traveller", [validators.DataRequired("Please enter your name")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])

    password = StringField("Password", [validators.DataRequired("Please enter Password")])
    sl = StringField("Starting Location", [validators.DataRequired("Please Enter Starting Loacation")])
    st = StringField("Starting Time", [validators.DataRequired("Please Enter  Starting Time")])
    dl = StringField("Drop Location", [validators.DataRequired("Please enter your drop Location")])

