from pom.basepage import BasePage
from .checkoutpagelocator import CheckoutPageLocator
from .confirmationpage import ConfirmationPage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CheckoutPageLocator()

        self.first_name_field = self.find_element(*self.locator.FIRST_NAME_FIELD)
        self.last_name_field = self.find_element(*self.locator.LAST_NAME_FIELD)
        self.postal_code_field = self.find_element(*self.locator.POSTAL_CODE_FIELD)
        self.continue_button = self.find_element(*self.locator.CONTINUE_BUTTON)

    def type_first_name(self, first_name):
        self.first_name_field.clear()
        self.first_name_field.send_keys(first_name)

    def type_last_name(self, last_name):
        self.last_name_field.clear()
        self.last_name_field.send_keys(last_name)

    def type_zip_code(self, zip_code):
        self.postal_code_field.clear()
        self.postal_code_field.send_keys(zip_code)

    def click_continue(self):
        self.continue_button.click()
        return ConfirmationPage(self.driver)
    