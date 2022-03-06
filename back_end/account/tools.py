import re

class Tools():
    def CheckUserData(self, username, email, password):

        ## Username
        if len(username) < 5 or len(username) > 30:
            return "Username must have between 5 and 30 characters."

        ## Email
        if not re.match("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
            return "Invalid email"
        if len(email) > 60:
            return "email must have less then 60 characters."

        ## Password
        if not re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$", password):
            return "Password must have between 8 and 32 characters, contain lower case letters, capital letters and numbers."

        return ""