import time

from Project_Data.Driver_Startup import Driver_run


def test_opening_web():
    my_driver = Driver_run()
    my_driver.get("http://test-admin-env.eba-fnn924ys.eu-west-1.elasticbeanstalk.com/")
    time.sleep(5)