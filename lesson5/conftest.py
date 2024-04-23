import pytest
from selene import browser, support
import allure_commons
import allure
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser_management():
    
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser.config.driver_options = options
    browser.config.window_height = 100
    browser.config.window_width = 500
    browser.config.timeout = 10

    browser.config._wait_decorator = support._logging.wait_with(
            context=allure_commons._allure.StepContext
        )
    
    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    browser.quit()