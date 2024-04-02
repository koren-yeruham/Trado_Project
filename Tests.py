
from Project_Data.Login_func import *


def test_6_1_1():
    pass

def test_1_1_1():
    my_driver = login_web()
    orders_btn = find_element(my_driver, EC.presence_of_element_located(dashboard_orders_btn))
    orders_btn.click()
    assert my_driver.current_url == "http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/#/orders"
    time.sleep(5)
    my_driver.close()
    my_driver.quit()
