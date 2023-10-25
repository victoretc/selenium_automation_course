from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    url_befor = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.XPATH, '// button[ @ id = "react-burger-menu-btn"]')
    burger_menu.click()

    time.sleep(3)

    logout_text = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
    logout_text.click()

    url_after = driver.current_url

    assert url_befor == url_after

    # assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()

