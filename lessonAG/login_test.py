from setup.conftest import *


@pytest.mark.parametrize('credentials', good_credentials_lst)
def test_good_login(driver, credentials):
    """Авторизация > Авторизация используя корректные данные"""
    login(driver, *credentials)
    assert driver.current_url == INVENTORY_URL


@pytest.mark.parametrize('credentials', bad_credentials_lst)
def test_bad_login(driver, credentials):
    """Авторизация > Авторизация используя некорректные данные"""
    alert, *credentials = credentials
    login(driver, *credentials)
    assert driver.find_element(*ERROR).text == alert