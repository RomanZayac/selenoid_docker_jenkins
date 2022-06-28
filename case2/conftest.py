import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    capabilities = {
        "browserName": "firefox",
        "browserVersion": "101.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    browser.maximize_window()

    yield browser
    browser.close()