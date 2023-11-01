from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import locators
import time


def test_filter_A_Z(driver, login):
    # find all elements
    items_before = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    list_before = []
    for a in items_before:
        list_before.append(a.text)
    #filter1.select_by_index(1)
    #filter1.select_by_name("az")
    filter1 = Select(driver.find_element(By.CSS_SELECTOR, 'select[data-test="product_sort_container"]'))
    filter1.select_by_visible_text("Name (Z to A)")
    itemsZA = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item_name')
    list_after = []
    for a in itemsZA:
        list_after.append(a.text)
    assert list_before == sorted(list_after)
    #, reverse=True)

