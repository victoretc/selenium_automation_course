import time

import pytest
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.parametrize('name', ['Olya', '@5tg_'])
def test_checkout(driver, login, cart_with_item, name):
    driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    # заполнение формы
    fake = Faker()
    driver.find_element(By.XPATH, '//input[@data-test="firstName"]').send_keys(name)
    driver.find_element(By.XPATH, '//input[@data-test="lastName"]').send_keys(fake.last_name())
    driver.find_element(By.XPATH, '//input[@data-test="postalCode"]').send_keys(fake.postcode())

    driver.find_element(By.XPATH, '//input[@data-test="continue"]').click()
    driver.find_element(By.XPATH, '//button[@data-test="finish"]').click()

    assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text == 'Thank you for your order!'


def test_checkout_empty_form_error_message(driver, login, cart_with_item):
    driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    driver.find_element(By.XPATH, '//input[@data-test="continue"]').click()
    error_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
    assert error_text == 'Error: First Name is required'