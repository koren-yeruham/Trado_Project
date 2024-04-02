import time

import pytest

from Project_Data.Driver_Startup import Driver_run
from data_connection import get_loginCode
from data_connection import create_mongo_connection
from data_connection import create_mongo_db
from Project_Data.Locators_and_DB_Info import *
from Project_Data.My_Actions import *


"mongodb connection"
client = create_mongo_connection(username, password, database_name)
db = create_mongo_db(client, 'trado_qa')
collection = db['adminusers']

def login_web():
    my_driver = Driver_run()
    my_driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")
    phone_input = find_element(my_driver, EC.presence_of_element_located(input_phone_field))
    phone_input.click()
    phone_input.send_keys("1234987655")
    submit_button = find_element(my_driver, EC.presence_of_element_located(submit_btn))
    submit_button.click()
    updated_login_code = get_loginCode(db, '9721234987655')
    code_input = find_element(my_driver, EC.presence_of_element_located(code_submit))
    code_input.send_keys(updated_login_code)
    time.sleep(3)
    submit_login_btn = find_element(my_driver, EC.presence_of_element_located((login_button)))
    submit_login_btn.click()
    final_login = find_element(my_driver, EC.presence_of_element_located((trado_button)))
    final_login.click()
    time.sleep(5)
    return my_driver

