from pom.basepage import BasePage
from .inventorypagelocator import InventoryPageLocator
from .productpage import ProductPage

from selenium.webdriver.support.ui import Select


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = InventoryPageLocator()

        self.product_sort = Select(self.find_element(*self.locator.SORT))
        self.first_item = self.find_element(*self.locator.FIRST_ITEM)

    def sort_items(self, sort_option):
        self.product_sort.select_by_value(sort_option)        
    
    def get_first_item_name(self):
        self.first_item.click()
        return ProductPage(self.driver)
    