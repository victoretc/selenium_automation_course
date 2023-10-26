from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://victoretc.github.io/selenium_waits/"
H1_TAG = (By.TAG_NAME, "h1")
START_TEST_BUTTON = (By.ID, "startTest")
LOGIN_FIELD = (By.ID, "login")
PASSWORD_FIELD = (By.ID, "password")
AGREE_CHECKBOX = (By.ID, "agree")
REGISTER_BUTTON = (By.ID, "register")
LOADER_DIV = (By.ID, "loader")
P_TAG = (By.ID, "successMessage")

users_lst = [("user", "pass"), ("user1", "pass1")]


# ToDO пустой юзер\пасс\согласие - JS(alert('Пожалуйста, заполните все поля и согласитесь с правилами.');)


def register(driver, credentials):
    """Вводит логин и пароль, принимает соглашение и нажимает регистрировать"""
    username, password = credentials
    driver.find_element(*LOGIN_FIELD).send_keys(username)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*AGREE_CHECKBOX).click()
    driver.find_element(*REGISTER_BUTTON).click()


def show_state(el):
    """Печатает статус элемента"""
    displayed = ["not ", ""][el.is_displayed()]
    enabled = ["not ", ""][el.is_enabled()]
    print(f"is {displayed}displayed and {enabled}enabled")


@pytest.mark.parametrize('credentials', users_lst)
def test_registration_with_sleep(driver, wait, credentials):
    """С использованием time.sleep()"""
    driver.get(BASE_URL)
    assert driver.current_url == BASE_URL
    assert driver.find_element(*H1_TAG).text == "Практика с ожиданиями в Selenium"
    sleep(5.2)
    driver.find_element(*START_TEST_BUTTON).click()
    register(driver, credentials)
    assert driver.find_element(*LOADER_DIV).text == "Загрузка..."
    sleep(3.2)
    assert driver.find_element(*P_TAG).text == "Вы успешно зарегистрированы!"


@pytest.mark.parametrize('credentials', users_lst)
def test_registration_with_implicit_waits(driver, wait, credentials):
    """С использованием Implicit waits"""
    driver.get(BASE_URL)
    driver.implicitly_wait(6)
    assert driver.current_url == BASE_URL
    assert driver.find_element(*H1_TAG).text == "Практика с ожиданиями в Selenium"

    driver.find_element(*START_TEST_BUTTON).click()
    register(driver, credentials)
    assert driver.find_element(*LOADER_DIV).text == "Загрузка..."

    # p_tag = driver.find_element(*P_TAG)
    # show_state(p_tag)
    # while not p_tag.is_displayed():
    #     sleep(0.5)
    #     print('waiting p_tag to be visible', p_tag.text)
    #     show_state(p_tag)
    # assert p_tag.text == "Вы успешно зарегистрированы!"

    # driver.implicitly_wait(6)
    # assert driver.find_element(*P_TAG).text == "Вы успешно зарегистрированы!"

    assert driver.find_element(By.CSS_SELECTOR, 'p[class=""]').text == "Вы успешно зарегистрированы!"
    assert driver.find_element(By.XPATH, '//p[@class=""]').text == "Вы успешно зарегистрированы!"


@pytest.mark.parametrize('credentials', users_lst)
def test_registration_with_explicit_waits(driver, wait, credentials):
    """С использованием Explicit waits и Expected Conditions"""
    driver.get(BASE_URL)
    assert driver.current_url == BASE_URL
    assert driver.find_element(*H1_TAG).text == "Практика с ожиданиями в Selenium"
    wait.until(EC.visibility_of_element_located(START_TEST_BUTTON)).click()
    register(driver, credentials)
    assert wait.until(EC.visibility_of_element_located(LOADER_DIV)).text == "Загрузка..."
    assert wait.until(EC.visibility_of_element_located(P_TAG)).text == "Вы успешно зарегистрированы!"
