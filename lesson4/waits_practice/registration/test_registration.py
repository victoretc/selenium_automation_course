from locators import HEADER, START_TESTING_BUTTON, LOGIN_FIELD, PASSWORDD_FIELD, AGREE_CHECKBOX, REGISTRATION_BUTTON, LOADER, SUCCESS_MESSAGE
from data import REGISTRATION_PAGE
from data import PASSWORD
from selenium.webdriver.support import expected_conditions as EC

def test_registration_positive(driver, wait, random_email):
    # Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/ 
    driver.get(REGISTRATION_PAGE)
    
    # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
    header = wait.until(EC.visibility_of_element_located(HEADER))
    assert header.text == "Практика с ожиданиями в Selenium"

    # Дождаться появления кнопки "Начать тестирование" 
    # Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    start_testing_button = wait.until(EC.element_to_be_clickable(START_TESTING_BUTTON))
    
    # Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    start_testing_button.click()

    # Ввод логина: Ввести "login" в поле для логина.
    login_field = wait.until(EC.visibility_of_element_located(LOGIN_FIELD))
    login_field.clear()
    login_field.send_keys(random_email)

    # Ввод пароля: Ввести "password" в поле для пароля.
    password_field = wait.until(EC.visibility_of_element_located(PASSWORDD_FIELD))
    password_field.clear()
    password_field.send_keys((random_email))

    # Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    checkbox_agree = wait.until(EC.visibility_of_element_located(AGREE_CHECKBOX))
    checkbox_agree.click()
    assert checkbox_agree.is_selected() == True 

    # Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    registration_button = wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON))
    registration_button.click()

    # Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    loader = wait.until(EC.visibility_of_element_located(LOADER))

    # Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_message = wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
    assert success_message.text == "Вы успешно зарегистрированы!"






