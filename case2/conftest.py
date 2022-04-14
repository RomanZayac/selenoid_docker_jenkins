import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

# caps = {
#         "browserName": "firefox",
#         "browserVersion": "98.0",
#         'name': 'Parallel Test3',
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": False
#         }}
@pytest.fixture(scope="session")
def setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserVersion", "98")
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("enableVNC", True)
    chrome_options.set_capability("enableVideo", False)
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=chrome_options)

    driver.maximize_window()
    yield driver
    driver.quit()







# for req in caps:
#     Thread(target=run_session, args=(req)).start()



# def setup(request):
#
#     capabilities = {
#         "browserName": "firefox",
#         "browserVersion": "98.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": False
#         }
#     }
#
#
#     driver = webdriver.Remote(
#         command_executor="http://localhost:4444/wd/hub",
#         desired_capabilities=capabilities)
#     driver.maximize_window()
#
#     yield driver
#     driver.quit()
#     driver.close()



# firefox_options = webdriver.FirefoxOptions()
# firefox_options.set_capability("browserVersion", "97.0")
# firefox_options.set_capability("browserName", "firefox")
# firefox_options.set_capability("enableVNC", True)
# firefox_options.set_capability("enableVideo", False)
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     options=firefox_options)
