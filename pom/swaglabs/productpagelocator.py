from selenium.webdriver.common.by import By

class ProductPageLocator(object):
    # Define locators for the elements on the product page
    # Example locators:
    ADD_TO_CART_BUTTON = (By.NAME, 'add-to-cart')
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')
