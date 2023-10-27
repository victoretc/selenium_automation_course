class BaseUrls:
    CHECKBOX_URL = "https://the-internet.herokuapp.com/checkboxes"
    ADD_REMOVE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    AUTH_URL = "https://the-internet.herokuapp.com/basic_auth"
    BROKEN_IMG_URL = "https://the-internet.herokuapp.com/broken_images"

class BaseLocators:
    CHECKBOX_1 = "#checkboxes >input:nth-child(1)"
    ADD_BTN = "//button[@onclick='addElement()']"
    DELETE_BTN = "//button[text()='Delete']"
    DELETE_BTN_WITHOUT_BUTTON_CLASS_DELETE = "//div[@id='elements' and not(contains(@class, 'added-manually'))]"
    FIRST_BROKEN_IMG = ".example> img:nth-child(2)"
    SECOND_BROKEN_IMG = ".example> img:nth-child(3)"
    ALL_IMAGES = "img"
