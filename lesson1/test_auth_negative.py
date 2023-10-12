from selenium import webdriver
from selenium.webdriver.common.by import By


def test_auth_negative():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    login_button.click()

    error = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text

    assert error == "Epic sadface: Username and password do not match any user in this service"

    driver.quit()
