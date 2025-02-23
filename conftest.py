import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"])
def driver_session(request):
    if request.param == "chrome":
        driver_session = webdriver.Chrome()
    elif request.param == "firefox":
        driver_session = webdriver.Firefox()
    yield driver_session
    driver_session.quit()

@pytest.fixture()
def menu_item():
   menu_item = ['Соусы', 'Начинки', 'Булки']
   return menu_item

@pytest.fixture()
def registration_url():
    return "https://stellarburgers.nomoreparties.site/register"

@pytest.fixture()
def main_url():
    return "https://stellarburgers.nomoreparties.site/"

@pytest.fixture()
def login_url():
    return "https://stellarburgers.nomoreparties.site/login"

@pytest.fixture()
def forgot_password_url():
    return "https://stellarburgers.nomoreparties.site/forgot-password"

@pytest.fixture()
def profile_url():
    return "https://stellarburgers.nomoreparties.site/account/profile"

@pytest.fixture()
def registration_data():
    registration_data = {
        "name": "Misolka",
        "email": "alina_sitalova_16_025@yandex.ru",
        "password": "neowick"
    }
    return registration_data

@pytest.fixture()
def invalid_registration_data():
    registration_data = {
        "name": "Misolka",
        "email": "alina_sitalova_16_025@yandex.ru",
        "password": "sss"
    }
    return registration_data






