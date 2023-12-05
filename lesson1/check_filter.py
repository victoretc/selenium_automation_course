from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_filter_A_Z():
    driver.get("https://www.saucedemo.com/")
    # authorization
    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    #container_sort = driver.find_element(By.CLASS_NAME, '[class="product_sort_container"]')
    #container_sort.click()
    # find all elements
    all_elem_ZA = driver.find_elements(By.XPATH, "//*[contains(text(), 'Sauce Labs')]")
    # mix the elements
    driver.find_element(By.XPATH, '//*[@id="header_container"]//select').click()
    sort_element = driver.find_element(By.XPATH, '//*[@id="header_container"]//option[2]')
    sort_element.click()
    time.sleep(3)
    all_elem_ZA = driver.find_elements(By.CSS_SELECTOR, 'inventory_item_name ')

    # click item in menu
    sort_element = driver.find_element(By.XPATH, '//*[@id="header_container"]//option[1]')
    sort_element.click()
    time.sleep(3)
    all_elem_AZ = driver.find_elements(By.CSS_SELECTOR, 'inventory_item_name ')
    print(len(all_elem_AZ))
    for a in all_elem_AZ:
        print(a.text)
    assert all_elem_AZ == all_elem_ZA