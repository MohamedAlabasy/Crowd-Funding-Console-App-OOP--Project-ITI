import os
import re


class Validation_Class:
    email_regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    phone_regex = r'^01[0125][0-9]{8}$'

    def name_validation(self, _name):
        if len(_name) > 3 and _name.isalpha():
            return True
        else:
            os.system("cls")
            return False

    def email_validation(self, _email):
        if len(_email) > 4 and re.fullmatch(self.email_regex, _email):
            return True
        else:
            os.system("cls")
            return False

    def password_validation(self, _password):
        if len(_password) > 3:
            return True
        else:
            os.system("cls")
            return False

    def confirm_password_validation(self, _password, _confirm_password):
        if _password == _confirm_password:
            return True
        else:
            os.system("cls")
            return False

    def phone_validation(self, _phone):
        if len(_phone) == 11 and re.fullmatch(self.phone_regex, _phone):
            return True
        else:
            os.system("cls")
            return False

    def login_validation(self, _email):
        if len(_email) > 3 and re.fullmatch(self.email_regex, _email):
            return True
        else:
            os.system("cls")
            return False
