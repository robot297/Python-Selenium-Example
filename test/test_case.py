import unittest
from selenium import webdriver
from pom.google.homepage import HomePage

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Wait for elements to load
        self.driver.get("https://www.google.com")
        self.home_page = HomePage(self.driver)

    def test_search(self):
        results = self.home_page.search("Selenium Python")
        for result in results:
            print(result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
