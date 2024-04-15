def test_auth_positive(login_page):
    login_page.open()

    login_page.start_button().click()

    login_page.login_field()\
        .password_field()\
        .agree_button()\
        .registration_button()

    assert login_page.loader().is_displayed()
    assert login_page.success_message().text == 'Вы успешно зарегистрированы!'
