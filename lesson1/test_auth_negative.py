from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()


def test_login_form_negative():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.find_element(By.XPATH, '//button[@class="error-button"]').is_displayed()

    driver.quit()