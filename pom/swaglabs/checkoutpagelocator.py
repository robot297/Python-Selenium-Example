from selenium.webdriver.common.by import By

class CheckoutPageLocator(object):
    # Define locators for the elements on the checkout page
    # Example locators:
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    