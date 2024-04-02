from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until((locator))
    return element