from configuration import BASE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


"""Add item to cart"""

def test_add_item_to_cart():

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
    """add item to cart"""
    add_item_backpack = driver.find_element(
        By.XPATH,
        "//button[@id='add-to-cart-sauce-labs-backpack']"
    )
    add_item_backpack.click()
    """go to the cart"""
    cart = driver.find_element(
        By.XPATH,
        "//a[@class='shopping_cart_link']"
    )
    cart.click()
    time.sleep(2)
    """checking added item to cart"""
    item_backpack_in_cart = driver.find_element(
        By.XPATH,
        "//a[@id='item_4_title_link']"
    )
    verification_item_backpack = item_backpack_in_cart.text
    assert verification_item_backpack == "Sauce Labs Backpack"
    """checking add item to cart - the 2nd check"""
    verification_add_item_backpack = driver.find_element(
        By.XPATH,
        "//button[@id='remove-sauce-labs-backpack']"
    )
    add_item_backpack = verification_add_item_backpack.text
    assert add_item_backpack == "Remove"

    driver.quit()

