from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.women_tab = (By.LINK_TEXT, 'Women')

    def go_to_women_section(self):
        self.driver.find_element(*self.women_tab).click()
