import pyautogui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_sort_desc(driver, auth):

    data = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_list = [i.text for i in data]

    sort_button = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    sort_button.select_by_index(1)

    reversed_data = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
    desc_product_list = [i.text for i in reversed_data]

    assert sorted(product_list, reverse=True) == desc_product_list
