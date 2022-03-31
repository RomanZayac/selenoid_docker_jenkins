import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="session")
def setup(request):

    # capabilities = {
    #     "browserName": "firefox",
    #     "browserVersion": "98.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    # }
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_capability("browserVersion", "97.0")
    firefox_options.set_capability("browserName", "firefox")
    firefox_options.set_capability("enableVNC", True)
    firefox_options.set_capability("enableVideo", False)
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=firefox_options)

    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     desired_capabilities=capabilities)
    driver.maximize_window()

    yield driver
    driver.close()