class AuthPage:
    """-------------auth page----------------"""

    """auth page logo"""
    AUTH_PAGE_LOGO = "//div[@class='login_logo']"
    """username input field"""
    USERNAME_FIELD = '//input[@data-test="username"]'
    """password input field"""
    PASSWORD_FIELD = '//input[@data-test="password"]'
    """login confirm button"""
    LOGIN_BUTTON = '//input[@data-test="login-button"]'

    """auth error borderlines"""
    # USERNAME_ERROR_BORDER = ".input_error.error"
    # PASSWORD_ERROR_BORDER = ".input_error.error"

    """auth error buttons"""
    USERNAME_ERROR_CLOSE_BUTTON = "#user-name ~svg"
    PASSWORD_ERROR_CLOSE_BUTTON = "#password ~svg"
    AUTH_ERROR_MESSAGE_BUTTON = "//button[@class='error-button']"
    LOCKED_USER_ERROR_BUTTON = "//button[@class='error-button']"

    """auth error messages"""
    USERNAME_ERROR_CLOSE_MESSAGE = "//h3[@data-test='error']"
    PASSWORD_ERROR_CLOSE_MESSAGE = "//h3[@data-test='error']"
    BOTH_USERNAME_PASSWORD_ERROR_MESSAGE = "//h3[@data-test='error']"  # incorrect error message
    LOCKED_USER_ERROR_MESSAGE = "//h3[@data-test='error']"

    """auth error message container"""
    MESSAGE_ERROR_BORDER = "//div[@class='error-message-container error']"

