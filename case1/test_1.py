import time
from selenium import webdriver



capabilities = {
    "browserName": "firefox",
    "browserVersion": "101.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

def test_open_urls():
    driver.get("https://www.facebook.com/")
    print(driver.title)
    time.sleep(5)
