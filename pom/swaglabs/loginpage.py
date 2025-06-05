from pom.basepage import BasePage
from .inventorypage import InventoryPage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)

        self.username_field = self.find_element(*self.USERNAME_FIELD)
        self.password_field = self.find_element(*self.PASSWORD_FIELD)
        self.login_button = self.find_element(*self.LOGIN_BUTTON)

    def type_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def type_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)
    
    def click_login(self):
        self.login_button.click()
        # "Browse" to the inventory page
        return InventoryPage(self.driver)
    