from base.seleniumbase import BasePage
from locators import HEADER, START_TESTING_BUTTON, LOGIN_FIELD, PASSWORDD_FIELD, AGREE_CHECKBOX, REGISTRATION_BUTTON, LOADER, SUCCESS_MESSAGE

class RegistrationPage(BasePage):
    def header(self):
        return self.is_visible(HEADER)

    def start_testing_button(self):
        return self.is_clickable(START_TESTING_BUTTON)

    def login_field(self):
        return self.is_visible(LOGIN_FIELD)

    def password_field(self):
        return self.is_visible(PASSWORDD_FIELD)

    def agree_checkbox(self):
        return self.is_visible(AGREE_CHECKBOX)

    def registration_button(self):
        return self.is_clickable(REGISTRATION_BUTTON)

    def loader(self):
        return self.is_visible(LOADER)

    def success_message(self):
        return self.is_clickable(SUCCESS_MESSAGE)
    