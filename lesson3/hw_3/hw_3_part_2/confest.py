import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


"""fixture for options"""
@pytest.fixture
def driver_options():
    options = Options()
    #options.add_argument('--headless')
    # options.add_argument('--incognito')
    options.add_argument('--window-size=1920, 1200')
    return options


"""fixture for Chromedriver"""
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


"""fixture for explicit wait"""
@pytest.fixture
def explicit_wait(driver):
    explicit_wait = WebDriverWait(driver, timeout=10)
    return explicit_wait


"""fixture for implicit wait"""
@pytest.fixture
def implicit_wait(driver):
    implicit_wait = driver.implicitly_wait(10)  # method of implicit wait (self, time_for_wait)
    return implicit_wait
