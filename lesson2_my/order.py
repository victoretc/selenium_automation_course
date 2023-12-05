from selenium.webdriver.common.by import By
import locators


def test_make_order(driver, login):
    driver.find_element(*locators.ELEM1_ADD_FROM_CATALOG).click()
    driver.find_element(*locators.ELEM3_ADD_FROM_CATALOG).click()
    driver.find_element(*locators.BASKET).click()
    driver.find_element(By.CSS_SELECTOR, "BUTTON[data-test='checkout']").click()
    #time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="firstName"').send_keys("Ola")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="lastName"').send_keys("Cruz")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="postalCode"').send_keys("99038")
    driver.find_element(By.CSS_SELECTOR, 'input[data-test="continue"').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="finish"]').click()

    complete = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
    assert complete.text == "Thank you for your order!"

    # проверить отмену
    # проверить что после покупки корзина пуста



