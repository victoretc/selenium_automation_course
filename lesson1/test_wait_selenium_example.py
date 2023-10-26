import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from util import chrome_options

driver = webdriver.Chrome(options=chrome_options())


def test_load_button_without_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element(By.XPATH, "//button")
    load_content_button.click()

    welcome_message = driver.find_element(By.XPATH, "//h2")

    time.sleep(6)
    assert welcome_message.text == "Welcome to the Unstable Load Site!"


def test_load_with_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element(By.XPATH, "//button")
    load_content_button.click()

    welcome_message = driver.find_element(By.XPATH, "//h2")

    time.sleep(6)
    assert welcome_message.text == "Welcome to the Unstable Load Site!"
