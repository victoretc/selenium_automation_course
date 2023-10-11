from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_logout():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu_button = driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
    burger_menu_button.click()

    time.sleep(3)

    logout_button = driver.find_element(By. CSS_SELECTOR, '#logout_sidebar_link')
    logout_button.click()

    assert driver.current_url == 'https://www.sauceemo.com/'

    driver.quit()
