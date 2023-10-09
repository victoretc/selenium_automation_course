from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_redirection_to_item_page():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]/div[@class="inventory_item_name"]').text

    item = driver.find_element(By.XPATH, '//a[@id="item_3_img_link"]')
    item.click()


    text_after = driver.find_element(By.XPATH, "//div[contains(text(), 'T-Shirt (Red)')]").text

    assert text_before == text_after
