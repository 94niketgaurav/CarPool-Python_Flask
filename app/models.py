from app import db


class Users(db.Model):
    id = db.Column('owner_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)


class RegistrationDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer())
    start_location = db.Column(db.String(200))
    start_time = db.Column(db.DateTime())
    drop_location = db.Column(db.String(200))
    car_model = db.Column(db.String(100))
    car_number = db.Column(db.String(100))
    seats = db.Column(db.Integer())
    car_type = db.Column(db.String(50))

    def __init__(self, phone_number, start_location, start_time, drop_location, car_number,
                 car_model, seats, car_type):

        self.phone_number = phone_number
        self.start_location = start_location
        self.start_time = start_time
        self.drop_location = drop_location
        self.car_model = car_model
        self.car_number = car_number
        self.seats = seats
        self.car_type = car_type


# class TravellerSignup(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     password = db.Column(db.String(50))
#     start_location = db.Column(db.String(200))
#     start_time = db.Column(db.String(100))
#     drop_location = db.Column(db.String(200))
# 
#     def __init__(self, name, email, password, start_location, start_time, drop_location):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.start_location = start_location
#         self.start_time = start_time
#         self.drop_location = drop_location


class TravellerDirect(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer())
    start_time = db.Column(db.DateTime())

    def __init__(self, name, email, phone, start_time):
        self.name = name
        self.email = email
        self.phone = phone
        self.start_time = start_time
