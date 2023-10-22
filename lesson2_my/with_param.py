import locators


def test_add_all_items_from_catalog(driver, login):
    # add items
    for a in locators.ALL_ELEM_IN_CATALOG:
        driver.find_element(*a).click()
    # go to cart and check it
    driver.find_element(*locators.BASKET).click()
    # check item in cart
    driver.find_element(*locators.BASKET).click()
    count_before_removing = driver.find_element(*locators.COUNT_ITEMS_IN_BASKET).text

    assert int(count_before_removing) == 3


