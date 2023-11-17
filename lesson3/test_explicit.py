import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_login_with_explicit(driver, wait):
    driver.get("https://victoretc.github.io/selenium_waits/")
    title = driver.find_element(By.XPATH, "//h1[.='Практика с ожиданиями в Selenium']").text
    assert title == "Практика с ожиданиями в Selenium"

    begin_testing_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Начать тестирование']")))
    assert begin_testing_button.text == 'Начать тестирование'

    begin_testing_button.click()
    driver.find_element(By.XPATH, "//*[@id='login']").send_keys('m-nariman')
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys('19031983')
    driver.find_element(By.XPATH, "//*[@id='agree']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()
    loading_icon = driver.find_element(By.XPATH, "//div[.='Загрузка...']")
    assert loading_icon.text == 'Загрузка...'

    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[.='Загрузка...']")))
    successful_message = driver.find_element(By.XPATH, "//p[text()='Вы успешно зарегистрированы!']")
    assert successful_message.text == 'Вы успешно зарегистрированы!'
