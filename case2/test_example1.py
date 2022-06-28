import time


def test_open_url(driver):
    driver.get("https://www.google.com/")
    print(driver.title)
    time.sleep(5)


def test_title_of_site(driver):
    driver.get("https://www.facebook.com/")
    title = driver.title
    time.sleep(5)
    assert title == "Facebook - log in or sign up", "The title is not the same"
