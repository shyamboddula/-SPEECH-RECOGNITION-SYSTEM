from selenium import webdriver
from selenium.webdriver.common.by import By

class Infow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()

# Create an instance and call the function
assist = Infow()
assist.get_info("Today's NEWS")

input("Press Enter to close the browser...")  
assist.driver.quit()  # Ensure the browser closes properly