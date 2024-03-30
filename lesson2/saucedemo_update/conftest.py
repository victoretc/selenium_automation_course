import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver 
    print('\nquit browser...')
    driver.quit()



