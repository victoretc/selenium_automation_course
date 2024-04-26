from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    time.sleep(3)

    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()

    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    text_after = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    assert cart_badge.text == '1'
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    assert text_before == text_after
    assert remove_button.text == "Remove"

    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    time.sleep(3)

    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()

    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    text_after = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
    remove_button = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    assert cart_badge.text == '1'
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    assert text_before == text_after
    assert remove_button.text == "Remove"

    driver.quit()
