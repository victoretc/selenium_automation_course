from lesson1.hw_1.configuration import BASE_URL, INVALID_USER, INVALID_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


"""Authorization - invalid name, password"""

def test_authorization_invalid_data():
    driver.get(BASE_URL)
    driver.maximize_window()

    """input name"""
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
    user_name.send_keys(INVALID_USER)
    """input password"""
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(INVALID_PASSWORD)
    """click login"""
    button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
    button_login.click()
    time.sleep(2)
    """Checking error text"""
    warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    value_warring_text = warring_text.text
    assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"

    driver.quit()
