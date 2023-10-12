from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


def test_add_to_cart_from_product_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_in_the_list = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]').text

    product_card = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]')
    product_card.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    add_to_cart_button.click()

    shopping_cart = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
    shopping_cart.click()

    item_in_the_cart = driver.find_element(By.XPATH, '//*[@class="inventory_item_name"]').text

    assert item_in_the_list == item_in_the_cart
