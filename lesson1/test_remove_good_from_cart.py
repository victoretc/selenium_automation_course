from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_good_to_cart():
    driver.get("https://www.saucedemo.com/")
    # authorization
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # select item
    # add item 1 to cart
    button_add = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    button_add.click()
    # add item 2 to cart
    button_add = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    button_add.click()
    # go to cart and check it
    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()
    count_before_removing = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    #item_in_cart = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div [contains(text(), "Sauce Labs Bolt T-Shirt")]')

    remove_item = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
    remove_item.click()
    count_after_removing = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    assert int(count_after_removing) == int(count_before_removing) - 1


