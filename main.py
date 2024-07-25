from dotenv import load_dotenv
from automation.data.user_data import UserData
from automation.tests.login import Login
from automation.tests.search_item import SearchItem
import os

load_dotenv()


def run_tests():
    user = UserData()
    login_url = os.getenv("LOGIN_URL")
    home_url = os.getenv("HOME_URL")

    if not login_url or not home_url:
        raise ValueError("LOGIN_URL or LOGIN_HOME not set in .env file")

    # Teste 01
    login_test = Login(user, login_url)
    try:
        login_test.test_case_01()
    except Exception as e:
        print(f"Test case 01 failed: {e}")
    else:
        print("Test case 01 completed successfully.")
    finally:
        login_test.close_browser()

    # Teste 02
    login_test = Login(user, login_url)
    try:
        login_test.test_case_02()
    except Exception as e:
        print(f"Test case 02 failed: {e}")
    else:
        print("Test case 02 completed successfully.")
    finally:
        login_test.close_browser()

    # Teste 03
    login_test = Login(user, login_url)
    try:
        login_test.test_case_03()
    except Exception as e:
        print(f"Test case 03 failed: {e}")
    else:
        print("Test case 03 completed successfully.")
    finally:
        login_test.close_browser()

    # Teste de Adicionar ao Carrinho
    search_test = SearchItem(user, home_url)
    try:
        search_test.test_case_search()
    except Exception as e:
        print(f"Test case search failed: {e}")
    else:
        print("Item buscado com sucesso.")
    finally:
        search_test.close_browser()  # Certifique-se de fechar o navegador após o teste


if __name__ == "__main__":
    run_tests()
