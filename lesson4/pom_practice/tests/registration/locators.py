from selenium.webdriver.common.by import By

# # Registration Page 

HEADER = (By.XPATH, '//h1')
START_TESTING_BUTTON = (By.XPATH, "//button[text()='Начать тестирование']")
LOGIN_FIELD = (By.XPATH, "//input[@id='login']")
PASSWORDD_FIELD = (By.XPATH, "//input[@id='password']")
AGREE_CHECKBOX = (By.XPATH, "//input[@id='agree']")
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") 
LOADER = (By.XPATH, "//div[@id='loader']")
SUCCESS_MESSAGE = (By.XPATH, "//p[@id='successMessage']")
