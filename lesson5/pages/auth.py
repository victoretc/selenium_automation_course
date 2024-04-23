from selene import browser, by, have
from selene.support.shared.jquery_style import s


def visit(url):
    browser.open(url)

def start():
    return s('//*[@id="startTest"]')

def login():
    s('#login').type('login')
    s('#password').type('password')
    s('#agree').click()
    browser.element(by.text('Зарегистрироваться')).click()

def success_message_have_text(text):
    s('#successMessage').should(have.text(text))






