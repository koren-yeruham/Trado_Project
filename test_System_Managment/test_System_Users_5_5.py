import time

from Project_Data.Login_func import *
from selenium.webdriver.support import expected_conditions as EC


def test_5_5_1():
    my_driver = login_web()
    tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
    tab_system.click()
    search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
    search_bar.send_keys("שלנווווו")
    system_user_row = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_1st_row))
    system_user_row.click()
    input_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_firstname))
    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys("סתוית")
    submit_systemuser = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_submit))
    submit_systemuser.click()
    time.sleep(3)
    system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_name_tab))
    system_user_row_inner = system_user_row_assert.get_attribute("innerText")
    assert system_user_row_inner == "סתוית"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()


def test_5_5_2():
    my_driver = login_web()
    tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
    tab_system.click()
    search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
    search_bar.send_keys("שלנווווו")
    system_user_row = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_1st_row))
    system_user_row.click()
    input_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_lastname))
    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys("לוי")
    submit_systemuser = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_submit))
    submit_systemuser.click()
    time.sleep(3)
    system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_lastname_tab))
    system_user_row_inner = system_user_row_assert.get_attribute("innerText")
    assert system_user_row_inner == "לוי"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()


def test_5_5_3():
    my_driver = login_web()
    tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
    tab_system.click()
    search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
    search_bar.send_keys("שלנווווו")
    system_user_row = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_1st_row))
    system_user_row.click()
    input_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_email))
    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys("jogog92125@artgulin.co.il")
    submit_systemuser = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_submit))
    submit_systemuser.click()
    time.sleep(3)
    system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_email_tab))
    system_user_row_inner = system_user_row_assert.get_attribute("innerText")
    assert system_user_row_inner == "jogog92125@artgulin.co.il"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()


# def test_5_5_4():
#     pass

def test_5_5_5():
    my_driver = login_web()
    tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
    tab_system.click()
    search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
    search_bar.send_keys("שלנווווו")
    system_user_row = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_1st_row))
    system_user_row.click()
    input_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_store))
    input_field.send_keys(Keys.CONTROL + "a")
    input_field.send_keys("שופרסלטסטטטטטטט")
    input_field_1st_opt = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_store_1st))
    input_field_1st_opt.click()
    submit_systemuser = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_submit))
    submit_systemuser.click()
    time.sleep(3)
    system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_stores_tab))
    system_user_row_inner = system_user_row_assert.get_attribute("innerText")
    assert system_user_row_inner == "Tradoשופרסלטסטטטטטטט"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()


# def test_5_5_6():
#     my_driver = login_web()
#     tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
#     tab_system.click()
#     system_user_kebab_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_kebab))
#     system_user_kebab_btn.click()
#     system_user_add = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_add_btn))
#     system_user_add.click()
#     input_field_first_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_firstname))
#     input_field_first_name.send_keys("אריקה")
#     input_field_last_name = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_lastname))
#     input_field_last_name.send_keys("אלופה")
#     input_field_email = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_email))
#     input_field_email.send_keys("jogog92125@artgulin.co.il")
#     input_field_phone = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_phone))
#     input_field_phone.send_keys("1234567899")
#     input_field_store = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_store))
#     input_field_store.send_keys("שופרסלטסטטטטטטט")
#     store_1st_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_store_1st))
#     store_1st_btn.click()
#     submit_systemuser = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_submit))
#     submit_systemuser.click()
#     time.sleep(5)
#     search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
#     search_bar.send_keys("אריקה")
#     time.sleep(3)
#     system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_name_tab))
#     system_user_row_inner = system_user_row_assert.get_attribute("innerText")
#     assert system_user_row_inner == "אריקה"
#     time.sleep(5)
#     my_driver.close()
#     my_driver.quit()


def test_5_5_8():
    my_driver = login_web()
    tab_system = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_tab))
    tab_system.click()
    search_bar = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(searchbarsystem))
    search_bar.send_keys("סתוית")
    system_user_row_assert = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(system_user_name_tab))
    system_user_row_inner = system_user_row_assert.get_attribute("innerText")
    assert system_user_row_inner == "סתוית"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()