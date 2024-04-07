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
    field_store_phone.send_keys(Keys.CONTROL + 'a')
    field_store_phone.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    country_stores_add_store_field_phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_add_store_field_phone_country))
    country_stores_add_store_field_phone.click()
    time.sleep(1)
    IL_stores_add_store_field_phone_country = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_add_store_field_phone_country_IL))
    IL_stores_add_store_field_phone_country.click()
    time.sleep(2)
    field_store_phone.send_keys('1320207423')
    time.sleep(1)
    field_store_city = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_city_field))
    field_store_city.send_keys('רמת גן')
    time.sleep(1)
    field_street_city = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_street_field))
    field_street_city.send_keys('החילזון')
    time.sleep(1)
    field_building_city = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(store_building_field))
    field_building_city.send_keys('6')
    time.sleep(1)
    btn_stores_add_store = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(stores_add_store_btn))
    btn_stores_add_store.click()
    time.sleep(1)
    # bar_stores_search = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(stores_search_bar))
    # bar_stores_search.send_keys('שולי')
    # a = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(aa))
    # a_inner=a.get_attribute('innerText')
    time.sleep(2)
    # assert
    my_driver.close()
    my_driver.quit()

def test_5_3_3():
    my_driver = login_web()
    tab_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_tab))
    tab_stores.click()
    time.sleep(1)
    sign_stores_btn1_arrow = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_btn1_arrow_sign))
    sign_stores_btn1_arrow.click()
    time.sleep(1)
    sign_stores_btn2_arrow = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_btn2_arrow_sign))
    sign_stores_btn2_arrow.click()
    time.sleep(2)
    assert sign_stores_btn2_arrow.is_displayed()
    my_driver.close()
    my_driver.quit()

def test_5_3_4():
    my_driver = login_web()
    tab_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_tab))
    tab_stores.click()
    time.sleep(1)
    row_stores_specialty_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_row))
    row_stores_specialty_store.click()
    time.sleep(1)
    name_stores_specialty_store_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_field_name))
    name_stores_specialty_store_field.send_keys(Keys.CONTROL + 'a')
    time.sleep(1)
    name_stores_specialty_store_field.send_keys('כוכבה')
    time.sleep(1)
    btn_stores_update_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_update_store_btn))
    btn_stores_update_store.click()
    time.sleep(1)
    tab_store_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_name_tab))
    tab_store_name_inner = tab_store_name.get_attribute('innerText')
    assert tab_store_name_inner == 'כוכבה'
    time.sleep(2)
    my_driver.close()
    my_driver.quit()

def test_5_3_5():
    my_driver = login_web()
    tab_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_tab))
    tab_stores.click()
    time.sleep(1)
    row_stores_specialty_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_row))
    row_stores_specialty_store.click()
    time.sleep(1)
    phone_stores_specialty_store_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_field_phone))
    phone_stores_specialty_store_field.send_keys(Keys.CONTROL + 'a')
    phone_stores_specialty_store_field.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    country_stores_specialty_store_field_phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_field_phone_country))
    country_stores_specialty_store_field_phone.click()
    time.sleep(1)
    IL_stores_specialty_store_field_phone_country = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_field_phone_country_IL))
    IL_stores_specialty_store_field_phone_country.click()
    time.sleep(2)
    phone_stores_specialty_store_field.send_keys('1320207123')
    time.sleep(2)
    btn_stores_update_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_update_store_btn))
    btn_stores_update_store.click()
    time.sleep(1)
    tab_store_phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(store_phone_tab))
    tab_store_phone_inner = tab_store_phone.get_attribute('innerText')
    assert tab_store_phone_inner == '9721320207123'
    time.sleep(2)
    my_driver.close()
    my_driver.quit()

def test_5_3_6():
    my_driver = login_web()
    tab_stores = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_tab))
    tab_stores.click()
    time.sleep(1)
    row_stores_specialty_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(stores_specialty_store_row))
    row_stores_specialty_store.click()
    time.sleep(1)

    time.sleep(2)
    my_driver.close()
    my_driver.quit()