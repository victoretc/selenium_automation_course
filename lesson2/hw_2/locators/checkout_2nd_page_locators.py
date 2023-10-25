class CheckoutSecondPage:
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

