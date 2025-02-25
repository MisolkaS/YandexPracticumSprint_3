from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def wait_and_send_keys(driver, xpath, keys, timeout=20):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.send_keys(keys)

def wait_for_url(driver, url, timeout=20):
    if driver.capabilities['browserName'] == 'firefox':
        time.sleep(3)
    WebDriverWait(driver, timeout).until(EC.url_to_be(url))

def wait_and_click(driver, xpath, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()

def wait_for_class_to_appear(driver, xpath, class_name, timeout=20):
    WebDriverWait(driver, timeout).until(
        lambda d: class_name in d.find_element(By.XPATH, xpath).get_attribute("class")
    )
