from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN, PASSWORD, MAIN_PAGE

def test_login_form(driver):
    driver.get(MAIN_PAGE)
    
    # вводим валидный логин в поле "Username"
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
  
    # вводим валидный пароль в поле "Password"
    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    # кликаем на кнопку "Login"
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

