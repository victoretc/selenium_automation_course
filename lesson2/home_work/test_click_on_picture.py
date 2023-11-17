from selenium.webdriver.common.by import By
import time
from locators import PRODUCT_IMAGE
from data import PRODUCT_URL


def test_picture_card(driver, auth):

    driver.find_element(By.XPATH, PRODUCT_IMAGE).click()

    time.sleep(2)
    assert driver.current_url == PRODUCT_URL
