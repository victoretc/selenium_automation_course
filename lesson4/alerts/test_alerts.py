from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time 


def test_alert_accept_now(driver, wait):
    driver.get('https://demoqa.com/alerts')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="alertButton"]'))).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'You clicked a button'
    alert.accept()

def test_alert_accept_after_5_sec(driver, wait):
    driver.get('https://demoqa.com/alerts')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="timerAlertButton"]'))).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'This alert appeared after 5 seconds'
    alert.accept()

def test_alert_confirm_cancel(driver, wait):
    driver.get('https://demoqa.com/alerts')
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="confirmButton"]'))).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'Do you confirm action?'
    alert.dismiss()
    wait.until(EC.text_to_be_present_in_element(((By.XPATH, '//span[@id="confirmResult"]')), 'You selected Cancel'))

def test_alert_confirm_ok(driver, wait):
    driver.get('https://demoqa.com/alerts')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="confirmButton"]'))).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'Do you confirm action?'
    alert.accept()
    wait.until(EC.text_to_be_present_in_element(((By.XPATH, '//span[@id="confirmResult"]')), 'You selected Ok'))

    
def test_alert_prompt(driver, wait):
    driver.get('https://demoqa.com/alerts')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="promtButton"]'))).click()
    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == 'Please enter your name'
    alert.send_keys("Hello World")
    alert.accept()
    wait.until(EC.text_to_be_present_in_element(((By.XPATH, '//span[@id="promptResult"]')), 'You entered Hello World'))






