from selene import browser, have

url='https://magento.softwaretestingboard.com/customer/account/'

def open():
    browser.open(url)

def should_be_opened():
    browser.should(have.url(url))

