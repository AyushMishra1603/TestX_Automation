import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Initialize the service for geckodriver; no need for a full path if it's in the system PATH
service_obj = Service("geckodriver")  # Just specify "geckodriver" if it's in the PATH
driver = webdriver.Firefox(service=service_obj)

def test_setup():
    driver.implicitly_wait(4)
    driver.get("https://www.xbox.com/en-US/")
    time.sleep(2)

def test_get_title():
    title = driver.title
    assert "Xbox Official Site" in title

def test_screen_shot():
    # Update the screenshot path to a relative path
    screenshot_dir = "End_To_End_Testing/Screen-shots"
    os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist
    screenshot_path = os.path.join(screenshot_dir, "ss.png")
    driver.get_screenshot_as_file(screenshot_path)

def test_browser_close():
    driver.close()

if __name__ == "__main__":
    test_setup()
    test_get_title()
    test_screen_shot()
    test_browser_close()
