from locators import *
from wait_and_click import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestNavigate:

    # Переход по клику на «Личный кабинет».
    def test_navigate_click_button_lk_on_main_page_success(self, driver, login_url, main_url):
        driver.get(main_url)
        time.sleep(3)
        wait_and_click(driver, xpath_of_personal_page)
        wait_for_url(driver, login_url)
        assert driver.current_url == login_url

    # Переход по клику на «Конструктор»
    def test_navigate_from_login_page_click_button_constructor_success(self, driver, login_url, main_url):
        driver.get(login_url)
        time.sleep(3)
        wait_and_click(driver, xpath_constructor_button)
        wait_for_url(driver, main_url)
        assert driver.current_url == main_url

    # Переход по клику на логотип Stellar Burgers.
    def test_navigate_from_login_page_click_logo_success(self, driver, login_url, main_url):
        driver.get(login_url)
        time.sleep(3)
        wait_and_click(driver, xpath_logo_button)
        wait_for_url(driver, main_url)
        assert driver.current_url == main_url

    #Выход из аккаунта по кнопке "Выйти" в личном кабинете
    def test_navigate_from_login_page_click_button_logout_success(self, driver, login_url, main_url, profile_url, registration_data):
        driver.get(login_url)
        time.sleep(3)
        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])

        wait_and_click(driver, xpath_login_button)

        wait_for_url(driver, main_url)
        wait_and_click(driver, xpath_of_personal_page)

        wait_for_url(driver, profile_url)
        wait_and_click(driver, xpath_login_logout_button)

        wait_for_url(driver, login_url)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_login_button))
        )
