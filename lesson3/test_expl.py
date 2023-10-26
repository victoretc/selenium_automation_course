import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import util


@pytest.fixture
def chrome_options():
    options = util.chrome_options()
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
    visible_after_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Visible After 5 Seconds']")))
    assert visible_after_button.text == 'Visible After 5 Seconds'
