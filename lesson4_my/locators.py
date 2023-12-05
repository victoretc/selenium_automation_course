from selenium.webdriver.common.by import By


BASE_URL = 'https://victoretc.github.io/selenium_waits/'
START_BUTTON = (By.XPATH, "//*[@id='startTest']")
INPUT_LOGIN = (By.XPATH, "//*[@id='login']")
INPUT_PSW = (By.XPATH, "//*[@id='password']")
CHECK_BOX = (By.XPATH, "//*[@id='agree']")
CLICK_REGISTER = (By.XPATH, "//*[@id='register']")
LOADER = (By.XPATH, '//*[@id="loader"]')
MSG = (By.XPATH, '//*[@id="successMessage"]')
