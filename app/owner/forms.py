from flask_wtf import Form
from wtforms import Form as WTForm
from wtforms import StringField, IntegerField, BooleanField, TextField, PasswordField, DateTimeField
from wtforms import validators
from wtforms import widgets


class Login(Form):
    email = StringField("Email", [validators.DataRequired("Please Enter Your Email")])
    password = PasswordField("Password", [validators.DataRequired("Please Enter Your Password")])
    remember_me = BooleanField("Remember Me", default=False)


class SignupForm(Form):
    name = StringField("Name Of Owner", [validators.DataRequired("Please Enter Your Name.")])
    email = StringField("Email", [validators.DataRequired("Please Enter Your Email Address."),
                                  validators.Email("Please Enter Your Email Address.")])
    password = PasswordField("Password", [validators.DataRequired("Please Enter Password")])

class RegistrationDetails(Form):
    phone_number = StringField("Phone Number", [validators.DataRequired("Please Enter Phone Number")])
    start_location = StringField("Starting Location", [validators.DataRequired("Please Enter Starting Location")])
    start_time = DateTimeField("Starting Time", [validators.DataRequired("Please Enter  Starting Time")])
    drop_location = StringField("Drop Location", [validators.DataRequired("Please Enter your drop Location")])
    car_model = StringField("Car Model", [validators.DataRequired("Please Enter Car Model")])
    car_number = StringField("Car Number", [validators.DataRequired("Please Enter Car Number")])
    seats = IntegerField("Seats", [validators.DataRequired("Please Enter Your Drop Location")])
    car_type = StringField("Ac/Non Ac Type", [validators.DataRequired("Please Enter Type")])
