from selenium.webdriver.common.by import By


class LoginPageLocator(object):
    # Define locators for the elements on the login page
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
