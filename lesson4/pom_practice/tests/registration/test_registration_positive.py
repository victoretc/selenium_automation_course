from data import REGISTRATION_PAGE
from pages.registration_page import RegistrationPage


class TestRegistration():
    def test_registration_positive(self, driver, random_email):
        page = RegistrationPage(driver, url = REGISTRATION_PAGE)

        # Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/ 
        page.open()

        # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
        assert page.header().text == "Практика с ожиданиями в Selenium"

        # Начать тестирование: Кликнуть по кнопке "Начать тестирование".
        page.start_testing_button().click()

        # Ввод логина: Ввести "login" в поле для логина. 
        page.login_field().clear()
        page.login_field().send_keys(random_email)

        #  Ввод пароля: Ввести "password" в поле для пароля.
        page.password_field().clear()
        page.password_field().send_keys(random_email)

        # Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
        page.agree_checkbox().click()
        assert page.agree_checkbox().is_selected() == True 

        # Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
        page.registration_button().click()

        #  Проверка загрузки: Удостовериться, что появился индикатор загрузки.
        assert page.loader().text == 'Загрузка...'

        #  Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы!".
        assert page.success_message().text == "Вы успешно зарегистрированы!"








    

