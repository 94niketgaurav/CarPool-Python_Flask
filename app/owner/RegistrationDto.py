class RegistrationDto:

    def __init__(self, phone_number="", start_location="", start_time="", drop_location="", car_model="", car_number="",
                 seats="", car_type=""):
        self.phone_number = phone_number
        self.start_location = start_location
        self.start_time = start_time
        self.drop_location = drop_location
        self.car_model = car_model
        self.car_number = car_number
        self.seats = seats
        self.car_type = car_type
