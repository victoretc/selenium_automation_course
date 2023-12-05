from setup.conftest import *


def test_add_product_to_cart(driver, product_details):
    """Корзина > Добавление товара в корзину из карточки товара"""
    add_to_cart_button = driver.find_element(*BTN_INVENTORY)
    product_name = add_to_cart_button.get_attribute(DATA_TEST)
    add_to_cart_button.click()

    driver.get(CART_URL)

    cart_item_name = driver.find_element(*CART_BUTTON).get_attribute(DATA_TEST)

    assert product_name[12:] == cart_item_name[7:]