from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_item_in_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']").text
    print(item)

    text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']")


    button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, "div[class='shopping_cart_container']")
    cart.click()

    #текст до и текст после для того, чтобы проверить правильность товара после вложения в корзину

    text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']")
    assert text_before == text_after






