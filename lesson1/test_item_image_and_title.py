# Карточка товара
# Успешный переход к карточке товара после клика на картинку товара
# Успешный переход к карточке товара после клика на название товара


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_item_image():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # clicking on the item image
    item_image = driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
    item_image.click()
    time.sleep(1)

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert "Sauce Labs Backpack" in driver.page_source

    driver.quit()

def test_item_title():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()


    # clicking on the item title
    item_title = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    item_title.click()
    time.sleep(1)

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert "Sauce Labs Backpack" in driver.page_source
    driver.quit()