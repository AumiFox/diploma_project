import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    """Фикстура для инициализации браузера перед каждым тестом"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-notifications")

    chrome_driver_path = r"C:\Users\кристина\PycharmProjects\pythonProjectSelenium\chromedriver.exe"

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://b2c.passport.rt.ru"


@pytest.fixture(scope="session")
def test_account():
    return {
        "phone": "+79522741743",
        "email": "test.test098@inbox.ru",
        "password": "Qwer1234"
    }

@pytest.fixture(scope="session")
def account_login():
    return "rtkid_1779311779273"

@pytest.fixture(scope="session")
def account_phone(test_account):
    return test_account["phone"]


@pytest.fixture(scope="session")
def account_email(test_account):
    return test_account["email"]


@pytest.fixture(scope="session")
def valid_password(test_account):
    return test_account["password"]


@pytest.fixture(scope="function")
def new_user_data():
    import random
    import string
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return {
        "first_name": "Тест",
        "last_name": "Тестов",
        "phone": f"+7999{random.randint(1000000, 9999999)}",
        "email": f"{random_str}@test.ru",
        "password": "Qwerty123",
        "region": "Москва"
    }