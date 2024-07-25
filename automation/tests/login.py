from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData
import os


class Login(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user

    def workflow(self):
        self.go_to(self.url)  # Navega para a URL fornecida

    def test_case_01(self):
        self.workflow()
        try:
            email_field = self.wait_until_element_visible("id", "ap_email", 20)
            if email_field is None:
                raise Exception("Campo de email retornou None.")
            email_field.send_keys(self.user.get_correct_login())
            print("Email inserido com sucesso.")
        except TimeoutException:
            raise Exception("Campo de email não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de email está desatualizado.")

        try:
            continue_button = self.wait_until_element_visible("id", "continue", 20)
            if continue_button is None:
                raise Exception("Botão continuar retornou None.")
            continue_button.click()
            print("Botão continuar clicado com sucesso.")
        except TimeoutException:
            raise Exception("Botão continuar não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão continuar está desatualizado.")

        try:
            password_field = self.wait_until_element_visible("id", "ap_password", 20)
            if password_field is None:
                raise Exception("Campo de senha retornou None.")
            password_field.send_keys(self.user.get_correct_password())
            print("Senha inserida com sucesso.")
        except TimeoutException:
            raise Exception("Campo de senha não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de senha está desatualizado.")

        try:
            sign_in_button = self.wait_until_element_visible("id", "signInSubmit", 20)
            if sign_in_button is None:
                raise Exception("Botão de login retornou None.")
            sign_in_button.click()
            print("Botão de login clicado com sucesso.")
        except TimeoutException:
            raise Exception("Botão de login não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão de login está desatualizado.")

    def test_case_02(self):
        self.workflow()
        try:
            email_field = self.wait_until_element_visible("id", "ap_email", 20)
            if email_field is None:
                raise Exception("Campo de email retornou None.")
            email_field.send_keys(self.user.get_incorrect_login())
            print("Email não cadastrado inserido com sucesso.")
        except TimeoutException:
            raise Exception("Campo de email não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de email está desatualizado.")

        try:
            continue_button = self.wait_until_element_visible("id", "continue", 20)
            if continue_button is None:
                raise Exception("Botão continuar retornou None.")
            continue_button.click()
            print("Botão continuar clicado com sucesso.")
        except TimeoutException:
            raise Exception("Botão continuar não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão continuar está desatualizado.")

        try:
            error_message = self.wait_until_element_visible(
                "xpath", "//div[contains(@class, 'a-alert-content')]", 20
            )
            if error_message is None:
                raise Exception("Mensagem de erro retornou None.")
            print("Mensagem de erro para e-mail não cadastrado exibida com sucesso.")
        except TimeoutException:
            raise Exception("Mensagem de erro não encontrada.")
        except StaleElementReferenceException:
            raise Exception("Mensagem de erro está desatualizada.")

    def test_case_03(self):
        self.workflow()
        try:
            email_field = self.wait_until_element_visible("id", "ap_email", 20)
            if email_field is None:
                raise Exception("Campo de email retornou None.")
            email_field.send_keys(self.user.get_correct_login())
            print("Email inserido com sucesso para teste com senha incorreta.")
        except TimeoutException:
            raise Exception("Campo de email não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de email está desatualizado.")

        try:
            continue_button = self.wait_until_element_visible("id", "continue", 20)
            if continue_button is None:
                raise Exception("Botão continuar retornou None.")
            continue_button.click()
            print("Botão continuar clicado com sucesso para teste com senha incorreta.")
        except TimeoutException:
            raise Exception("Botão continuar não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão continuar está desatualizado.")

        try:
            password_field = self.wait_until_element_visible("id", "ap_password", 20)
            if password_field is None:
                raise Exception("Campo de senha retornou None.")
            password_field.send_keys(os.getenv("INCORRECT_AMAZON_PASSWORD"))
            print("Senha incorreta inserida com sucesso.")
        except TimeoutException:
            raise Exception("Campo de senha não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de senha está desatualizado.")

        try:
            sign_in_button = self.wait_until_element_visible("id", "signInSubmit", 20)
            if sign_in_button is None:
                raise Exception("Botão de login retornou None.")
            sign_in_button.click()
            print("Botão de login clicado com sucesso para teste com senha incorreta.")
        except TimeoutException:
            raise Exception("Botão de login não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão de login está desatualizado.")

    def close_browser(self):
        self.web_driver.quit()
