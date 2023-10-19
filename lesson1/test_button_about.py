from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_check_button_about():
    driver.get("https://www.saucedemo.com/")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)
    # click item in menu
    menu_about = driver.find_element(By.ID, 'about_sidebar_link')
    menu_about.click()
    time.sleep(1)
    url_actual = driver.current_url
    url_expected = "https://saucelabs.com/"
    assert url_actual == url_expected
    