from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.driver.web_driver import WebDriver
from automation.data.user_data import UserData


class SearchItem(WebDriver):
    def __init__(self, user: UserData, url: str):
        super().__init__(url)
        self.user = user

    def workflow(self):
        self.go_to(self.url)  # Navega para a URL fornecida

    def test_case_05(self):
        self.workflow()

        try:
            # Espera pela barra de pesquisa e insere o texto "echo pop"
            search_box = self.wait_until_element_visible(
                "id", "twotabsearchtextbox", 20
            )
            if search_box is None:
                raise Exception("Barra de pesquisa não encontrada.")
            search_box.send_keys("echo pop")
            search_box.submit()
            print("Busca realizada com sucesso.")
        except TimeoutException:
            raise Exception("Barra de pesquisa não encontrada.")
        except StaleElementReferenceException:
            raise Exception("Barra de pesquisa está desatualizada.")
