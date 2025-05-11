from pom.basepage import BasePage
from .homepagelocator import HomePageLocator

from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocator()

        self.search_box = self.find_element(*self.locator.SEARCH_BOX)
        self.search_button = self.find_element(*self.locator.SEARCH_BUTTON)



    def search(self, query):
        self.search_box.clear()
        self.search_box.send_keys(query)
        self.search_box.send_keys(Keys.RETURN)
        # Wait for the results to load
        self.driver.implicitly_wait(10)
        return ResultsPage(self.driver)


class ResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocator()
        self.results = self.find_element(*self.locator.RESULTS)