from lesson1.hw_1.configuration import BASE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


"""Delete item from product card"""

def test_delete_from_product_card():

    driver.get(BASE_URL)
    driver.maximize_window()

    """input name"""
    user_name = driver.find_element(
        By.XPATH,
        "//input[@id='user-name']"
    )
    user_name.send_keys(LOGIN_STANDARD_USER)
    """input password"""
    password = driver.find_element(
        By.XPATH,
        "//input[@id='password']"
    )
    password.send_keys(PASSWORD_ALL)
    """click login"""
    button_login = driver.find_element(
        By.XPATH,
        "//input[@id='login-button']"
    )
    button_login.click()
    """open product card"""
    item_backpack = driver.find_element(
        By.XPATH,
        "//a[@id='item_4_title_link']"
    )
    item_backpack.click()
    """click button item inside item`s card"""
    button_item_backpack = driver.find_element(
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-backpack']"
    )
    button_item_backpack.click()
    """remove added item from the cart"""
    button_cart = driver.find_element(
        By.XPATH,
        "//button[@id='remove-sauce-labs-backpack']"
    )
    button_cart.click()
    time.sleep(1)
    """checking that the item was deleted from the cart"""
    cart_item = driver.find_element(
        By.XPATH,
        "//a[@class='shopping_cart_link']"
    )
    verification_item_delete = cart_item.text
    assert verification_item_delete == ''

    driver.quit()
