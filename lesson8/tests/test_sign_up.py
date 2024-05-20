from luma_project.pages import sign_up, account
from luma_project.test_data import user_data

def test_sign_up():
    sign_up.open()
    sign_up.type_first_name("first_name")
    sign_up.type_last_name("last_name")
    sign_up.type_email(user_data.email)
    sign_up.type_password("Password123$$__")
    sign_up.type_password_confirm("Password123$$__")
    sign_up.create_account().click()
    account.should_be_opened()

def test_sign_up_with_invalid_email():
    sign_up.open()
    sign_up.type_first_name(user_data.first_name)
    sign_up.type_last_name(user_data.last_name)
    sign_up.type_email(user_data.password)
    sign_up.type_password(user_data.password)
    sign_up.type_password_confirm(user_data.password)
    sign_up.create_account().click()
    sign_up.should_be_opened()
