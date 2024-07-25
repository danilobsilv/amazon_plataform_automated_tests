import os
from dotenv import load_dotenv

load_dotenv()


class UserData:
    def __init__(self):
        self._correct_login = os.getenv("CORRECT_AMAZON_LOGIN")
        self._correct_password = os.getenv("CORRECT_AMAZON_PASSWORD")
        self._incorrect_login = os.getenv("INCORRECT_AMAZON_LOGIN")
        self._incorrect_password = os.getenv("INCORRECT_AMAZON_PASSWORD")
        self._register_name = os.getenv("REGISTER_NAME")
        self._register_email = os.getenv("REGISTER_EMAIL")
        self._register_password = os.getenv("REGISTER_PASSWORD")

    def get_correct_login(self):
        return self._correct_login

    def get_correct_password(self):
        return self._correct_password

    def get_incorrect_login(self):
        return self._incorrect_login

    def get_incorrect_password(self):
        return self._incorrect_password
    
    def get_register_name(self):
        return self._register_name
    
    def get_register_email(self):
        return self._register_email
    
    def get_register_password(self):
        return self._register_password
