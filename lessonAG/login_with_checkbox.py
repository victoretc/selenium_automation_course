from setup.conftest import *


def test_login_form_with_checkbox(driver):
    """Авторизация c чекбоксом"""
    user, password = ("user", "password")
    driver.get(AUTH_URL)
    driver.find_element(*USERNAME_FIELD).send_keys(user)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    checkbox = driver.find_element(*AGREEMENT_CHECKBOX)
    if not checkbox.is_selected():
        checkbox.click()

    driver.find_element(*REGISTER_BUTTON).click()

    assert driver.current_url == AUTH_URL + '?'