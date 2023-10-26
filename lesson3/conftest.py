import logging

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from util import chrome_options

GRID_URL = "http://localhost:4444/wd/hub"


@pytest.fixture
def options():
    options = chrome_options()
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    # driver.start_session()
    yield driver
    driver.quit()


# ToDo Remote with CDP nad for other browsers
@pytest.fixture
def _driver(options):
    driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)


@pytest.fixture(scope='function')
def log_path():
    suffix = 'my'
    log_path = 'log_file_' + suffix + '.log'

    yield log_path

    logger = logging.getLogger('selenium')
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()

    # os.remove(log_path)


@pytest.fixture
def log(log_path):
    logger = logging.getLogger('selenium')

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)

    # logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.INFO)
