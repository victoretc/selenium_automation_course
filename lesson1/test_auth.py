from selenium.webdriver.common.by import By
from locators import USERNAME, PASSWORD, LOGIN_BUTTON
from data import *


def test_login_form_correct(driver):

    driver.find_element(USERNAME).send_keys(CORRECT_LOGIN)
    driver.find_element(PASSWORD).send_keys(CORRECT_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()

    assert driver.current_url == PRODUCT_LIST_URL

def test_login_form_uncorrect(driver):

    driver.find_element(USERNAME).send_keys(INCORRECT_LOGIN)
    driver.find_element(PASSWORD).send_keys(INCORRECT_PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()

    error_button_text = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text

    assert error_button_text == 'Epic sadface: Username and password do not match any user in this service'










