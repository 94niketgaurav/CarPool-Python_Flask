class IllegalArgumentException(Exception):

    def __init__(self, *args, **kwargs):
        super(IllegalArgumentException, self).__init__(self, *args, **kwargs)


class TravellerDto:

    def __init__(self, name="", email="", phone="", start_time=""):
        if not (email):
            # print("Illegal Arguments")
            raise IllegalArgumentException('email and password are required')
        self.name = name
        self.email = email
        self.phone = phone
        self.start_time = start_time
