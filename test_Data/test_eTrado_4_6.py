import time

from Project_Data.Login_func import *
def test_4_6_1():
    my_driver = login_web()
    tab_etrado = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(etrado_tab))
    tab_etrado.click()
    time.sleep(3)
    more_option_menu_btn_etrado = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_more_option_menu_etrado))
    more_option_menu_btn_etrado.click()
    time.sleep(3)
    add_btn =  WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_add))
    add_btn.click()
    time.sleep(3)
    sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_sum))
    sum_btn.send_keys('300')
    time.sleep(3)
    next_sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_next_sum))
    next_sum_btn.click()
    next_details_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_next_details))
    next_details_btn.click()
    next_results_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_next_results))
    next_results_btn.click()
    add_etrado_payment_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_add_etrado_payment))
    add_etrado_payment_btn.click()

    # td_elements = (my_driver.find_elements(By.XPATH,'//tr/td'))
##need to change the for loop function
    # for td in td_elements:
    #     td_element = (my_driver.find_element(By.XPATH, '//tr/td/div'))
    #     td_element.click()
    #
    #
    #     sum_btn_300 = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_sum))
    #     sum_btn_inner_text = sum_btn_300.get_attribute('innerText')
    #
    #     if sum_btn_inner_text != '300':
    #         continue
    #     print("Sum button inner text is '300'")
    #     assert True

    my_driver.close()
    my_driver.quit()

def test_4_6_3():
    my_driver = login_web()
    tab_etrado = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(etrado_tab))
    tab_etrado.click()
    time.sleep(3)
    creation_date_etrado_text = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(text_creation_date_etrado))
    creation_date_etrado_text.click()
    time.sleep(3)
    sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_sum))
    sum_btn.send_keys(Keys.CONTROL + 'a')
    sum_btn.send_keys('4000')
    time.sleep(3)
    update_sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_update_sum))
    update_sum_btn.click()
    time.sleep(3)
    next_detail_etrado_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_next_detail_etrado))
    next_detail_etrado_btn.click()
    time.sleep(3)
    next_result_etrado_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_next_result_etrado))
    next_result_etrado_btn.click()
    time.sleep(3)
    update_etrado_payment_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_update_etrado_payment))
    update_etrado_payment_btn.click()
    time.sleep(3)
    etrado_sum_element = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(sum_element_etrado))
    etrado_sum_element_inner = etrado_sum_element.get_attribute("innerText")
    assert etrado_sum_element_inner == '₪4,000.00'

    my_driver.close()
    my_driver.quit()


def test_4_6_4():
    my_driver = login_web()
    tab_etrado = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(etrado_tab))
    tab_etrado.click()
    time.sleep(3)
    creation_date_etrado_text = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(text_creation_date_etrado))
    creation_date_etrado_text.click()
    time.sleep(3)
    next_etrado_sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btnn_next_etrado_sum))
    next_etrado_sum_btn.click()
    ID_etrado_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_ID_etrado))
    ID_etrado_btn.click()
    ID_etrado_btn.send_keys(Keys.CONTROL + 'a')
    ID_etrado_btn.send_keys('123456789')
    time.sleep(3)
    updat_id_etrado_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_updat_id_etrado))
    updat_id_etrado_btn.click()
    updat_id_etrado_payment_BTN = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_updat_id_etrado_payment))
    updat_id_etrado_payment_BTN.click()
    UPDATE_ID_ETRADO_RESULT_BTN = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(BTN_UPDATE_ID_ETRADO_RESULT))
    UPDATE_ID_ETRADO_RESULT_BTN.click()
    success_msg = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(success_msg_update))
    success_msg_inner = success_msg.get_attribute('innerText')
    assert success_msg_inner == 'etrado-payment updated successfully'

    my_driver.close()
    my_driver.quit()

def test_4_6_5():
    my_driver = login_web()
    tab_etrado = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(etrado_tab))
    tab_etrado.click()
    time.sleep(3)
    creation_date_etrado_text = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(text_creation_date_etrado))
    creation_date_etrado_text.click()
    time.sleep(3)
    next_etrado_sum_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btnn_next_etrado_sum))
    next_etrado_sum_btn.click()
    Payment_period = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Payment_period_element))
    Payment_period.send_keys(Keys.CONTROL + 'a')
    Payment_period.send_keys('25')
######
    updat_id_etrado_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_updat_id_etrado))
    updat_id_etrado_btn.click()
    updat_id_etrado_payment_BTN = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(btn_updat_id_etrado_payment))
    updat_id_etrado_payment_BTN.click()
    UPDATE_ID_ETRADO_RESULT_BTN = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(BTN_UPDATE_ID_ETRADO_RESULT))
    UPDATE_ID_ETRADO_RESULT_BTN.click()
    success_msg = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(success_msg_update))
    success_msg_inner = success_msg.get_attribute('innerText')
    assert success_msg_inner == '"etrado-payment updated successfully"'

    my_driver.close()
    my_driver.quit()



