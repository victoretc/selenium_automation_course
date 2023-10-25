from selenium.webdriver.common.by import By
from lesson3.hw_3.configuration import BaseUrls, LocatorsText, TestData
from lesson3.hw_3.locators import AuthLocators
from selenium.webdriver.support import expected_conditions as EC

def test_auth_with_explicit(driver, explicit_wait):
    """test with explicit waits"""

    auth_page = driver.get(BaseUrls.AUTH_URL)

    """check h1 - header"""
    h1_header = driver.find_element(By.XPATH, AuthLocators.AUTH_H1_TEXT)
    assert h1_header.text == LocatorsText.H1_HEADER_TEXT

    start_testing_btn = explicit_wait.until(EC.element_to_be_clickable((By.XPATH, AuthLocators.START_TEST_BUTTON))).click()  # the method of explicit waits is at work here
    input_login = driver.find_element(By.XPATH, AuthLocators.INPUT_LOGIN).send_keys(TestData.LOGIN)
    input_password = driver.find_element(By.XPATH, AuthLocators.INPUT_PASSWORD).send_keys(TestData.PASSWORD)
    checkbox = driver.find_element(By.XPATH, AuthLocators.AGREE_CHECKBOX).click()
    reg_btn = driver.find_element(By.XPATH, AuthLocators.REGISTRATION_BUTTON).click()

    """check loader"""
    loader = explicit_wait.until(EC.visibility_of_element_located((By.XPATH, AuthLocators.LOADER)))  # the method of explicit waits is at work here
    assert loader.text == LocatorsText.LOADER_TEXT

    """the 2nd check loader"""
    expected_loader = explicit_wait.until(EC.text_to_be_present_in_element_attribute((By.ID, 'loader'), 'class', 'hidden'))  # the method of explicit waits is at work here
    loader = driver.find_element(By.ID, 'loader').get_attribute('class') == 'hidden'
    assert loader == expected_loader

    """check success message"""
    suc_message = explicit_wait.until(EC.visibility_of_element_located((By.XPATH, AuthLocators.SUCCESS_MESSAGE)))  # the method of explicit waits is at work here
    assert suc_message.text == LocatorsText.SUCCESS_MESSAGE_TEXT



