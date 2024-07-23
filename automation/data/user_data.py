import os
from dotenv import load_dotenv
load_dotenv()


class UserData:
    def __init__(self):
        self._correct_login = os.getenv("CORRECT_AMAZON_LOGIN")
        self._correct_password = os.getenv("correct_amazon_password")
        self._incorrect_login = os.getenv("INCORRECT_AMAZON_LOGIN")
        self._incorrect_password = os.getenv("INCORRECT_AMAZON_PASSWORD")

    def get_correct_login(self):
        return self._correct_login

    def get_correct_password(self):
        return self._correct_password

    def get_incorrect_login(self):
        return self._incorrect_login

    def get_incorrect_password(self):
        return self._incorrect_password
