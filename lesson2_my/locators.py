import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CARD_ITEM4_URL = "https://www.saucedemo.com/inventory-item.html?id=3"

BASKET = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")
COUNT_ITEMS_IN_BASKET = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

ELEM1_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
ELEM1_IN_BASKET = (By.XPATH, "//*[contains(text(),'Sauce Labs Bike Light')]")

ELEM2_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
ELEM2_IN_BASKET = (By.XPATH, "//*[contains(text(),'Sauce Labs Backpack')]")

ELEM3_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
ELEM3_IN_BASKET = (By.XPATH, "//*[contains(text(),'Sauce Labs Bolt T Shirt')]")
REMOVE_ELEM3_FROM_BASKET = (By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
ELEM3_TITLE_IN_BASKET = (By.ID, 'item_4_title_link')
ELEM3_IN_CATALOG = (By.CSS_SELECTOR, "a[id='item_1_title_link']")

ELEM4_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
ELEM4_PIC_IN_CATALOG = (By.CSS_SELECTOR, "a#item_3_img_link")

ELEM5_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
ELEM5_TITLE_IN_CATALOG = (By.CSS_SELECTOR, "#item_5_title_link > div")

ELEM6_ADD_FROM_CATALOG = (By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')

ALL_ELEM_IN_CATALOG = [ELEM1_ADD_FROM_CATALOG, ELEM2_ADD_FROM_CATALOG, ELEM3_ADD_FROM_CATALOG]

