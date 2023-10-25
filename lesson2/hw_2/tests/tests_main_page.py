from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.main_page_locators import MainPage
from lesson2.hw_2.locators.cart_page_locators import CartPage
from lesson2.hw_2.locators.checkout_page_locators import CheckoutPage
from lesson2.hw_2.locators.checkout_2nd_page_locators import CheckoutSecondPage
from lesson2.hw_2.locators.checkout_complete_page_locators import CompletePage
from lesson2.hw_2.tests.configuration import CheckoutTestData, BaseUrls


def test_checkout_valid_user(driver, authorization):
    add_item_backpack = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_ADD_TO_CART_BUTTON).click()
    item_name = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_HEADER).text
    cart = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_CART).click()
    item_backpack_in_cart = driver.find_element(By.XPATH, CartPage.CART_ITEM_HEADER).text
    assert item_backpack_in_cart == "Sauce Labs Backpack"
    checkout_button = driver.find_element(By.XPATH, CartPage.CART_CHECKOUT_BUTTON).click()
    firstname = driver.find_element(By.XPATH, CheckoutPage.CHECKOUT_FIRST_NAME).send_keys(CheckoutTestData.VALID_NAME)
    lastname = driver.find_element(By.XPATH, CheckoutPage.CHECKOUT_LAST_NAME).send_keys(CheckoutTestData.VALID_SURNAME)
    zip_code = driver.find_element(By.XPATH, CheckoutPage.CHECKOUT_ZIP_CODE).send_keys(CheckoutTestData.VALID_ZIP)
    continue_button = driver.find_element(By.XPATH, CheckoutPage.CHECKOUT_CONTINUE_BUTTON).click()
    item_name_checkout = driver.find_element(By.XPATH, CheckoutSecondPage.TWO_CHECKOUT_ITEM_HEADER).text
    assert item_name == item_name_checkout
    finish_button = driver.find_element(By.XPATH, CheckoutSecondPage.TWO_CHECKOUT_FINISH_BUTTON).click()
    current_url = driver.current_url
    assert current_url == BaseUrls.CHECKOUT_COMPLETE_URL

