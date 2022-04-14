import time
from urllib import request

import pytest
from selenium import webdriver
firefox97_cap={"browserName": "firefox",
        "browserVersion": "97.0",
        'name': 'Parallel Test3',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
       }

firefox98_cap={"browserName": "firefox",
        "browserVersion": "98.0",
        'name': 'Parallel Test4',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
       }



@pytest.fixture(params=["firefox_97", "firefox_98"],scope="class")
def driver_init(request):
    if request.param == "firefox_97":
        web_driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=firefox97_cap)
    if request.param == "firefox_98":
        web_driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=firefox98_cap)
    request.cls.driver = web_driver
    yield web_driver
    web_driver.close()
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):


    def test_open_urls(self):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)
        time.sleep(5)

    def test_open_uri(self, driver_init):
        driver_init.get("https://www.lambdatest.com/")
        print(driver_init.title)
        time.sleep(5)
        assert driver_init.current_url == "https://www.lambdatet.com/"



    def test_open_urld(self, driver_init):
        driver_init.get("https://www.lambdatest.com/")
        print(driver_init.title)
        time.sleep(5)
        assert driver_init.current_url == "https://www.lambdatest.com/"

