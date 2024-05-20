from selene import browser, have
from selene.support.shared.jquery_style import s

url='https://magento.softwaretestingboard.com/customer/account/create/'

def open():
    browser.open(url)

def type_first_name(name):
    s('#firstname').type(name)

def type_last_name(name):
    s('#lastname').type(name)

def type_email(email):
    s('#email_address').type(email)

def type_password(password):
    s('#password').type(password)

def type_password_confirm(password):
    s('#password-confirmation').type(password)

def create_account():
    return s('[title="Create an Account"]')

def should_be_opened():
    browser.should(have.url(url))