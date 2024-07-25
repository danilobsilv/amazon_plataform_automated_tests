from dotenv import load_dotenv
from automation.data.user_data import UserData
from automation.tests.login import Login
import os

load_dotenv()


def run_tests():
    user = UserData()
    login_url = os.getenv("LOGIN_URL")

    if not login_url:
        raise ValueError("LOGIN_URL not set in .env file")

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
        print("Test case 03 completed sucesso.")
    finally:
        login_test.close_browser()


if __name__ == "__main__":
    run_tests()
