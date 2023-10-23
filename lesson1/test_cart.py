from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from random import choice


def test_add_item_from_catalog(driver, login):

    first_item_add_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    first_item_add_button.click()

    item_in_the_cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    #assert item_in_the_cart.is_displayed()
    assert item_in_the_cart.text == '1'

def test_remove_item_from_the_cart(driver, login):

    first_item_add_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    first_item_add_button.click()

    cart_button = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    cart_button.click()

    remove_button_cart = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button_cart.click()

    try:
        driver.find_element(By.XPATH, '//div[@class="cart_item_label"]')
        assert False, 'There are items in the cart'
    except NoSuchElementException:
        assert True
    # assert driver.find_elements(By.XPATH, '//div[@class="removed_cart_item"]')

def test_remove_item_from_the_cart_list(driver, login):
    random_items = driver.find_elements(By.CSS_SELECTOR, 'button.btn_inventory')
    first_item = choice(random_items)
    first_item.click()
    second_item = choice(random_items)
    second_item.click()

    driver.get('https://www.saucedemo.com/cart.html')
    # driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    list_items_before = driver.find_elements(By.CSS_SELECTOR, 'div.cart_item') #2
    # driver.find_element(By.CSS_SELECTOR, 'button.cart_button').click()
    driver.find_elements(By.CSS_SELECTOR, 'button.cart_button')[0].click()
    list_items_after = driver.find_elements(By.CSS_SELECTOR, 'div.cart_item') #1
    assert len(list_items_before) == len(list_items_after) + 1


def test_add_item_from_items_card(driver, login):
    items_image = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]')
    items_image.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    item_in_the_cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    # assert item_in_the_cart.is_displayed()
    assert item_in_the_cart.text == '1'

def test_remove_item_from_cart_from_items_card(driver, login):

    items_image = driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Backpack"]')
    items_image.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    remove_button_items_card = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_button_items_card.click()
    time.sleep(3)

    assert driver.find_elements(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')






