from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
   
    def start_button(self):
        return self.is_visible((By.XPATH, '//*[@id="startTest"]'))

    def login_field(self):
        self.is_visible((By.XPATH, '//*[@id="login"]')).send_keys('login')
        return self

    def password_field(self):
        self.is_visible((By.XPATH, '//*[@id="password"]')).send_keys('password')
        return self
    
    def agree_button(self):
        self.is_visible((By.XPATH, '//*[@id="agree"]')).click()
        return self
    
    def registration_button(self):
        self.is_visible((By.XPATH, '//*[@id="register"]')).click()
        return 
    
    def loader(self):
        return self.is_visible((By.XPATH, '//*[@id="loader"]'))
    
    def success_message(self):
        return self.is_visible((By.XPATH, '//*[@id="successMessage"]'))

    







