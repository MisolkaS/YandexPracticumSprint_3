from locators import *
from generate_data import *
from wait_and_click import *

class TestRegisration:
    #успешная регистрация

    def test_registration_success(self, driver, registration_url, login_url):
        driver.get(registration_url)
        time.sleep(3)
        user_data = generate_random_user_data()
        wait_and_send_keys(driver, xpath_name_input, user_data['name'])
        wait_and_send_keys(driver, xpath_email_input, user_data['email'])
        wait_and_send_keys(driver, xpath_password_input, user_data['password'])
        wait_and_click(driver, xpath_register_button)
        WebDriverWait(driver, 10).until(EC.url_changes(registration_url))

        assert driver.current_url == login_url


    def test_invalid_password_error(self, driver, login_url, invalid_registration_data):
        driver.get(login_url)
        time.sleep(3)
        wait_and_send_keys(driver, xpath_email_login_input, invalid_registration_data['email'])
        wait_and_send_keys(driver, xpath_password_login_input, invalid_registration_data['password'])
        wait_and_click(driver, xpath_login_button)
        assert WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, xpath_password_error)))






