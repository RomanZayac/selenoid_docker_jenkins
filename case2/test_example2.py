import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExampleTwo:


    def test_funcfast(self):
        time.sleep(0.1)

    def test_funcslow1(self):
        time.sleep(0.2)

    def test_funcslow2(self):
        time.sleep(0.3)