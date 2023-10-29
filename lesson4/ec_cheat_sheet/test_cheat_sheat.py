from selenium.webdriver.support import expected_conditions as EC
from urls import PAGE_ALERTS
from locators import ALERT_AFTER_5_SECOND

def test_alert_is_present(driver, wait):
    driver.get(PAGE_ALERTS)
    wait.until(EC.element_to_be_clickable(ALERT_AFTER_5_SECOND)).click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()


