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

    item = driver.find_element(By.XPATH, '//div[contains(text(),"Sauce Labs Backpack")]')
    item.click()

    time.sleep(3)
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"

    added_item = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    added_item.click()
    time.sleep(3)

    shopping_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart.click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '// div[contains(text(), "Sauce Labs Backpack")]').is_displayed()

    driver.quit()

