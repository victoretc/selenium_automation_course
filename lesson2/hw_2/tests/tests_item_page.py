from selenium.webdriver.common.by import By
from lesson2.hw_2.locators.main_page_locators import MainPage
from lesson2.hw_2.tests.configuration import BaseUrls

def test_click_image(driver, authorization):
    item_image = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_IMG).click()
    current_page_url = driver.current_url
    assert BaseUrls.ITEM_PAGE_URL == current_page_url

def test_click_name(driver, authorization):
    item_image = driver.find_element(By.XPATH, MainPage.MAIN_ITEM_HEADER).click()
    current_page_url = driver.current_url
    assert BaseUrls.ITEM_PAGE_URL == current_page_url

