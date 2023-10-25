from selenium.webdriver import ActionChains

from lesson1.hw_1.configuration import BASE_URL, PRODUCT_PAGE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL, VALID_ZIP, VALID_NAME,\
    VALID_SURNAME
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Checkout using correct data"""

def test_checkout():

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
        By.XPATH,
        "//span [@class ='title']"
    )
    value_product_page = product_page.text
    assert value_product_page == "Products"
    """checking product page - the second check"""
    current_page_url = driver.current_url
    assert PRODUCT_PAGE_URL == current_page_url
    """scroll down to item page and click"""
    red_shirt = driver.find_element(
        By.XPATH,
        "//img[@src='/static/media/red-tatt-1200x1500.30dadef4.jpg']")
    ActionChains(driver).scroll_to_element(red_shirt).perform()
    red_shirt.click()
    time.sleep(2)
    #  driver.execute_script("window.scrollTo(0, 500)") #  scroll the 2nd
    """add item to cart"""
    add_button = driver.find_element(
        By.XPATH,
        "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    )
    add_button.click()
    time.sleep(1)
    """go to cart"""
    cart_button = driver.find_element(
        By.XPATH,
        "//div[@id='shopping_cart_container']"
    )
    cart_button.click()
    time.sleep(1)
    """go to checkout"""
    checkout_button = driver.find_element(
        By.XPATH,
        "//button[@id='checkout']"
    )
    checkout_button.click()
    """fill in order form - name"""
    first_name = driver.find_element(
        By.XPATH,
        "//input[@id='first-name']"
    )
    first_name.send_keys(VALID_NAME)
    """fill in order form - lastname"""
    last_name = driver.find_element(
        By.XPATH,
        "//input[@id='last-name']"
    )
    last_name.send_keys(VALID_SURNAME)
    """fill in order form - zip"""
    zip_name = driver.find_element(
        By.XPATH,
        "//input[@data-test='postalCode']"
    )
    zip_name.send_keys(VALID_ZIP)
    """click button continue"""
    continue_button = driver.find_element(
        By.XPATH,
        "//input[@name='continue']"
    )
    continue_button.click()
    """checking checkout-item name"""
    item_name = driver.find_element(
        By.XPATH,
        "//div[@class='inventory_item_name']"
    )
    assert item_name.text == 'Test.allTheThings() T-Shirt (Red)'
    """checking checkout-item price"""
    item_price = driver.find_element(
        By.XPATH,
        "//div[@class='inventory_item_price']"
    )
    assert item_price.text == '$15.99'
    """click button-finish"""
    finish_button = driver.find_element(
        By.XPATH,
        "//button[@id='finish']"
    )
    finish_button.click()
    """checking checkout-item price"""
    complete_checkout = driver.find_element(
        By.XPATH,
        "//span[text()='Checkout: Complete!']"
    )
    assert complete_checkout.text == 'Checkout: Complete!'

    driver.quit()

