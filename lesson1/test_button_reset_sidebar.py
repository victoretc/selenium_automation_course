from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# bag: buttons reset remain ON


def test_check_button_reset():
    driver.get("https://www.saucedemo.com/")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # add items to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # check nr of items in cart
    time.sleep(1)
    item_in_the_cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    items_before = item_in_the_cart.text    #  == '2'

    #go to burger menu
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)
    # click item reset in menu
    driver.find_element(By.ID, 'reset_sidebar_link').click()
    buttons_remove = driver.find_elements(By.CSS_SELECTOR, '*[name^="remove"]')

    item_in_the_cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    items_after = item_in_the_cart.text  # == '0'
    assert items_after == "", "cart is not empty"
    assert len(buttons_remove) == 0, "cart is empty, but buttons Remove are still on"
