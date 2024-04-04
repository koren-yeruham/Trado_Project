import time

from Project_Data.Login_func import *
from selenium.webdriver.support import expected_conditions as EC

def test_5_4_1():
    my_driver = login_web()
    users_tab_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_tab))
    users_tab_btn.click()
    users_kebab_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_kebab))
    users_kebab_btn.click()
    time.sleep(3)
    users_kebab_add_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_kebab_add))
    users_kebab_add_btn.click()
    users_kebab_add2_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_kebab_add2))
    users_kebab_add2_btn.click()
    users_add_phone_input = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_add_phone))
    users_add_phone_input.send_keys(Keys.CONTROL + "a")
    users_add_phone_input.send_keys("9721320207423")
    users_add_store_input = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_add_store))
    users_add_store_input.send_keys("test")
    users_add_store_dropdown_select = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_add_store_dropdown))
    users_add_store_dropdown_select.click()
    time.sleep(5)
    users_add_submit_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(users_add_submit))
    users_add_submit_btn.click()
    # assert
    time.sleep(5)
    my_driver.close()
    my_driver.quit()


