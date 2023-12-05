from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_go_to_item_card_by_pic():
    driver.get("https://www.saucedemo.com/inventory.html")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # click on img
    driver.find_element(By.CSS_SELECTOR, "a#item_3_img_link").click()

    # check item card
    item_URL = driver.current_url
    expected_URL = "https://www.saucedemo.com/inventory-item.html?id=3"

    assert expected_URL == item_URL

