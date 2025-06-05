from pom.basepage import BasePage
from pom.swaglabs.cartpage import CartPage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.NAME, 'add-to-cart')
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')
    
    def __init__(self, driver):
        super().__init__(driver)
        
        self.add_to_cart_button = self.find_element(*self.ADD_TO_CART_BUTTON)
        self.shopping_cart = self.find_element(*self.SHOPPING_CART)

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_shopping_cart(self):
        self.shopping_cart.click()
        return CartPage(self.driver)
    