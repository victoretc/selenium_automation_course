from selenium.webdriver.common.by import By


def test_login_form_correct(driver):

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_form_uncorrect(driver):

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    error_button_text = driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text

    assert error_button_text == 'Epic sadface: Username and password do not match any user in this service'










