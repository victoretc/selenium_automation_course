import pytest
from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.auth_page_locators import AuthPage
from lesson2.hw_2.tests.configuration import BaseUrls, TestData

def test_authorization(driver):
    driver.get(BaseUrls.BASE_URL)
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD).send_keys(TestData.LOGIN_STANDARD_USER)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD).send_keys(TestData.PASSWORD_STANDARD_USER)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()
    assert driver.current_url == BaseUrls.PRODUCT_PAGE_URL

@pytest.mark.parametrize("login_value, password_value, expected_error_message",
                         [(TestData.LOGIN_INVALID_USER, TestData.INVALID_PASSWORD, "Epic sadface: Username and password do not match any user in this service"),
                          (TestData.LOGIN_EMPTY, TestData.PASSWORD_EMPTY, "Epic sadface: Username is required"),
                          (TestData.LOGIN_LOCKED_USER, TestData.PASSWORD_LOCKED_USER, "Epic sadface: Sorry, this user has been locked out."),
                          ])
def test_authorization_invalid_data(driver, login_value, password_value, expected_error_message):
    driver.get(BaseUrls.BASE_URL)
    login_field = driver.find_element(By.XPATH, AuthPage.USERNAME_FIELD)
    login_field.send_keys(login_value)
    password_field = driver.find_element(By.XPATH, AuthPage.PASSWORD_FIELD)
    password_field.send_keys(password_value)
    driver.find_element(By.XPATH, AuthPage.LOGIN_BUTTON).click()

    """username underline color"""
    user_underline = driver.find_element(By.CSS_SELECTOR, AuthPage.USERNAME_ERROR_BORDER)
    user_error_underline = user_underline.value_of_css_property("border-bottom-color")
    assert user_error_underline == 'rgba(226, 35, 26, 1)'  # #e2231a

    """error username btn"""
    user_error_btn = driver.find_element(By.CSS_SELECTOR, AuthPage.USERNAME_ERROR_CLOSE_BUTTON)
    assert user_error_btn.is_displayed()
    assert user_error_btn.is_enabled()

    """password underline color"""
    password_underline = driver.find_element(By.CSS_SELECTOR, AuthPage.PASSWORD_ERROR_BORDER)
    password_error_underline = password_underline.value_of_css_property("border-bottom-color")
    assert user_error_underline == 'rgba(226, 35, 26, 1)'  # #e2231a

    """error password btn"""
    password_error_btn = driver.find_element(By.CSS_SELECTOR, AuthPage.PASSWORD_ERROR_CLOSE_BUTTON)
    assert password_error_btn.is_displayed()
    assert password_error_btn.is_enabled()

    """error container text"""
    warning_text = driver.find_element(By.XPATH, AuthPage.BOTH_USERNAME_PASSWORD_ERROR_MESSAGE)
    value_warring_text = warning_text.text
    assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"

    """error container color"""
    message_container = driver.find_element(By.CSS_SELECTOR, AuthPage.MESSAGE_ERROR_CONTAINER)
    background_error_container = message_container.value_of_css_property("background-color")
    assert user_error_underline == 'rgba(226, 35, 26, 1)'  # #e2231a

    """error container btn"""
    warning_error_btn = driver.find_element(By.XPATH, AuthPage.MESSAGE_ERROR_BUTTON)
    assert warning_error_btn.is_displayed()
    assert warning_error_btn.is_enabled()


