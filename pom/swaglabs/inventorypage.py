from pom.basepage import BasePage
from .productpage import ProductPage

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):

        # Example locators:
    SORT = (By.CLASS_NAME, 'product_sort_container')
    FIRST_ITEM = (By.CLASS_NAME, 'inventory_item_name')
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        super().__init__(driver)

        self.product_sort = Select(self.find_element(*self.SORT))
        self.first_item = self.find_element(*self.FIRST_ITEM)

    def sort_items(self, sort_option):
        self.product_sort.select_by_value(sort_option)        
    
    def get_first_item_name(self):
        self.first_item.click()
        return ProductPage(self.driver)
    