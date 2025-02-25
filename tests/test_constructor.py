from locators import *
from wait_and_click import *
import time
import pytest

class TestConstructor:

    @pytest.mark.parametrize("start, menu_id, menu_item_text", [
        ('2', '3', 'Начинки'),
        ('3', '2', 'Соусы'),
        ('3', '1', 'Булки')])
    def test_check_menu_activation_and_scroll_success(self, driver_session, main_url, start, menu_id, menu_item_text):
        # Переход на главную страницу
        driver_session.get(main_url)
        time.sleep(3)
        WebDriverWait(driver_session, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        wait_and_click(driver_session, f"{xpath_of_menu}[{start}]")
        wait_for_class_to_appear(driver_session, f"{xpath_of_menu}[{start}]", "current")

        wait_and_click(driver_session, f"{xpath_of_menu}[{menu_id}]")
        wait_for_class_to_appear(driver_session, f"{xpath_of_menu}[{menu_id}]", "current")


        menu_item = driver_session.find_element(By.XPATH, f"{xpath_of_menu}[{menu_id}]")
        assert "current" in menu_item.get_attribute("class")

        h2_element = WebDriverWait(driver_session, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"{xpath_of_h2}[text()='{menu_item_text}']"))
        )

        driver_session.execute_script("arguments[0].scrollIntoView();", h2_element)
        assert h2_element.text == menu_item_text
