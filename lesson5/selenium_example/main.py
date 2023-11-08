from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get('https://www.selenium.dev/blog/2023/whats-new-in-selenium-manager-with-selenium-4.11.0/')

assert driver.current_url == 'https://www.selenium.dev/blog/2023/whats-new-in-selenium-manager-with-selenium-4.11.0/'