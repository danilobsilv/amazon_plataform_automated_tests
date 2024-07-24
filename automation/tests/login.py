from dotenv import load_dotenv
from selenium.common import TimeoutException

from automation.data.user_data import UserData
from automation.driver.web_driver import WebDriver

load_dotenv()


class Login(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user
        self.url = url

    def workflow(self):
        pass

    # if this script goes to the 2FA page, then it worked
    def test_case_01(self):

        self.type_text("id", "ap_email", self.user.get_correct_login())

        self.find_by("id", "continue").click()

        try:
            expected_password_field = self.wait_until_element_visible("id", "ap_password", 15)
            expected_password_field.send_keys(self.user.get_correct_password())
        except TimeoutException:
            raise Exception("Field not found.")

        self.find_by("id", "signInSubmit").click()

    def test_case_02_1(self):

        self.type_text("id", "ap_email", self.user.get_incorrect_login())

        self.find_by("id", "continue").click()

    def test_case_02_2(self):

        self.type_text("id", "ap_email", self.user.get_correct_login())

        self.find_by("id", "continue").click()

        try:
            expected_password_field = self.wait_until_element_visible("id", "ap_password", 15)
            expected_password_field.send_keys(self.user.get_incorrect_password())
        except TimeoutException:
            raise Exception("Field not found.")

        self.find_by("id", "signInSubmit").click()
