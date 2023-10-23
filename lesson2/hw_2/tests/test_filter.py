from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.main_page_locators import MainPage

def test_filter_az(driver, authorization):
    filter_button = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_FILTER).click()
    filter_az = driver.find_element(By.XPATH, MainPage.AZ_FILTER).click()
    item_headers = driver.find_elements(By.XPATH, MainPage.MAIN_ITEM_HEADER)
    list_items = []
    for item_header in item_headers:
        list_items.append(item_header.text)
    #  print(list_items)
    list_sorted = sorted(list_items)
    #  print(list_sorted)
    assert list_items == list_sorted

def test_filter_za(driver, authorization):
    filter_button = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_FILTER).click()
    filter_az = driver.find_element(By.XPATH, MainPage.ZA_FILTER).click()
    item_headers = driver.find_elements(By.XPATH, MainPage.MAIN_ITEM_HEADER)
    list_items = []
    for item_header in item_headers:
        list_items.append(item_header.text)
    list_sorted = sorted(list_items, reverse=True)
    assert list_items == list_sorted

def test_filter_lh(driver, authorization):
    filter_button = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_FILTER).click()
    filter_h_l = driver.find_element(By.XPATH, MainPage.LTH_FILTER).click()
    price_headers = driver.find_elements(By.XPATH, MainPage.MAIN_ITEM_PRICE)
    list_prices = []
    for item_header in price_headers:
        list_prices.append(float(item_header.text.replace('$', '')))
    list_sorted = sorted(list_prices)
    assert list_prices == list_sorted

def test_filter_hl(driver, authorization):
    filter_button = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_FILTER).click()
    filter_h_l = driver.find_element(By.XPATH, MainPage.HTL_FILTER).click()
    price_headers = driver.find_elements(By.XPATH, MainPage.MAIN_ITEM_PRICE)
    list_prices = []
    for item_header in price_headers:
        list_prices.append(float(item_header.text.replace('$', '')))
    list_sorted = sorted(list_prices, reverse=True)
    assert list_prices == list_sorted

