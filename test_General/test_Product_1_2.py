import time

from Project_Data.Login_func import *

# from Project_Data.Locators_and_DB_Info import *
# from Project_Data.Login_func import login_web
# from Project_Data.My_Actions import find_element
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time


"test start and end"
# def test_1_2_3():
#     my_driver = login_web()
#     time.sleep(5)
#     my_driver.close()
#     my_driver.quit()




def test_1_2_1():
    my_driver = login_web()
    tab_product = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_tab))
    tab_product.click()
    time.sleep(3)
    kebab_products = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_kebab))
    kebab_products.click()
    add_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_user))
    add_btn.click()
    add_MKT_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_MKT))
    add_MKT_field.send_keys("7290000284316")
    add_name_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_name))
    add_name_field.send_keys("בקבוק קולה")
    add_price_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_price))
    add_price_field.send_keys("10")
    add_next_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_submit_btn))
    add_next_btn.click()
    add_supercategory = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_supercategory))
    add_supercategory.send_keys("משקאות")
    add_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_store))
    add_store.send_keys("שופרסלטסטטטטטטט")
    add_country = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_country))
    add_country.send_keys("Israel")
    add_country.send_keys(Keys.ENTER)
    add_submit2 = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_add_submit_btn2))
    add_submit2.click()
    time.sleep(2)
    add_submit2.click()
    time.sleep(2)
    add_submit2.click()
    time.sleep(2)
    add_submit2.click()
    time.sleep(5)
    my_driver.close()
    my_driver.quit()



def test_1_2_3():
    my_driver = login_web()
    tab_product = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_tab))
    tab_product.click()
    time.sleep(3)
    first_item = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(products_1st_tab))
    first_item.click()
    time.sleep(5)
    my_driver.close()
    my_driver.quit()