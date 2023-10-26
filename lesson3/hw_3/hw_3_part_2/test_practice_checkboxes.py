from selenium.webdriver.common.by import By
from lesson3.hw_3.hw_3_part_2.configuration import BaseUrls, BaseLocators
from lesson3.hw_3.hw_3_part_2.confest import driver

def test_checkbox(driver):
    """check checkbox"""

    driver.get(BaseUrls.CHECKBOX_URL)
    checkbox_1 = driver.find_element(By.CSS_SELECTOR, BaseLocators.CHECKBOX_1)
    click_checkbox = checkbox_1.click()

    assert checkbox_1.is_selected()


