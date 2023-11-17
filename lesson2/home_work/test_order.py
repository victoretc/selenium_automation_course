from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test_make_order(driver, auth):

    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()
    driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Nariman")
    driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Mirzakhanov")
    driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("94086")
    driver.find_element(By.XPATH, "//*[@id='continue']").click()
    finish_button = driver.find_element(By.XPATH, "//*[@id='finish']")
    ActionChains(driver)\
        .scroll_to_element(finish_button)\
        .perform()
    finish_button.click()
    actual_result = driver.find_element(By.XPATH, "//*[@class='complete-header']").text
    expected_result = "Thank you for your order!"
    assert actual_result == expected_result


