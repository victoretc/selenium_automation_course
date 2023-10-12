from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_go_to_item_card_by_title():
    driver.get("https://www.saucedemo.com/inventory.html")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # click on title
    driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > div").click()

    # check item card
    expected_title = "Sauce Labs Fleece Jacket"
    actual_title = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Fleece Jacket')]").text

    assert expected_title == actual_title
