import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.auth_page_locators import AuthPage
from lesson2.hw_2.tests.configuration import BaseUrls, TestData

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def authorization(driver):
    driver.get(BaseUrls.BASE_URL)
    driver.maximize_window()
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD).send_keys(TestData.LOGIN_STANDARD_USER)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD).send_keys(TestData.PASSWORD_STANDARD_USER)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()
    assert driver.current_url == BaseUrls.PRODUCT_PAGE_URL

