import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
firefox97_cap={
    "browserName": "firefox",
        "browserVersion": "97.0",
        'name': 'Parallel Test3'
       }

firefox98_cap=  {
            "browserName": "firefox",
            "browserVersion": "98.0",
            'name': 'Parallel Test4',
        }

Firefox97 = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=firefox97_cap)
Firefox98 = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=firefox98_cap)
class TestLog():
    @pytest.fixture()
    def setup1(self):
        browser = [Firefox97, Firefox98]
        for i in browser:
            self.driver = i
        yield

        self.driver.quit()

