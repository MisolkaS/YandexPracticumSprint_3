from locators import *
from wait_and_click import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAuth:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_click_button_enter_in_account_on_main_page_success(self, driver, main_url, registration_data):
        driver.get(main_url)
        time.sleep(3)
        wait_and_click(driver, xpath_enter_in_account_button)

        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])
        wait_and_click(driver, xpath_login_button)

        WebDriverWait(driver, 10).until(EC.url_to_be(main_url))
        assert driver.current_url == main_url

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_of_order_button))
        )

    # вход через кнопку «Личный кабинет» на главной
    def test_login_click_button_lk_on_main_page_success(self, driver, registration_data, main_url):
        driver.get(main_url)
        time.sleep(3)
        wait_and_click(driver, xpath_of_personal_page)

        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])

        wait_and_click(driver, xpath_login_button)

        wait_for_url(driver, main_url)
        assert driver.current_url == main_url
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_of_order_button))
        )

    # вход через ссылку войти в форме регистрации
    def test_login_click_link_enter_on_registration_page_success(self, driver, registration_url, main_url,
                                                                 registration_data):
        driver.get(registration_url)
        time.sleep(3)
        wait_and_click(driver, xpath_link_enter)

        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])

        wait_and_click(driver, xpath_login_button)
        wait_for_url(driver, main_url)

        assert driver.current_url == main_url
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_of_order_button))
        )

    # вход через кнопку в форме регистрации
    def test_login_click_button_lk_on_registration_page_success(self, driver, registration_url, main_url,
                                                                registration_data):
        driver.get(registration_url)
        time.sleep(3)
        wait_and_click(driver, xpath_of_personal_page)

        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])

        wait_and_click(driver, xpath_login_button)
        wait_for_url(driver, main_url)

        assert driver.current_url == main_url
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_of_order_button))
        )

    # вход через кнопку в форме восстановления пароля
    def test_login_click_link_enter_on_forgot_password_page_success(self, driver, forgot_password_url, main_url,
                                                                    registration_data):
        driver.get(forgot_password_url)
        time.sleep(3)
        wait_and_click(driver, xpath_of_personal_page)

        wait_and_send_keys(driver, xpath_email_login_input, registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, registration_data['password'])

        wait_and_click(driver, xpath_login_button)
        wait_for_url(driver, main_url)

        assert driver.current_url == main_url
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_of_order_button))
        )

