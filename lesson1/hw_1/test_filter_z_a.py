from lesson1.hw_1.configuration import BASE_URL, PRODUCT_PAGE_URL, LOGIN_STANDARD_USER, PASSWORD_ALL
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Filter function check (Z to A)"""

def test_filter_za():

    driver.get(BASE_URL)
    driver.maximize_window()

    """input name"""
    user_name = driver.find_element(
        By.XPATH,
        "//input[@id='user-name']"
    )
    user_name.send_keys(LOGIN_STANDARD_USER)
    """input password"""
    password = driver.find_element(
        By.XPATH,
        "//input[@id='password']"
    )
    password.send_keys(PASSWORD_ALL)
    """click login"""
    button_login = driver.find_element(
        By.XPATH,
        "//input[@id='login-button']"
    )
    button_login.click()
    time.sleep(1)
    """checking product page"""
    product_page = driver.find_element(
        By.XPATH,
        "//span [@class ='title']"
    )
    value_product_page = product_page.text
    assert value_product_page == "Products"
    """checking product page - the second check"""
    current_page_url = driver.current_url
    assert PRODUCT_PAGE_URL == current_page_url
    """click filter"""
    filter_button = driver.find_element(
        By.XPATH,
        "//select[@class='product_sort_container']"
    )
    filter_button.click()
    """click z-a button"""
    click_button = driver.find_element(
        By.XPATH,
        "//option[text()='Name (Z to A)']"
    )
    click_button.click()
    """checking comparing between lists"""
    """variable - for compare actual and expected result"""
    item_headers = driver.find_elements(
        By.XPATH,
        "//div[@class='inventory_item_name ']"
    )
    # list_items = [item_header.text for item_header in item_headers]
    list_items = []
    for item_header in item_headers:
        list_items.append(item_header.text)
    print(list_items)
    list_sorted = sorted(list_items, reverse=True)
    print(list_sorted)
    assert list_items == list_sorted

    driver.quit()