import locators
from selenium.webdriver.common.by import By


def test_go_to_item_card_by_pic(driver, login):
    # click on img
    driver.find_element(*locators.ELEM4_PIC_IN_CATALOG).click()

    # check item card
    item_URL = driver.current_url
    expected_URL = locators.CARD_ITEM4_URL

    assert expected_URL == item_URL


def test_go_to_item_card_by_title(driver, login):
    # click on title
    driver.find_element(*locators.ELEM5_TITLE_IN_CATALOG).click()

    # check item card
    expected_title = "Sauce Labs Fleece Jacket"
    actual_title = driver.find_element(By.XPATH, "//*[contains(text(),'Sauce Labs Fleece Jacket')]").text

    assert expected_title == actual_title
