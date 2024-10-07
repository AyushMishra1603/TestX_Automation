import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service_obj = Service("C:\\Browserdrivers\\geckodriver-v0.34.0-win32\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)


def test_setup():
    driver.implicitly_wait(4)
    driver.get("https://www.xbox.com/en-US/")
    time.sleep(2)


def test_get_title():
    title = driver.title
    assert "Xbox Official Site" in title


def test_screen_shot():
    driver.get_screenshot_as_file("C:\\PythonSelenium\\Xbox_Automation\\End_To_End_Testing\\Screen-shots\\ss.png")


def test_browser_close():
    driver.close()
