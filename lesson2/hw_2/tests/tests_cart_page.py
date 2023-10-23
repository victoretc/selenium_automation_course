
from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.main_page_locators import MainPage
from lesson2.hw_2.locators.cart_page_locators import CartPage
from lesson2.hw_2.locators.item_page_locators import ItemPage

def test_add_item_to_cart(driver, authorization):
    add_item_backpack = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_ADD_TO_CART_BUTTON).click()
    cart = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_CART).click()
    item_backpack_in_cart = driver.find_element(By.XPATH, CartPage.CART_ITEM_HEADER).text
    assert item_backpack_in_cart == "Sauce Labs Backpack"
    add_item_backpack = driver.find_element(By.XPATH, CartPage.CART_ITEM_REMOVE_BUTTON).text
    assert add_item_backpack == "Remove"


def test_add_item_from_product_card(driver, authorization):
    item_backpack = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_HEADER).click()
    button_item = driver.find_element(By.XPATH, ItemPage.PRODUCT_ADD_TO_CART_BUTTON).click()
    button_cart = driver.find_element(By.XPATH, ItemPage.PRODUCT_CART_BUTTON).click()
    item_backpack_in_cart = driver.find_element(By.XPATH, CartPage.CART_ITEM_HEADER).text
    assert item_backpack_in_cart == "Sauce Labs Backpack"
    add_item_backpack = driver.find_element(By.XPATH, CartPage.CART_ITEM_REMOVE_BUTTON).text
    assert add_item_backpack == "Remove"

def test_delete_item_from_cart(driver, authorization):
    add_item_backpack = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_ADD_TO_CART_BUTTON).click()
    cart = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_CART).click()
    item_backpack_in_cart = driver.find_element(By.XPATH, CartPage.CART_ITEM_HEADER).text
    assert item_backpack_in_cart == "Sauce Labs Backpack"
    add_item_backpack = driver.find_element(By.XPATH, CartPage.CART_ITEM_REMOVE_BUTTON).text
    assert add_item_backpack == "Remove"
    button_remove = driver.find_element(By.XPATH, CartPage.CART_ITEM_REMOVE_BUTTON).click()
    quantity_item = driver.find_element(By.XPATH, CartPage.CART_BADGE).text
    assert quantity_item == ''

def test_delete_item_from_product_card(driver, authorization):
    item_backpack = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_HEADER).click()
    button_item = driver.find_element(By.XPATH, ItemPage.PRODUCT_ADD_TO_CART_BUTTON).click()
    button_cart = driver.find_element(By.XPATH, ItemPage.PRODUCT_CART_BUTTON).click()
    item_backpack_in_cart = driver.find_element(By.XPATH, CartPage.CART_ITEM_HEADER).text
    assert item_backpack_in_cart == "Sauce Labs Backpack"
    add_item_backpack = driver.find_element(By.XPATH, CartPage.CART_ITEM_REMOVE_BUTTON).text
    assert add_item_backpack == "Remove"
    remove_button = driver.find_element(By.XPATH, ItemPage.PRODUCT_ADD_BUTTON_REMOVE).click()
    quantity_item = driver.find_element(By.XPATH, ItemPage.PRODUCT_CART_BADGE).text
    assert quantity_item == ''

