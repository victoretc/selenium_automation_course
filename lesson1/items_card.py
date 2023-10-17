from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_open_items_card_by_image():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    first_item_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

    item_image = driver.find_element(By.CSS_SELECTOR, 'img.inventory_item_img')
    # print(item_image.get_attribute('alt'))
    item_image.click()

    product_card_item_name = driver.find_element(By.CLASS_NAME, 'inventory_details_name').text

    assert first_item_name == product_card_item_name

#base64 - сравнить картинки