from selenium.webdriver.common.by import By
import time
from locators import PRODUCT_TITLE
from data import PRODUCT_URL


def test_title_of_product(driver, auth):

    driver.find_element(By.XPATH, PRODUCT_TITLE).click()

    assert driver.current_url == PRODUCT_URL
    time.sleep(2)
