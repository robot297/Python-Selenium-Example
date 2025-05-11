from pom.basepage import BasePage
from .loginpagelocator import LoginPageLocator
from .inventorypage import InventoryPage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocator()

        self.username_field = self.find_element(*self.locator.USERNAME_FIELD)
        self.password_field = self.find_element(*self.locator.PASSWORD_FIELD)
        self.login_button = self.find_element(*self.locator.LOGIN_BUTTON)

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
    