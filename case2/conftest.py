import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    capabilities = {
        "browserName": "firefox",
        "browserVersion": "98.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=capabilities)
    driver.maximize_window()

    yield driver
    driver.close()