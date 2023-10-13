from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
def test_remove_from_product_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    product = driver.find_element(By.XPATH, "//div[contains(text(),'Test.allTheThings() T-Shirt (Red)')]")
    product.click()

    the_product_before = driver.find_element(By.XPATH, "//*[@name='add-to-cart-test.allthethings()-t-shirt-(red)']").text
    print(the_product_before)

    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    add_to_cart_button.click()

    remove_button = driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)")
    remove_button.click()

    the_product_after = driver.find_element(By.XPATH, "//*[@name='add-to-cart-test.allthethings()-t-shirt-(red)']").text

    assert the_product_before == the_product_after
