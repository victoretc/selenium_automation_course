from os import environ

from selenium import webdriver


def chrome_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if environ.get('GITLAB_CI') or environ.get('GITHUB_ACTIONS') == 'true':
        options.add_argument('--headless')  # Run Chrome in headless mode.
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    return options
