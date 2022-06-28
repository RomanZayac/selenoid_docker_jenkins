import time
import pytest
from selenium import webdriver
from urllib import request

firefox101_cap = {"browserName": "firefox",
                  "browserVersion": "101.0",
                  'name': 'Parallel Test1 firefox_101',
                  "selenoid:options": {
                      "enableVNC": True,
                      "enableVideo": False
                  }
                  }

firefox100_cap = {"browserName": "firefox",
                  "browserVersion": "100.0",
                  'name': 'Parallel Test2 firefox_100.0',
                  "selenoid:options": {
                      "enableVNC": True,
                      "enableVideo": False
                  }
                  }


@pytest.fixture(params=["firefox_101", "firefox_100"], scope="class")
def driver_init(request):
    if request.param == "firefox_101":
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=firefox101_cap)
    if request.param == "firefox_100":
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=firefox100_cap)

    request.cls.driver = web_driver
    yield web_driver
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):

    def test_url(self, driver_init):
        driver_init.get("https://www.lambdatest.com/")
        print(driver_init.title)
        time.sleep(4)
        assert 1 == 1

    def test_open_url2(self, driver_init):
        driver_init.get("https://www.lambdatest.com/")
        print(driver_init.title)
        time.sleep(3)
        assert driver_init.current_url == "https://www.lambdatest.com/"

    def test_open_url3(self, driver_init):
        driver_init.get("https://www.google.com/")
        print(driver_init.title)
        time.sleep(3)
        assert driver_init.current_url == "https://www.google.com/"
# write into pytest.ini file addopts = --alluredir=report
