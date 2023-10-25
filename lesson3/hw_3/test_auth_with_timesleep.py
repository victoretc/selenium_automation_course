import time
from selenium.webdriver.common.by import By
from lesson3.hw_3.configuration import BaseUrls, LocatorsText, TestData
from lesson3.hw_3.locators import AuthLocators


def test_auth(driver):
    """test with time sleep"""

    auth_page = driver.get(BaseUrls.AUTH_URL)

    # """check url"""
    # current_url = driver.current_url
    # assert current_url == BaseUrls.AUTH_URL

    """check h1 - header"""
    h1_header = driver.find_element(By.XPATH, AuthLocators.AUTH_H1_TEXT)
    assert h1_header.text == LocatorsText.H1_HEADER_TEXT

    time.sleep(5)  # wait for button "Start Testing"
    start_testing_btn = driver.find_element(By.XPATH, AuthLocators.START_TEST_BUTTON).click()

    # """check start testing button"""
    # reg_form_login_text = driver.find_element(By.XPATH, AuthLocators.LOGIN_FORM_TEXT).text
    # assert reg_form_login_text == LocatorsText.LOGIN_TEXT
    # reg_form_password_text = driver.find_element(By.XPATH, AuthLocators.PASSWORD_FORM_TEXT).text
    # assert reg_form_password_text == LocatorsText.PASSWORD_TEXT

    input_login = driver.find_element(By.XPATH, AuthLocators.INPUT_LOGIN).send_keys(TestData.LOGIN)
    input_password = driver.find_element(By.XPATH, AuthLocators.INPUT_PASSWORD).send_keys(TestData.PASSWORD)
    checkbox = driver.find_element(By.XPATH, AuthLocators.AGREE_CHECKBOX).click()
    reg_btn = driver.find_element(By.XPATH, AuthLocators.REGISTRATION_BUTTON).click()

    """check loader"""
    loader = driver.find_element(By.XPATH, AuthLocators.LOADER)
    assert loader.is_displayed()

    """check success message"""
    time.sleep(3)  # wait for message
    suc_message = driver.find_element(By.XPATH, AuthLocators.SUCCESS_MESSAGE)
    assert suc_message.text == LocatorsText.SUCCESS_MESSAGE_TEXT



