import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from lessonAG.setup.data import *
from lessonAG.setup.locators import *
from time import sleep
from random import choice
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="module")
def mdriver():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("useAutomationExtension", False)
    # service = ChromeService()
    # driver = webdriver.Chrome(service=service, options=options)

    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(3)
    driver.get("https://google.com/")

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def driver(mdriver):
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)
    driver = mdriver
    original_window = driver.current_window_handle
    driver.switch_to.new_window('tab')

    driver.implicitly_wait(5)
    driver.get(BASE_URL)

    yield driver

    # driver.quit()
    driver.close()
    driver.switch_to.window(original_window)


@pytest.fixture(scope="function")
def _driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    driver.get(BASE_URL)

    yield driver

    driver.quit()

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(3)
#     driver.get(BASE_URL)
#
#     yield driver
#
#     driver.quit()


@pytest.fixture(params=[("standard_user", "secret_sauce")])
def standard_user(request):
    return request.param


@pytest.fixture(params=[('user', 'user')])
def user(request):
    return request.param


# from selenium.webdriver import Firefox, FirefoxOptions
# opts = FirefoxOptions()
# opts.add_argument("--width=2560")
# opts.add_argument("--height=1440")
# driver = Firefox(options=opts)
@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get(BASE_URL)
    yield driver

    driver.quit()


def login(driver, username, password):
    driver.find_element(*USERNAME).send_keys(username)
    driver.find_element(*PASSWORD).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()


@pytest.fixture
def inventory(driver, standard_user):
    login(driver, *standard_user)


@pytest.fixture
def burger_menu(driver, inventory):
    driver.find_element(*BM_BURGER_BUTTON).click()


@pytest.fixture
def product_details(driver, inventory):
    driver.get(ITEM_URL + str(choice([*range(6)])))


@pytest.fixture
def cart_with_product(driver, inventory):
    choice(driver.find_elements(*BTN_INVENTORY)).click()
    driver.get(CART_URL)

# def check_exists(strategy, locator):
#     return len(driver.find_elements(strategy, locator)) > 0
