from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData


class CartClick(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user

    def workflow(self):
        self.go_to(self.url)  # Navega para a URL fornecida

    def test_case_click(self):
        self.workflow()

        try:
            # Espera pelo botão do carrinho
            cart_button = self.wait_until_element_visible(
                "id", "nav-cart", 20
            )
            if cart_button is None:
                raise Exception("Botão de Carrinho não encontrado.")
            cart_button.click()
            print("Carrinho clicado com sucesso.")
        except TimeoutException:
            raise Exception("Botão de Carrinho não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Botão de Carrinho está desatualizado.")