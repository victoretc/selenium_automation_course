import requests
from selenium.webdriver.common.by import By
from lesson3.hw_3.hw_3_part_2.configuration import BaseUrls, BaseLocators
from lesson3.hw_3.hw_3_part_2.confest import driver


def test_find_broken_image(driver):
    """find broken images"""

    driver.get(BaseUrls.BROKEN_IMG_URL)
    broken_img_counter = 0
    image_list = driver.find_elements(By.TAG_NAME, BaseLocators.ALL_IMAGES)

    for img in image_list:
        response = requests.get(img.get_attribute('src'))
        if response.status_code != 200:
            broken_img_counter += 1
            print(img.get_attribute('outerHTML') + " is broken.")
    assert broken_img_counter == 0, "check the images links above the error"

