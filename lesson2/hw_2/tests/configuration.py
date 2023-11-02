"""All constants that relate to tests"""

class BaseUrls:
    """----------urls----------"""

    """base page"""
    BASE_URL = 'https://www.saucedemo.com/'
    """main page"""
    PRODUCT_PAGE_URL = 'https://www.saucedemo.com/inventory.html'
    """cart page"""
    CART_URL = 'https://www.saucedemo.com/cart.html'
    """item id - 4 page"""
    ITEM_PAGE_URL = 'https://www.saucedemo.com/inventory-item.html?id=4'
    """checkout 1 step page"""
    CHECKOUT_FIRST_STEP_URL = 'https://www.saucedemo.com/checkout-step-one.html'
    """checkout 2 step page"""
    CHECKOUT_SECOND_STEP_URL = 'https://www.saucedemo.com/checkout-step-two.html'
    """checkout complete"""
    CHECKOUT_COMPLETE_URL = 'https://www.saucedemo.com/checkout-complete.html'
    """burger menu links"""
    ABOUT_URL = 'https://saucelabs.com/'

    """----------footer links----------"""
    """social media urls"""
    FOOTER_TWITTER_URL = "https://twitter.com/saucelabs"
    FOOTER_FACEBOOK_URL = "https://www.facebook.com/saucelabs"
    FOOTER_LINKEDIN_URL = "https://www.linkedin.com/company/sauce-labs/"

class TestData:
    """----------auth - page----------"""

    """login data"""
    LOGIN_STANDARD_USER = "standard_user"
    LOGIN_INVALID_USER = "user"
    LOGIN_LOCKED_USER = "locked_out_user"
    LOGIN_EMPTY = ''
    """password data"""
    PASSWORD_STANDARD_USER = "secret_sauce"
    INVALID_PASSWORD = "user"
    PASSWORD_LOCKED_USER = "secret_sauce"
    PASSWORD_ALL = "secret_sauce"
    PASSWORD_EMPTY = ''

class CheckoutTestData:
    """----------checkout page data----------"""

    """valid data"""
    VALID_NAME = 'John'
    VALID_SURNAME = 'Carter'
    VALID_ZIP = 1372

    """invalid data"""

    """checkout name"""
    INVALID_NAME_ONE_CHAR = 'A'
    INVALID_NAME_ONLY_NUM = 11.1
    INVALID_NAME_EMPTY = ''
    """checkout surname"""
    INVALID_SURNAME_ONE_CHAR = 'C'
    INVALID_SURNAME_ONLY_NUM = 22.2
    INVALID_SURNAME_EMPTY = ''
    """checkout zip name"""
    INVALID_ZIP_STR = '1372'
    INVALID_ZIP_EMPTY = ''
