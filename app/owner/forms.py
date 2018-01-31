from flask_wtf import Form
from wtforms import Form as WTForm
from wtforms import StringField, IntegerField, BooleanField, TextField, PasswordField, DateTimeField
from wtforms import validators
from wtforms import widgets


class Login(Form):
    email = StringField("Email", [validators.DataRequired("Please enter your Email")])
    password = PasswordField("Password", [validators.DataRequired("Please enter your Password")])
    remember_me = BooleanField('remember_me', default=False)


class signupForm(Form):
    name = StringField("Name Of Owner", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                                  validators.Email("Please enter your email address.")])
    password = PasswordField("Password", [validators.DataRequired("Please enter Password")])


class service(Form):
    phone_number = StringField("Phone Number", [validators.DataRequired("Please Enter Phone Number")])
    start_location = StringField("Starting Location", [validators.DataRequired("Please Enter Starting Location")])
    start_time = DateTimeField("Starting Time", [validators.DataRequired("Please Enter  Starting Time")])
    drop_location = StringField("Drop Location", [validators.DataRequired("Please enter your drop Location")])
    car_model = StringField("Car Model", [validators.DataRequired("Please Enter Car Model")])
    car_number = StringField("Car Number", [validators.DataRequired("Please Enter Car Number")])
    seats = IntegerField("Seats", [validators.DataRequired("Please enter your drop Location")])
    type = StringField("Ac/Non Ac Type", [validators.DataRequired("Please Enter Type")])
