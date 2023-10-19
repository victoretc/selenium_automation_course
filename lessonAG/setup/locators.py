from selenium.webdriver.common.by import By

# auth page
USERNAME = (By.XPATH, '//input[@data-test="username"]')
PASSWORD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')

# auth error
ERROR = (By.XPATH, '//h3[@data-test="error"]')

# shopping cart locator
SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
CART_BUTTON = (By.CLASS_NAME, "cart_button")

# burger menu locator
BM_BURGER_BUTTON = (By.CLASS_NAME, "bm-burger-button")

# burgher menu items
INVENTORY_SIDEBAR_LINK = (By.ID, "inventory_sidebar_link")
ABOUT_SIDEBAR_LINK = (By.ID, "about_sidebar_link")
LOGOUT_SIDEBAR_LINK = (By.ID, "logout_sidebar_link")
RESET_SIDEBAR_LINK = (By.ID, "reset_sidebar_link")


# inventory
INVENTORY_ITEM_IMG = (By.CSS_SELECTOR, "img.inventory_item_img")
INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
BTN_INVENTORY = (By.CLASS_NAME, "btn_inventory")
INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")


# inventory item
INVENTORY_DETAILS_NAME = (By.CLASS_NAME, "inventory_details_name")

# inventory filter
ACTIVE_OPTION = (By.CLASS_NAME, "active_option")
PRODUCT_SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")

# checkout
CHECKOUT = (By.ID, "checkout")
FIRST_NAME = (By.ID, "first-name")
LAST_NAME = (By.ID, "last-name")
POSTAL_CODE = (By.ID, "postal-code")
CONTINUE = (By.ID, "continue")
FINISH = (By.ID, "finish")
CONTINUE_SHOPPING = (By.ID, "continue-shopping")
CANCEL = (By.ID, "cancel")
BACK_TO_PRODUCTS = (By.ID, "back-to-products")


# github checkbox login form
USERNAME_FIELD = (By.ID, "username")
PASSWORD_FIELD = (By.ID, "password")
AGREEMENT_CHECKBOX = (By.ID, "agreement")
REGISTER_BUTTON = (By.ID, "registerButton")

