from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.auth_page_locators import AuthPage
from lesson2.hw_2.tests.configuration import BaseUrls, TestData

def test_authorization(driver):
    driver.get(BaseUrls.BASE_URL)
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD).send_keys(TestData.LOGIN_STANDARD_USER)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD).send_keys(TestData.PASSWORD_STANDARD_USER)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()
    assert driver.current_url == BaseUrls.PRODUCT_PAGE_URL

def test_authorization_invalid_data(driver):
    driver.get(BaseUrls.BASE_URL)
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD).send_keys(TestData.LOGIN_STANDARD_USER)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD).send_keys(TestData.INVALID_PASSWORD)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()
    warring_text = driver.find_element(By.XPATH, AuthPage.BOTH_USERNAME_PASSWORD_ERROR_MESSAGE)
    value_warring_text = warring_text.text
    assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"

def test_auth_locked_user(driver):
    driver.get(BaseUrls.BASE_URL)
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD).send_keys(TestData.LOGIN_LOCKED_USER)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD).send_keys(TestData.PASSWORD_LOCKED_USER)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()
    warring_text = driver.find_element(By.XPATH, AuthPage.LOCKED_USER_ERROR_MESSAGE)
    value_warring_text = warring_text.text
    assert value_warring_text == "Epic sadface: Sorry, this user has been locked out."




