from selenium.webdriver.common.by import By
import time


def test_sort_asc(driver, auth):

    data = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    product_list = [i.text for i in data]

    assert product_list == sorted(product_list)
