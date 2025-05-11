class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        return self.driver.current_url
    