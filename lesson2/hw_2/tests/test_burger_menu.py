import time
from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.auth_page_locators import AuthPage
from lesson2.hw_2.locators.main_page_locators import MainPage
from lesson2.hw_2.tests.configuration import BaseUrls


def test_btn_about(driver, authorization):
    burger_menu = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BURGER_MENU).click()
    about_btn = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BM_ABOUT_BUTTON).click()
    current_page_url = driver.current_url
    assert BaseUrls.ABOUT_URL == current_page_url

def test_btn_reset(driver, authorization):
    burger_menu = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BURGER_MENU).click()
    about_btn = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BM_RESET_BUTTON).click()
    cart_item = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_CART).text
    assert cart_item == ''

def test_logout(driver, authorization):
    burger_menu = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BURGER_MENU).click()
    time.sleep(1)
    logout_btn = driver.find_element(By.XPATH, MainPage.MAIN_PAGE_BM_LOGOUT_BUTTON).click()
    auth_page_logo = driver.find_element(By.XPATH, AuthPage.AUTH_PAGE_LOGO).text
    current_url = driver.current_url
    assert auth_page_logo == 'Swag Labs'
    assert current_url == BaseUrls.BASE_URL

