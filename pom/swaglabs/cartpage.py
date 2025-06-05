from pom.basepage import BasePage
from .checkoutpage import CheckoutPage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver):
        super().__init__(driver)

        self.checkout_button = self.find_element(*self.CHECKOUT_BUTTON)

    def click_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.driver)
    