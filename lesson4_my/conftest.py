from faker import Faker
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout = 15)
    return wait


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()