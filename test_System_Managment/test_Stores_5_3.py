import time

from Project_Data.Login_func import *
def test_5_3_1():
    my_driver = login_web()
    tab_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_tab))
    tab_stores.click()
    time.sleep(1)
    btn_more_option_menu_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_more_option_menu_btn))
    btn_more_option_menu_stores.click()
    time.sleep(1)
    btn_add_store= WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(add_store_btn))
    btn_add_store.click()
    time.sleep(1)
    field_store_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_name_field))
    field_store_name.send_keys('שולי')
    time.sleep(1)
    field_store_phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_phone_field))
    field_store_phone.send_keys(Keys.CONTROL+'a')
    time.sleep(1)
    field_store_phone.send_keys('9721320207423')
    time.sleep(1)

    time.sleep(2)
    my_driver.close()
    my_driver.quit()