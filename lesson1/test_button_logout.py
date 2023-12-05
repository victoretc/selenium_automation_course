from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_logout():
    driver.get("https://www.saucedemo.com/")
    url_before = driver.current_url
 
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # в левой части есть меню магазина, там команда logout
    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(3)

    logout = driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link")
    logout.click()
    time.sleep(1)

    # если вышел , то возврат на начальную страницу, можно проверить через УРЛ
    url_after = driver.current_url
    #print(url_after)

    assert url_after == url_before
    driver.quit()       #когда будет закрывающая фикстура, то удалить
