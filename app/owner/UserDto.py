class IllegalArgumentException(Exception):

    def __init__(self, *args, **kwargs):
        super(IllegalArgumentException, self).__init__(self, *args, **kwargs)


class UserDto:

    def __init__(self, email, password="", name=""):
        if not (email):
            # print("illegal arguments")
            raise IllegalArgumentException('email and password are required')
        self.name = name
        self.email = email
        self.password = password
