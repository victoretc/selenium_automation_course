from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_remove_from_cart_from_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_button = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    item_button.click()

    # adding item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()
    time.sleep(3)

    # removing item from the item card
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    remove_button.click()
    time.sleep(3)

    # assert add_to_cart_button.is_displayed()
    assert "Remove" not in driver.page_source
    assert "Add to cart" in driver.page_source

    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()
    time.sleep(3)

    assert "Sauce Labs Backpack" not in driver.page_source

    driver.quit()
