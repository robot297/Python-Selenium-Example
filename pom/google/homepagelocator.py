from selenium.webdriver.common.by import By

class HomePageLocator(object):
    # Define locators for the elements on the home page
    # Example locators:
    SEARCH_BOX = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    RESULTS = (By.CSS_SELECTOR, 'h3')
    