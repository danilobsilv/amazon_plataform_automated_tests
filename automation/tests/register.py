import os
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData


class Register(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user

    def workflow(self):
        self.go_to(self.url)  # Navega para a URL fornecida

    def test_case_04(self):
        self.workflow()
        try:
            name_field = self.wait_until_element_visible("id", "ap_customer_name", 20)
            if name_field is None:
                raise Exception("Campo de name retornou None.")
            name_field.send_keys(self.user.get_register_name())
            print("Nome inserido com sucesso.")
            
        except TimeoutException:
            raise Exception("Campo de nome não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de nome está desatualizado.")

        try:
            email_field = self.wait_until_element_visible("id", "ap_email", 20)
            if email_field is None:
                raise Exception("Campo de email retornou None.")
            email_field.send_keys(self.user.get_register_name())
            print("Email inserido com sucesso.")
        except TimeoutException:
            raise Exception("Campo de email não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Campo de email está desatualizado.")

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
            sign_up_button = self.wait_until_element_visible("id", "continue", 20)
            if sign_up_button is None:
                raise Exception("Botão de criar conta retornou None.")
            sign_up_button.click()
            print("Botão de criar conta clicado com sucesso.")
        except TimeoutException:
            raise Exception("Botão de criar conta não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão de criar conta está desatualizado.")
        
        try:
            error_message = self.wait_until_element_visible(
                "id", "auth-error-message-box", 20
            )
            if error_message is None:
                raise Exception("Mensagem de erro retornou None.")
            print("Mensagem de erro para todos os campos devem ser preenchidos encontrada com sucesso.")
        except TimeoutException:
            raise Exception("Mensagem de erro não encontrada.")
        except StaleElementReferenceException:
            raise Exception("Mensagem de erro está desatualizada.")

    def close_browser(self):
        self.web_driver.quit()

