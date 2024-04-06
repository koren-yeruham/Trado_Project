import time

from Project_Data.Login_func import *
def test_1_5_5():
    my_driver = login_web()
    tab_orders = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(orders_tab))
    tab_orders.click()
    time.sleep(3)
    arrow_sign_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_arrow_sign))
    arrow_sign_btn.click()
    time.sleep(3)
    arrow_sign_btn2 = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn2_arrow_sign))
    arrow_sign_btn2.click()
    time.sleep(5)
    assert arrow_sign_btn2.is_displayed()
    my_driver.close()
    my_driver.quit()
