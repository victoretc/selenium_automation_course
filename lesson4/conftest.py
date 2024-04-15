import pytest
from selenium import webdriver
from pages.auth_page import LoginPage
from urls import base_url

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, base_url)
    return page

