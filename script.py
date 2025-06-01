import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    """This script is condensed down to a single file for simplicity.
    It automates the process of logging into the Swag Labs website, sorting items,
    selecting an item, adding it to the cart, and completing the checkout process.
    It uses Selenium WebDriver to interact with the web elements.

    I also found and did actions on web elements on the same line for simplicity.
    """
    chrome_options = webdriver.ChromeOptions()
    preferences = {
        'profile.password_manager_leak_detection': False
    }
    chrome_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the browser window
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)  # Wait for elements to load
    # Login
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.XPATH, "//option[@value='hilo']").click()  # Sort items from high to low price
    driver.find_element(By.CLASS_NAME, 'inventory_item_name').click()  # Click on the first item
    driver.find_element(By.NAME, 'add-to-cart').click()  # Click on the add to cart button
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()  # Click on the shopping cart icon
    driver.find_element(By.ID, 'checkout').click()  # Click on the checkout button
    driver.find_element(By.ID, 'first-name').send_keys('John')  # Enter first name
    driver.find_element(By.ID, 'last-name').send_keys('Doe')  # Enter last name
    driver.find_element(By.ID, 'postal-code').send_keys('12345')  # Enter zip code
    driver.find_element(By.ID, 'continue').click()  # Click on the continue button
    driver.find_element(By.ID, 'finish').click()  # Click on the finish button
    time.sleep(2)  # Wait for 2 seconds
    driver.quit()
