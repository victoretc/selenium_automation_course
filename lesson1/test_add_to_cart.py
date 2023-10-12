import time
from _ast import Assert

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()


def test_add_item_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    title_expected = (driver.find_element
             (By.CSS_SELECTOR, "a[id='item_4_title_link']  >  div[class='inventory_item_name']")).text

    #     button[data-test='add-to-cart-sauce-labs-backpack'
    add_button = driver.find_element(By.CSS_SELECTOR,
                                     "button[data-test='add-to-cart-sauce-labs-backpack']")
    add_button.click()
    #  //div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    #  //div[@class='cart_quantity']
    # a[id='item_4_title_link']  >  div[class='inventory_item_name']

    title_action = driver.find_element(By.XPATH, "//div[contains(text() , 'Sauce Labs Backpack')]").text
                    # (By.CSS_SELECTOR, "a[id='item_4_title_link']  >  div[class='inventory_item_name']")).text

    assert title_expected == title_action


