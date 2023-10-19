from setup.conftest import *


def test_close_menu(driver, burger_menu):
    """Бургер меню > Проверка работоспособности кнопки "Close" """
    x = (By.ID, "react-burger-cross-btn")


def test_open_inventory(driver, burger_menu):
    """Бургер меню > Проверка работоспособности кнопки "AlL Items" """
    # no ?
    inventory_button = driver.find_element(*INVENTORY_SIDEBAR_LINK)
    assert inventory_button.is_enabled() and inventory_button.is_displayed()
    inventory_button.click()
    assert driver.current_url == INVENTORY_URL


def test_open_about(driver, burger_menu):
    """Бургер меню > Проверка работоспособности кнопки "About" """

    about_button = driver.find_element(*ABOUT_SIDEBAR_LINK)
    assert about_button.is_enabled() and about_button.is_displayed()
    assert about_button.get_attribute(HREF) == ABOUT_URL
    about_button.click()
    assert driver.current_url == ABOUT_URL


def test_logout(driver, burger_menu):
    """Бургер меню > Выход из системы"""

    logout_button = driver.find_element(*LOGOUT_SIDEBAR_LINK)
    assert logout_button.is_enabled() and logout_button.is_displayed()
    logout_button.click()
    assert driver.current_url == BASE_URL


def test_reset_app_state(driver, burger_menu):
    """Бургер меню > Проверка работоспособности кнопки "Reset App State" """

    reset_button_is_found = len(driver.find_elements(*RESET_SIDEBAR_LINK)) > 0
    assert reset_button_is_found

    reset_button = driver.find_element(*RESET_SIDEBAR_LINK)
    assert reset_button.is_enabled() and reset_button.is_displayed()

    # is_clickable = True
    # try:
    #     reset_button.click()
    # except ElementClickInterceptedException:
    #     is_clickable = False
    # assert is_clickable is True


def show(elems, loc):
    print(f"\r\nFound {len(elems)} elements -> {loc}")
    for item in elems:
        print(f'text content of {["hidden", "displayed"][item.is_displayed()]} element: \n', item.get_attribute("textContent"))
        print(f'outer HTML of {["hidden", "displayed"][item.is_displayed()]} element:', item.get_attribute("outerHTML"), sep="\r\n")


def test_about_extended_mode(driver):

    driver.get(ABOUT_URL)
    sleep(13)

    v_div = "div.MuiBox-root.css-jv9ibt"
    h_div = "div.MuiBox-root.css-mntjpt"
    elems = driver.find_elements(By.CSS_SELECTOR, v_div)
    show(elems, v_div)

    elems = driver.find_elements(By.CSS_SELECTOR, h_div)
    show(elems, h_div)
