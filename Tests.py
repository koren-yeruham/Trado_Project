
from Logging_into_admin_user import *
from Project_Data.Driver_Startup import Driver_run
import pytest

def test_6_1_1(test_logging_web):
    pass

def test_1_1_1():
    my_driver = login_web()
    orders_btn = find_element(my_driver,EC.presence_of_element_located(dashboard_orders_btn))
    orders_btn.click()

    time.sleep(5)
    my_driver.close()
    my_driver.quit()
