import time
from pymongo import MongoClient
import pytest
from Driver_Startup import Driver_run
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data_connection import get_loginCode
from data_connection import create_mongo_connection
from data_connection import create_mongo_db

"data"
username = "qa_agency"
password = "!5szveK7$TE$93u"
database_name = "trado_qa"


"Locators"
input_selector = "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_phone div.phoneInput_phoneInputContainer:nth-child(2) div.react-tel-input > input.form-control"
submit_btn = "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn"
code_submit = "div.login_login div.login_panel form.form_form div.form_items div.form_formItem.undefined.undefined.formItem_code:nth-child(1) span.input_input:nth-child(2) div.input_relative > input:nth-child(1)"
login_button = "div.login_login div.login_panel span:nth-child(2) form.form_form > input.form_submitBtn"
trado_button = "div.login_login div.login_panel div.storesList_storesList:nth-child(2) div.storesList_list:nth-child(2) > div.storesList_store:nth-child(1)"

"mongodb stuff"
client = create_mongo_connection(username, password, database_name)
db = create_mongo_db(client, 'trado_qa')
collection = db['adminusers']


def test_logging_web():
    my_driver = Driver_run()
    my_driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")
    phone_input = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector)))
    phone_input.click()
    phone_input.send_keys("1234987655")
    submit_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, submit_btn)))
    submit_button.click()
    updated_login_code = get_loginCode(db, '9721234987655')
    code_input = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, code_submit)))
    code_input.send_keys(updated_login_code)
    submit_login_btn = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_button)))
    submit_login_btn.click()
    final_login = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, trado_button)))
    final_login.click()
    time.sleep(5)
    my_driver.quit()
