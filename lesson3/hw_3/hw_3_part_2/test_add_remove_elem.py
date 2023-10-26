from selenium.webdriver.common.by import By
from lesson3.hw_3.hw_3_part_2.configuration import BaseUrls, BaseLocators
from lesson3.hw_3.hw_3_part_2.confest import driver

def test_add_elem(driver):
    """add element"""

    driver.get(BaseUrls.ADD_REMOVE_URL)
    add_elem = driver.find_element(By.XPATH, BaseLocators.ADD_BTN)
    add_elem.click()

    delete_elem = driver.find_element(By.XPATH, BaseLocators.DELETE_BTN)
    assert delete_elem.is_displayed()

def test_remove_elem(driver):
    """delete element"""

    driver.get(BaseUrls.ADD_REMOVE_URL)
    add_elem = driver.find_element(By.XPATH, BaseLocators.ADD_BTN)
    add_elem.click()
    delete_elem = driver.find_element(By.XPATH, BaseLocators.DELETE_BTN)

    assert delete_elem.is_displayed()

    delete_elem.click()

    deleted_elem = driver.find_element(By.XPATH, BaseLocators.DELETE_BTN_WITHOUT_BUTTON_CLASS_DELETE)  # add special locator
    assert deleted_elem.is_displayed()
