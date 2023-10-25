from lesson1.hw_1.configuration import BASE_URL, PRODUCT_PAGE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Checking if the "Reset App State" button in the menu works"""

def test_reset_btn():

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
    time.sleep(1)
    """checking product page"""
    product_page = driver.find_element(
        By.XPATH, "//span [@class ='title']"
    )
    value_product_page = product_page.text
    assert value_product_page == "Products"
    """checking product page - the second check"""
    current_page_url = driver.current_url
    assert PRODUCT_PAGE_URL == current_page_url
    """add item to cart - for checking reset button in future"""
    item_button = driver.find_element(
        By.XPATH,
        "//button[@name='add-to-cart-sauce-labs-bolt-t-shirt']"
    )
    item_button.click()
    """click burger menu"""
    burger_menu = driver.find_element(
        By.XPATH,
        "//button[@id='react-burger-menu-btn']"
    )
    burger_menu.click()
    """click - reset"""
    reset_button = driver.find_element(
        By.XPATH,
        "//a[text()='Reset App State']"
    )
    reset_button.click()
    time.sleep(1)
    """checking - reset"""
    cart_item = driver.find_element(
        By.XPATH,
        "//a[@class='shopping_cart_link']"
    )
    assert cart_item.text == ''
    time.sleep(1)

    driver.quit()

