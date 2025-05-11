from pom.basepage import BasePage
from .confirmationpagelocator import ConfirmationPageLocator


class ConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ConfirmationPageLocator()

        self.finish = self.find_element(*self.locator.FINISH)

    def click_finish(self):
        self.finish.click()
        