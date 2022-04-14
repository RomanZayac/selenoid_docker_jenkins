# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.mark.usefixtures("setup")
# class TestExampleOne:
#
#
#     def test_one(self):
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         x = "hello"
#         assert 'e' in x
#
#     def test_three(self):
#         x = 3
#         assert 3 == x
#
#     def test_four(self):
#         x = 4
#         assert 5 == x
#
#     def test_open(self, setup):
#
#         # webdriver.Remote.get(setup, "https://www.selenium.dev/")
#         driver = webdriver.Remote
#         # time.sleep(2)
#         driver.get(setup, "https://www.selenium.dev/blog/")
#         time.sleep(2)
#         element = driver.find_element(setup, By.XPATH, "//h1")
#         text = element.text
#         assert "Blog" in text
