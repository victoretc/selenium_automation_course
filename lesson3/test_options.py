import pytest
from selenium import webdriver

import util


@pytest.fixture
def chrome_options():
    options = util.chrome_options()
    # options.add_argument('--window-size=100,100')
    options.add_argument('--incognito')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_example(driver):
    driver.get('https://www.saucedemo.com/')
    assert driver.current_url == 'https://www.saucedemo.com/'
