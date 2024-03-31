import time

from Driver_Startup import Driver_run
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test_opening_web():
    my_driver = Driver_run()
    my_driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")
    time.sleep(5)