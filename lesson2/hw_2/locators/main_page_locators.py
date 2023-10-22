class MainPage:
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
    MAIN_ITEM_ADD_TO_CART_BUTTON = "//button[@id='add-to-cart-sauce-labs-backpack']"  # "//button[text()='Add to cart']"
    MAIN_ITEM_ADD_BUTTON_REMOVE = "//button[text()='Remove']"

    """main page - footer"""
    MAIN_FOOTER_TWITTER_LINK = "//li[@class='social_twitter']"
    MAIN_FOOTER_FACEBOOK_LINK = "//li[@class='social_facebook']"
    MAIN_FOOTER_LINKEDIN_LINK = "//li[@class='social_linkedin']"
    MAIN_FOOTER_COPY = "//div[@class='footer_copy']"

