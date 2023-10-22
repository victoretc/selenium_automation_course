from selenium.webdriver.common.by import By
import locators


def test_add_item_from_catalog(driver, login):
    # add item
    driver.find_element(*locators.ELEM1_ADD_FROM_CATALOG).click()
    # go to cart and check it
    driver.find_element(*locators.BASKET).click()
    # check item in cart
    expected_name = "Sauce Labs Bike Light"
    actual_name = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Bike Light')]").text

    assert expected_name == actual_name


def test_add_good_to_cart(driver, login):
    # select item
    text_before = driver.find_element(*locators.ELEM3_IN_CATALOG).text

    # add item to cart
    driver.find_element(*locators.ELEM3_ADD_FROM_CATALOG).click()

    # go to cart and check it
    driver.find_element(*locators.BASKET).click()
    text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_1_title_link'] > div[class='inventory_item_name']").text

    assert text_before == text_after


def test_remove_good_from_cart(driver, login):
    # select item
    # add item 1 to cart
    driver.find_element(*locators.ELEM1_ADD_FROM_CATALOG).click()
    # add item 2 to cart
    driver.find_element(*locators.ELEM3_ADD_FROM_CATALOG).click()
    # go to cart and check it
    driver.find_element(*locators.BASKET).click()
    count_before_removing = driver.find_element(*locators.COUNT_ITEMS_IN_BASKET).text
    driver.find_element(*locators.REMOVE_ELEM3_FROM_BASKET).click()
    count_after_removing = driver.find_element(*locators.COUNT_ITEMS_IN_BASKET).text

    assert int(count_after_removing) == int(count_before_removing) - 1


def test_remove_good_from_cart2(driver, login):
    driver.find_element(*locators.ELEM3_ADD_FROM_CATALOG).click()
    driver.find_element(*locators.BASKET).click()
    driver.find_element(*locators.REMOVE_ELEM3_FROM_BASKET).click()

    assert len(driver.find_elements(*locators.ELEM3_TITLE_IN_BASKET)) == 0


