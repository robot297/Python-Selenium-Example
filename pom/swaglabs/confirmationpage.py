from pom.basepage import BasePage
from selenium.webdriver.common.by import By


class ConfirmationPage(BasePage):
    FINISH = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)

        self.finish = self.find_element(*self.FINISH)

    def click_finish(self):
        self.finish.click()
        