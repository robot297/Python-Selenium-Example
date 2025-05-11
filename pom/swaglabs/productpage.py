from pom.basepage import BasePage
from .productpagelocator import ProductPageLocator
from pom.swaglabs.cartpage import CartPage

class ProductPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProductPageLocator()
        
        self.add_to_cart_button = self.find_element(*self.locator.ADD_TO_CART_BUTTON)
        self.shopping_cart = self.find_element(*self.locator.SHOPPING_CART)

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_shopping_cart(self):
        self.shopping_cart.click()
        return CartPage(self.driver)
    