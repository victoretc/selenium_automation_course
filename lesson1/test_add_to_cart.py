from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_good_to_cart():
    driver.get("https://www.saucedemo.com/")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()
    # select item
    text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link']").text

    # add item to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # go to cart and check it
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
    text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']").text

    assert text_before == text_after