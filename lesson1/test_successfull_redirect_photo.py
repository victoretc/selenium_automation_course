from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    picture_before = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Bike Light"]')

    picture_item = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Bike Light"]')
    picture_item.click()

    time.sleep(3)

    picture_after = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Bike Light"]')

    assert driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Bike Light"]').is_displayed()
    # assert picture_item == picture_after
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'