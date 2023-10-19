from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_login_form_noncorrect():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("other_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("just_sauce")

    expected_error_message = driver.find_element(By.CSS_SELECTOR, '[class="error-message-container"] ')

    assert expected_error_message.is_displayed()

    driver.quit()