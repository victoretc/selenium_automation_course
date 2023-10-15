from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_from_catalog():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    first_item_add_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    first_item_add_button.click()

    item_in_the_cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    #assert item_in_the_cart.is_displayed()
    assert item_in_the_cart.text == '1'

def test_remove_item_from_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    first_item_add_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    first_item_add_button.click()

    cart_button = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_button.click()
    time.sleep(2)

    remove_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button.click()

    assert driver.find_elements(By.XPATH, '//div[@class="removed_cart_item"]')


def test_add_item_from_items_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    items_image = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]')
    items_image.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    item_in_the_cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    # assert item_in_the_cart.is_displayed()
    assert item_in_the_cart.text == '1'





