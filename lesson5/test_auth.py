from pages import auth
import allure 

url = 'https://victoretc.github.io/selenium_waits/'

@allure.title('Авторизация')
def test_login():
    auth.visit(url)
    auth.start().click()
    auth.login()
    auth.success_message_have_text('Вы успешно зарегистрированы!')