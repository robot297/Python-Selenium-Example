from selenium.webdriver.common.by import By

class InventoryPageLocator(object):
    # Define locators for the elements on the inventory page
    # Example locators:
    SORT = (By.CLASS_NAME, 'product_sort_container')
    FIRST_ITEM = (By.CLASS_NAME, 'inventory_item_name')
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')
