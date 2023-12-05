from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, START_BUTTON, INPUT_LOGIN, INPUT_PSW, CHECK_BOX, CLICK_REGISTER, MSG, LOADER


def enter_on_victor_login_form(driver, wait):
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(START_BUTTON)).click()
    expected_text = "Практика с ожиданиями в Selenium"
    actual_text = driver.find_element(By.XPATH, '//h1').text
    assert actual_text == expected_text


def test_input_login_data(driver, wait):
    enter_on_victor_login_form(driver, wait)
    wait.until(EC.element_to_be_clickable(INPUT_LOGIN)).send_keys("asdd@as.sa")
    wait.until(EC.element_to_be_clickable(INPUT_PSW)).send_keys("5677@domn.dr")
    checkbox_agree = wait.until(EC.element_to_be_clickable(CHECK_BOX))
    checkbox_agree.click()
    assert checkbox_agree.is_selected() == True


def test_registration(driver, wait):
    enter_on_victor_login_form(driver, wait)
    wait.until(EC.element_to_be_clickable(INPUT_LOGIN)).send_keys("asdd@as.sa")
    wait.until(EC.element_to_be_clickable(INPUT_PSW)).send_keys("5677@domn.dr")
    wait.until(EC.element_to_be_clickable(CHECK_BOX)).click()
    wait.until(EC.element_to_be_clickable(CLICK_REGISTER))
    wait.until(EC.visibility_of_element_located(LOADER))
    msg = wait.until(EC.visibility_of_element_located(MSG))
    expected_text = "Вы успешно зарегистрированы!"
    actual_text = msg.text
    assert expected_text == actual_text

