from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_remove_good_from_cart():
    driver.get("https://www.saucedemo.com/")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # select item
    # add item 1 to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    # add item 2 to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    # go to cart and check it
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
    count_before_removing = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    #item_in_cart = driver.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div [contains(text(), "Sauce Labs Bolt T-Shirt")]')
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]').click()
    count_after_removing = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    assert int(count_after_removing) == int(count_before_removing) - 1


def test_remove_good_from_cart2():
    driver.get("https://www.saucedemo.com/inventory.html")

    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # select item
    # add item to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    # go to cart and check it
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
    elements_before = len(driver.find_elements(By.CLASS_NAME, 'cart_item'))
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    count_after_removing = len(driver.find_elements(By.CLASS_NAME, 'cart_item'))

    assert elements_before == count_after_removing + 1
