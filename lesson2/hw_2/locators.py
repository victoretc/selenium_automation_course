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
USERNAME_ERROR_CLOSE_MESSAGE = "//h3[text()='Epic sadface: Username is required']"
PASSWORD_ERROR_CLOSE_MESSAGE = "//h3[text()='Epic sadface: Password is required']"
BOTH_USERNAME_PASSWORD_ERROR_MESSAGE = "//h3[text()='Epic sadface: Username is required']"  # incorrect error message

"""auth error message container"""
MESSAGE_ERROR_BORDER = "//div[@class='error-message-container error']"

"""-------------main page----------------"""

"""main page - header"""
MAIN_PAGE_BURGER_MENU = "//button[@id='react-burger-menu-btn']"
MAIN_PAGE_HEADER_TEXT = "//div[@class='app_logo']"
MAIN_PAGE_CART = "//a[@class='shopping_cart_link']"
MAIN_PAGE_CART_BADGE = "//span[@class='shopping_cart_badge']"
MAIN_PAGE_SECOND_HEADER = "//span[@class='title']"
MAIN_PAGE_FILTER = "//select[@class='product_sort_container']"

"""main page - burger menu"""
MAIN_PAGE_BM_ALL_ITEMS_BUTTON = "//a[text()='All Items']"
MAIN_PAGE_BM_ABOUT_BUTTON = "//a[text()='About']"
MAIN_PAGE_BM_LOGOUT_BUTTON = "//a[text()='Logout']"
MAIN_PAGE_BM_RESET_BUTTON = "//a[text()='Reset App State']"
MAIN_PAGE_BM_CLOSE_BUTTON = "//button[text()='Close Menu']"

"""main page - filter"""
AZ_FILTER = "//option[@value='az']"
ZA_FILTER = "//option[@value='za']"
LTH_FILTER = "//option[@value='lohi']"  # low to high
HTL_FILTER = "//option[@value='hilo']"  # high to low

"""main page - body. items - cards of product"""
MAIN_ITEM_IMG = "//div[@class='inventory_item_img']"
MAIN_ITEM_HEADER = "//div[@class='inventory_item_name ']"
MAIN_ITEM_DESC = "//div[@class='inventory_item_desc']"
MAIN_ITEM_PRICE = "//div[@class='inventory_item_price']"
MAIN_ITEM_ADD_TO_CART_BUTTON = "//button[text()='Add to cart']"
MAIN_ITEM_ADD_BUTTON_REMOVE = "//button[text()='Remove']"

"""main page - footer"""
MAIN_FOOTER_TWITTER_LINK = "//li[@class='social_twitter']"
MAIN_FOOTER_FACEBOOK_LINK = "//li[@class='social_facebook']"
MAIN_FOOTER_LINKEDIN_LINK = "//li[@class='social_linkedin']"
MAIN_FOOTER_COPY = "//div[@class='footer_copy']"

"""-------------item page----------------"""

PRODUCT_BACK_BUTTON = "//button[@id='back-to-products']"
PRODUCT_BACK_BUTTON_IMG = "//img[@class='back-image']"
PRODUCT_IMG = "//div[@class='inventory_details_img_container']"
PRODUCT_HEADER = "//div[@class='inventory_details_name large_size']"
PRODUCT_DESC = "//div[@class='inventory_details_desc large_size']"
PRODUCT_PRICE = "//div[@class='inventory_details_price']"
PRODUCT_ADD_TO_CART_BUTTON = "//button[text()='Add to cart']"
PRODUCT_ADD_BUTTON_REMOVE = "//button[text()='Remove']"

"""-------------cart page----------------"""

"""cart"""
CART_HEADER_TEXT = "//div[@class='app_logo']"
CART_BURGER_MENU = "//img[@class='bm-icon']"
CART_SECOND_HEADER_TEXT = "//span[@class='title']"
CART_QTY = "//div[@class='cart_quantity_label']"
CART_DESC = "//div[@class='cart_desc_label']"
CART_ITEM_QUANTITY = "//div[@class='cart_quantity']"
CART_ITEM_HEADER = "//div[@class='inventory_item_name']"
CART_ITEM_DESC = "//div[@class='inventory_item_desc']"
CART_ITEM_PRICE = "//div[@class='inventory_item_price']"
CART_ITEM_REMOVE_BUTTON = "//button[text()='Remove']"
CART_CONTINUE_BUTTON = "//button[@data-test='continue-shopping']"
CART_CONTINUE_IMG = "//img[@class='back-image']"
CART_CHECKOUT_BUTTON = "//button[@data-test='checkout']"

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

"""-------------checkout 2nd page----------------"""

TWO_CHECKOUT_HEADER = "//div[@class='app_logo']"
TWO_CHECKOUT_BURGER_MENU = "//div[@class='bm-burger-button']"
TWO_CHECKOUT_CART_BUTTON = "//a[@class='shopping_cart_link']"
TWO_CHECKOUT_SECOND_HEADER = "//span[@class='title']"
TWO_CHECKOUT_QTY = "//div[@class='cart_quantity_label']"
TWO_CHECKOUT_DESC = "//div[@class='cart_desc_label']"
TWO_CHECKOUT_ITEM_QUANTITY = "//div[@class='cart_quantity']"
TWO_CHECKOUT_ITEM_HEADER = "//div[@class='inventory_item_name']"
TWO_CHECKOUT_ITEM_DESC = "//div[@class='inventory_item_desc']"
TWO_CHECKOUT_ITEM_PRICE = "//div[@class='inventory_item_price']"

"""payment block info"""
TWO_CHECKOUT_PAYMENT_INFO = ".summary_value_label:nth-child(2)"
TWO_CHECKOUT_SHIPPING_INFO = ".summary_value_label:nth-child(4)"
TWO_CHECKOUT_PRICE_ITEM = "//div[@class='summary_subtotal_label']"
TWO_CHECKOUT_TAX = "//div[@class='summary_tax_label']"
TWO_CHECKOUT_TOTAL_PRICE = "//div[@class='summary_info_label summary_total_label']"

"""checkout 2nd page buttons"""
TWO_CHECKOUT_CANCEL_BUTTON = "//button[@id='cancel']"
TWO_CHECKOUT_CANCEL_IMG = "//img[@class='back-image']"
TWO_CHECKOUT_FINISH_BUTTON = "//button[@id='finish']"

"""-------------checkout complete page----------------"""

CHECKOUT_COMPLETE_HEADER = "//div[@class='app_logo']"
CHECKOUT_COMPLETE_BURGER_MENU = "//div[@class='bm-burger-button']"
CHECKOUT_COMPLETE_CART_BUTTON = "//div[@id='shopping_cart_container']"
CHECKOUT_COMPLETE_SECOND_HEADER = "//span[@class='title']"
CHECKOUT_COMPLETE_IMG = "//img[@class='pony_express']"
CHECKOUT_COMPLETE_THANK_HEADER = "//h2[@class='complete-header']"
CHECKOUT_COMPLETE_TEXT = "//div[@class='complete-text']"
CHECKOUT_COMPLETE_BUTTON = "//button[@id='back-to-products']"

