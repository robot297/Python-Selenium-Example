import time

from selenium import webdriver
from pom.swaglabs.loginpage import LoginPage

if __name__ == '__main__':
    # Initialize the Chrome WebDriver
    chrome_options = webdriver.ChromeOptions()
    preferences = {
        'profile.password_manager_leak_detection': False
    }
    chrome_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize the browser window
    
    # Open the Swag Labs website
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)  # Wait for elements to load
    
    login_page = LoginPage(driver)
    login_page.type_username('standard_user')
    login_page.type_password('secret_sauce')
    inventory_page = login_page.click_login()
    
    inventory_page.sort_items('hilo')  # Sort items from high to low price
    product_page = inventory_page.get_first_item_name()  # Click on the first item

    product_page.click_add_to_cart()  # Add the item to the cart
    cart_page = product_page.click_shopping_cart()  # Click on the shopping cart icon

    checkout_page = cart_page.click_checkout()  # Click on the checkout button
    
    checkout_page.type_first_name('John')  # Enter first name
    checkout_page.type_last_name('Doe')  # Enter last name
    checkout_page.type_zip_code('12345')  # Enter zip code
    confirmation_page = checkout_page.click_continue()  # Click on the continue button
    confirmation_page.click_finish()  # Click on the finish button
    
    # Wait for a few seconds to see the result
    time.sleep(5)
    
    # Close the browser
    driver.quit()
