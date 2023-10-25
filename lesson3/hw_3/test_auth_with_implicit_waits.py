from selenium.webdriver.common.by import By
from lesson3.hw_3.configuration import BaseUrls, LocatorsText, TestData
from lesson3.hw_3.locators import AuthLocators

def test_auth_with_implicit_waits(driver, implicit_wait):
    """test with implicit waits"""

    auth_page = driver.get(BaseUrls.AUTH_URL)

    """check h1 - header"""
    h1_header = driver.find_element(By.XPATH, AuthLocators.AUTH_H1_TEXT)
    assert h1_header.text == LocatorsText.H1_HEADER_TEXT

    start_testing_btn = driver.find_element(By.CSS_SELECTOR, AuthLocators.VISION_START_TEST_BUTTON).click()  # change the locator
    input_login = driver.find_element(By.XPATH, AuthLocators.INPUT_LOGIN).send_keys(TestData.LOGIN)
    input_password = driver.find_element(By.XPATH, AuthLocators.INPUT_PASSWORD).send_keys(TestData.PASSWORD)
    checkbox = driver.find_element(By.XPATH, AuthLocators.AGREE_CHECKBOX).click()
    reg_btn = driver.find_element(By.XPATH, AuthLocators.REGISTRATION_BUTTON).click()

    """check loader"""
    loader = driver.find_element(By.XPATH, AuthLocators.LOADER)
    assert loader.is_displayed()

    """check success message"""
    success_message = driver.find_element(By.XPATH, AuthLocators.VISION_SUCCESS_MESSAGE)  # change the locator
    assert success_message.is_displayed()

