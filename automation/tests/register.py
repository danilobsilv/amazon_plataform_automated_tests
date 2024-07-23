import os

from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData


class Register(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user
        self.url = url

    def test_case_03(self):
        self.type_text("id", "ap_customer_name", os.getenv("FULL_NAME"))
        self.type_text("id", "ap_email", os.getenv("PHONE_NUMBER"))
        self.type_text("id", "ap_password", os.getenv("INCORRECT_AMAZON_PASSWORD"))
        self.type_text("id", "ap_password_check", os.getenv("INCORRECT_AMAZON_PASSWORD"))
        self.find_by("id", "continue").click()

    def test_case_04(self, index):
        action_flow = [
            lambda: self.type_text("id", "ap_customer_name", os.getenv("FULL_NAME")),
            lambda: self.type_text("id", "ap_email", os.getenv("PHONE_NUMBER")),
            lambda: self.type_text("id", "ap_password", os.getenv("INCORRECT_AMAZON_PASSWORD")),
            lambda: self.type_text("id", "ap_password_check", os.getenv("INCORRECT_AMAZON_PASSWORD")),
            lambda: self.find_by("id", "continue").click()
        ]

        if 0 <= index < len(action_flow):
            action_flow.pop(index)
        else:
            raise IndexError("Index out of range")

        for action in action_flow:
            action()


