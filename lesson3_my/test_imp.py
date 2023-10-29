from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_visible_after_with_explicit_waits(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    button_after_5_sec = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enableAfter"]')))
    assert button_after_5_sec.text == "Will enable 5 seconds"


def test_change_color_after_5_sec(driver, wait):
    # not works
    driver.get('https://demoqa.com/dynamic-properties')
    button_color_before = driver.find_element(By.XPATH, '//*[@id="colorChange"]')
    b1 = button_color_before.value_of_css_property('font-color')
    print(b1)
    time.sleep(6)
    button_color_after = driver.find_element(By.XPATH, '//*[@id="colorChange"]')
    b2 = button_color_after.value_of_css_property('font-color')
    assert b1 != b2

