from pom.basepage import BasePage
from .cartpagelocator import CartPageLocator
from .checkoutpage import CheckoutPage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CartPageLocator()

        self.checkout_button = self.find_element(*self.locator.CHECKOUT_BUTTON)

    def click_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.driver)
    