from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_good_to_cart():
    driver.get("https://www.saucedemo.com/inventory.html")

    # select item
    #driver.find_element(By.CSS_SELECTOR, "a[id='item_3_title_link'] > div[class='inventory_item_name']").text

    # click on img
    #item_img = driver.find_element(By.CSS_SELECTOR, "a#item_3_img_link").click()
    #driver.find_element("/static/media/red-tatt-1200x1500.30dadef4.jpg", "img").click()
    #driver.find_element("#item_3_img_link > img").click()
    #driver.find_element(By.LINK_TEXT, "/static/media/red-tatt-1200x1500.30dadef4.jpg").click()
    #driver.find_element("#item_3_img_link", "img").click()

    # check item card
    item_URL = driver.current_url
    expected_URL = "https://www.saucedemo.com/inventory-item.html?id=3"

    assert expected_URL == item_URL

