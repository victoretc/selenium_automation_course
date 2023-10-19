# AUTH
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# URLS
ABOUT_URL = "https://saucelabs.com/"
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = BASE_URL + "inventory.html"
CART_URL = BASE_URL + "cart.html"
ITEM_URL = BASE_URL + "inventory-item.html?id="

#attr
DATA_TEST = "data-test"
ALT = "alt"
HREF = "href"

# checkout
CHECKOUT_STEP_ONE_URL = BASE_URL + "checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = BASE_URL + "checkout-step-two.html"
CHECKOUT_COMPLETE_URL = BASE_URL + "checkout-complete.html"


# checkout error messages
MSG_FIRST_NAME_REQUIRED = "Error: First Name is required"
MSG_LAST_NAME_REQUIRED = "Error: Last Name is required"
MSG_POSTAL_CODE_REQUIRED = "Error: Postal Code is required"

# filter options text
# values = ['az', 'za', 'lohi', 'hilo']
FILTER_AZ_TEXT = "Name (A to Z)"
FILTER_ZA_TEXT = "Name (Z to A)"
FILTER_LOHI_TEXT = "Price (low to high)"
FILTER_HILO_TEXT = "Price (high to low)"

# auth error messages
MSG_WRONG_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
MSG_AUTHORIZED_USERS_ONLY = "Epic sadface: You can only access '/inventory.html' when you are logged in."
MSG_USERNAME_REQUIRED = "Epic sadface: Username is required"
MSG_PASSWORD_REQUIRED = "Epic sadface: Password is required"
MSG_USER_LOCKED_OUT = "Epic sadface: Sorry, this user has been locked out."

good_credentials_lst = [("standard_user", "secret_sauce"),
                        ('problem_user', 'secret_sauce'),
                        ('performance_glitch_user', 'secret_sauce'),
                        ('error_user', 'secret_sauce'),
                        ('visual_user', 'secret_sauce')]
bad_credentials_lst = [(MSG_WRONG_CREDENTIALS, 'user', 'user'),
                       (MSG_USERNAME_REQUIRED, '', 'empty_user'),
                       (MSG_PASSWORD_REQUIRED, 'empty_password', ''),
                       (MSG_USER_LOCKED_OUT, 'locked_out_user', 'secret_sauce')]

# gitHub checkbox login form
AUTH_URL = "https://victoretc.github.io/webelements_information/"