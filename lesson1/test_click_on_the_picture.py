from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_click_on_picture():

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")

    driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
    login_button.click()

    driver.find_element(By.XPATH, "//img[@alt='Sauce Labs Onesie']").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=2"

    driver.quit()
