from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_visible_after_with_implicit_wait(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    vissible_after_button = driver.find_element(By.XPATH, "//button[text()='Visible After 5 Seconds']")
    assert vissible_after_button.is_displayed()





