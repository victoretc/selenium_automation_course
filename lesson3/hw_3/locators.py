class AuthLocators:
    AUTH_H1_TEXT = "//h1[text()='Практика с ожиданиями в Selenium']"
    START_TEST_BUTTON = "//button[@id='startTest']"
    VISION_START_TEST_BUTTON = "#startTest:not(.hidden)"
    REGISTRATION_FORM = "//div[@id='registrationForm']"
    LOGIN_FORM_TEXT = "//label[@for='login']"
    PASSWORD_FORM_TEXT = "//label[@for='password']"
    INPUT_LOGIN = "//input[@id='login']"
    INPUT_PASSWORD = "//input[@id='password']"
    AGREE_CHECKBOX = "//input[@id='agree']"
    REGISTRATION_BUTTON = "//button[@id='register']"
    LOADER = "//div[@id='loader']"
    LOADER_TEXT = "//div[text()='Загрузка...']"
    SUCCESS_MESSAGE = "//p[@id='successMessage']"
    VISION_SUCCESS_MESSAGE = '//p[@id="successMessage" and not(contains(@class, "hidden"))]'

