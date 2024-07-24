import time
from selenium import webdriver
from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class WebDriver(ABC):

    def __init__(self, url, options: ChromeOptions = None):

        self.options = options if options else self.personal_options()
        self.web_driver = webdriver.Chrome(options=self.options)
        self.url = url
        self.__BY_DICT = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'tag_name': By.TAG_NAME,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }

    @abstractmethod
    def workflow(self):
        pass

    @staticmethod
    def personal_options():
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--incognito")
        return options

    def clear_cache(self):
        self.find_by("xpath", "//settings-ui").send_keys(Keys.ENTER)

    def go_to(self, specific_url=None):
        if specific_url is not None:
            self.web_driver.get(specific_url)

        self.web_driver.get(self.url)

    def press_forward(self):
        self.web_driver.forward()

    def press_back(self):
        self.web_driver.back()

    def refresh_page(self):
        self.web_driver.refresh()

    def find_by(self, by: str, value: str):

        by_dict = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'tag_name': By.TAG_NAME,
            'class_name': By.CLASS_NAME,
            'css_selector': By.CSS_SELECTOR
        }
        if by not in self.__BY_DICT:
            raise ValueError(f"'{by}' locator is not supported.")
        return self.web_driver.find_element(by_dict[by], value)

    def type_text(self, field_type: str, field_location: str, text: str):

        type_list = ["id", "name", "xpath", "tag_name", "class_name", "css_selector"]

        if field_type.lower() not in type_list:
            raise ValueError("Unexisting field")

        field = self.find_by(field_type, field_location)
        field.send_keys(text)

    def wait_until_element_visible(self, by: str, value: str, timeout: int = 10):

        if by not in self.__BY_DICT:
            raise ValueError(f"'{by}' locator is not supported.")

        wait = WebDriverWait(self.web_driver, timeout)
        element = wait.until(EC.visibility_of_element_located((self.__BY_DICT[by], value)))
        return element

    @staticmethod
    def wait(seconds: int):
        time.sleep(seconds)
