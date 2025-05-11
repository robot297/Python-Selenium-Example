import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Wait for elements to load
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for result in results:
        print(result.text)
    
    time.sleep(5)  # Wait for a few seconds to see the results
    driver.quit()
