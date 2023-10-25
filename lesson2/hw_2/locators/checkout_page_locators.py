class CheckoutPage:
    """-------------checkout page----------------"""

    CHECKOUT_HEADER = "//div[@class='app_logo']"
    CHECKOUT_BURGER_MENU = "//div[@class='bm-burger-button']"
    CHECKOUT_CART_BUTTON = "//div[@id='shopping_cart_container']"
    CHECKOUT_SECOND_HEADER = "//span[@class='title']"
    CHECKOUT_FIRST_NAME = "//input[@id='first-name']"
    CHECKOUT_LAST_NAME = "//input[@id='last-name']"
    CHECKOUT_ZIP_CODE = "//input[@id='postal-code']"
    CHECKOUT_CANCEL_BUTTON = "//button[@id='cancel']"
    CHECKOUT_CANCEL_BUTTON_IMG = "//img[@class='back-image']"
    CHECKOUT_CONTINUE_BUTTON = "//input[@id='continue']"

    """checkout page error buttons"""
    CHECKOUT_FIRST_NAME_ERROR_BUTTON = "#first-name ~svg"
    CHECKOUT_LAST_NAME_ERROR_BUTTON = "#last-name ~svg"
    CHECKOUT_ZIP_CODE_ERROR_BUTTON = "#postal-code ~svg"
    CHECKOUT_ERROR_MESSAGE_BUTTON = "//button[@class='error-button']"

    """checkout page error messages"""
    CHECKOUT_FIRST_NAME_ERROR_MESSAGE = "//h3[text()='Error: First Name is required']"
    CHECKOUT_LAST_NAME_ERROR_MESSAGE = "//h3[text()='Error: Last Name is required']"
    CHECKOUT_ZIP_CODE_ERROR_MESSAGE = "//h3[text()='Error: Postal Code is required']"