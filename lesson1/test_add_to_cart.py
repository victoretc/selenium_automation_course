import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_add_item_in_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div[@class="inventory_item_name"]').text
    time.sleep(2)
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    add_to_cart_button.click()
    time.sleep(2)
    shopping_cart = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
    shopping_cart.click()
    time.sleep(2)
    item_in_the_cart = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div[@class="inventory_item_name"]').text
    assert item == item_in_the_cart

    driver.quit()
