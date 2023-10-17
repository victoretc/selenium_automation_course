from configuration import BASE_URL, PRODUCT_PAGE_URL, ITEM_PAGE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Successful transition to the product card after clicking on the product picture"""

def test_click_items_image():

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
        "//span[@class ='title']"
    )
    value_product_page = product_page.text
    assert value_product_page == "Products"
    """checking product page - the second check"""
    current_page_url = driver.current_url
    assert PRODUCT_PAGE_URL == current_page_url
    """click on item image"""
    item_image = driver.find_element(
        By.XPATH,
        "//img[@src='/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg']"
    )
    item_image.click()
    """checking item page"""
    current_page_url = driver.current_url
    assert ITEM_PAGE_URL == current_page_url

    driver.quit()
