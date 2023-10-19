from setup.conftest import *


def test_open_product_details_from_img(driver, inventory):
    """Успешный переход к карточке товара после клика на картинку товара"""
    product = choice(driver.find_elements(*INVENTORY_ITEM_IMG))
    product_name = product.get_attribute(ALT)
    product.click()

    assert driver.find_element(*INVENTORY_DETAILS_NAME).text == product_name


def test_open_product_details_from_name(driver, inventory):
    """Успешный переход к карточке товара после клика на название товара"""
    product = choice(driver.find_elements(*INVENTORY_ITEM_NAME))
    product_name = product.text
    product.click()

    assert driver.find_element(*INVENTORY_DETAILS_NAME).text == product_name


def test_add_product_to_shopping_cart(driver, inventory):
    """Корзина > Добавление товара в корзину через каталог"""
    product_add_button = choice(driver.find_elements(*BTN_INVENTORY))
    product_name = product_add_button.get_attribute(DATA_TEST)
    product_add_button.click()

    driver.get(CART_URL)

    assert driver.find_element(*CART_BUTTON).get_attribute(DATA_TEST)[7:] == product_name[12:]


@pytest.mark.parametrize('direction', [True, False])
def test_filter_by_name(driver, inventory, direction):
    """Проверка работоспособности фильтра (A to Z) и (Z to A)"""
    names = driver.find_elements(*INVENTORY_ITEM_NAME)
    initial_order = [x.text for x in names]

    dropdown = Select(driver.find_element(*PRODUCT_SORT_CONTAINER))
    dropdown.select_by_visible_text([FILTER_AZ_TEXT, FILTER_ZA_TEXT][direction])

    active_option = driver.find_element(*ACTIVE_OPTION)
    assert active_option.text == [FILTER_AZ_TEXT, FILTER_ZA_TEXT][direction]

    names = driver.find_elements(*INVENTORY_ITEM_NAME)
    final_order = [x.text for x in names]

    assert final_order == sorted(initial_order, reverse=direction)


@pytest.mark.parametrize('direction', [True, False])
def test_filter_by_price(driver, inventory, direction):
    """Проверка работоспособности фильтра (low to high) и (high to low)"""
    prices = driver.find_elements(*INVENTORY_ITEM_PRICE)
    initial_prices = [float(price.text[1:]) for price in prices]

    dropdown = Select(driver.find_element(*PRODUCT_SORT_CONTAINER))
    dropdown.select_by_visible_text([FILTER_LOHI_TEXT, FILTER_HILO_TEXT][direction])

    prices = driver.find_elements(*INVENTORY_ITEM_PRICE)
    final_prices = [float(price.text[1:]) for price in prices]
    #print(*final_prices)
    assert final_prices == sorted(initial_prices, reverse=direction)
