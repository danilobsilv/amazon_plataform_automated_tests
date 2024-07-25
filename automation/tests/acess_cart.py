from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData


class AcessCart(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user

    def workflow(self):
        self.go_to(self.url)  # Navega para a URL fornecida

    def test_case_06(self):
        self.workflow()

        try:
            # Clica no ícone do carrinho de compras
            cart_icon = self.wait_until_element_visible("id", "nav-cart", 20)
            if cart_icon is None:
                raise Exception("Ícone do carrinho de compras não encontrado.")
            cart_icon.click()
            print("Ícone do carrinho de compras clicado com sucesso.")
        except TimeoutException:
            raise Exception("Ícone do carrinho de compras não encontrado.")
        except StaleElementReferenceException:
            raise Exception("Ícone do carrinho de compras está desatualizado.")
