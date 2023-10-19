from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_add_item_from_catalog():
    driver.get("https://www.saucedemo.com/inventory.html")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    # add item
    driver.find_element(By.XPATH, '// *[ @ id = "add-to-cart-sauce-labs-bike-light"]').click()
    # go to cart and check it
    driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
    # check item in cart
    expected_name = "Sauce Labs Bike Light"
    actual_name = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Bike Light')]").text

    assert expected_name == actual_name
    