from setup.conftest import *
import time


def test_delete_product(driver, cart_with_product):
    """Корзина > Удаление товара из корзины через корзину"""
    driver.find_element(*CART_BUTTON).click()

    assert len(driver.find_elements(*CART_BUTTON)) == 0

    # found = True
    # try:
    #     driver.find_element(By.CLASS_NAME, CART_BUTTON)
    # except NoSuchElementException:
    #     found = False
    #
    # assert found is False


def test_delete_product_from_cart(driver, cart_with_product):
    """Корзина > Удаление товара из корзины через карточку товара"""

    driver.find_element(*INVENTORY_ITEM_NAME).click()
    driver.find_element(*BTN_INVENTORY).click()

    driver.get(CART_URL)

    assert len(driver.find_elements(*CART_BUTTON)) == 0

    # found = len(driver.find_elements(*CART_BUTTON)) > 0
    # assert found is False
    #
    # found = True
    # try:
    #     driver.find_element(*CART_BUTTON)
    # except NoSuchElementException:
    #     found = False
    # assert found is False


def test_checkout(driver, cart_with_product):
    """Оформление заказа > Оформление заказа используя корректные данные"""
    first_name, last_name, postal_code = ('first', 'last', '1234')

    driver.find_element(*CHECKOUT).click()
    driver.find_element(*FIRST_NAME).send_keys(first_name)
    driver.find_element(*LAST_NAME).send_keys(last_name)
    driver.find_element(*POSTAL_CODE).send_keys(postal_code)
    time.sleep(3)
    driver.find_element(*CONTINUE).click()
    time.sleep(3)
    driver.find_element(*FINISH).click()
    time.sleep(3)
    assert driver.current_url == CHECKOUT_COMPLETE_URL
